import pandas as pd
import streamlit as st

@st.cache_data
def load_data(file_path):
    """
    KOSIS 스타일의 CSV 데이터를 로드하고 전처리합니다.
    """
    try:
        # 1. 데이터 로드 (utf-8 또는 cp949 인코딩 시도)
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='cp949')

        # 2. 데이터 전처리 (Wide -> Long Format 변환)
        # '시도별' 컬럼을 기준으로 나머지 연도 컬럼들을 녹입니다(melt).
        key_column = '시도별'
        if key_column in df.columns:
            df_melted = df.melt(id_vars=[key_column], var_name='연도', value_name='인구수')
            
            # 연도 컬럼을 정수형으로 변환 (예: '2020' -> 2020)
            # 숫자가 아닌 문자가 포함될 경우를 대비해 처리
            df_melted['연도'] = pd.to_numeric(df_melted['연도'], errors='coerce')
            
            # 인구수 컬럼의 ',' 제거 및 숫자 변환
            if df_melted['인구수'].dtype == 'object':
                 df_melted['인구수'] = df_melted['인구수'].str.replace(',', '').astype(float)
            
            return df_melted
        else:
            return df

    except Exception as e:
        st.error(f"데이터 로드 중 오류 발생: {e}")
        return pd.DataFrame()

def get_basic_stats(df):
    """
    기초 통계량(EDA)을 반환합니다.
    """
    summary = {
        "총 데이터 수": len(df),
        "연도 범위": f"{df['연도'].min()} ~ {df['연도'].max()}" if '연도' in df.columns else "N/A",
        "지역 수": df['시도별'].nunique() if '시도별' in df.columns else 0,
        "평균 인구수": f"{df['인구수'].mean():,.0f}명" if '인구수' in df.columns else "N/A"
    }
    return summary
