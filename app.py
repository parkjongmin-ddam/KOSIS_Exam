import streamlit as st
import pandas as pd
import os
from modules.data_loader import load_data, get_basic_stats
from modules.plot_utils import DataVisualizer

# 1. 페이지 설정
st.set_page_config(
    page_title="KOSIS 통계 대시보드",
    page_icon="📊",
    layout="wide"
)

# 2. 사이드바 - 데이터 로드
st.sidebar.title("🛠️ 데이터 설정")
uploaded_file = st.sidebar.file_uploader("KOSIS CSV 파일 업로드", type=["csv"])

# 기본 제공 예제 데이터 경로
SAMPLE_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "kosis_population_sample.csv")

if not uploaded_file:
    st.sidebar.info("📂 예제 데이터(2020~2023 인구)를 사용합니다.")
    current_df = load_data(SAMPLE_DATA_PATH)
else:
    current_df = load_data(uploaded_file)

if current_df is not None and not current_df.empty:
    
    # 3. 메인 - 제목 및 개요
    st.title("📊 KOSIS 통계 데이터 시각화")
    st.markdown("통계청(KOSIS) 데이터를 기반으로 한 인터랙티브 대시보드입니다.")
    
    # 4. 데이터 전처리 결과 확인 (EDA)
    st.header("1. 데이터 탐색 (EDA)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 데이터 요약")
        stats = get_basic_stats(current_df)
        st.metric("총 데이터 행 수", f"{stats['총 데이터 수']:,} 개")
        st.metric("분석 기간", stats['연도 범위'])
        st.metric("지역 수", f"{stats['지역 수']} 개")
        st.metric("평균 값", stats['평균 인구수'])
        
    with col2:
        st.subheader("🔍 원본 데이터 미리보기")
        st.dataframe(current_df.head(10), use_container_width=True)

    # 5. 시각화 (Visualizer 사용)
    st.header("2. 데이터 시각화")
    
    viz = DataVisualizer(current_df)
    
    # 탭으로 구분하여 차트 보여주기
    tab1, tab2, tab3 = st.tabs(["📈 연도별 추세", "📊 지역별 비교", "🗺️ 히트맵 분포"])
    
    with tab1:
        st.caption("시간의 흐름에 따른 변화를 확인합니다.")
        fig_trend = viz.plot_trend()
        if fig_trend:
            st.plotly_chart(fig_trend, use_container_width=True)
            
    with tab2:
        st.caption("특정 연도의 지역별 데이터를 비교합니다.")
        
        # 연도 선택 필터
        years = sorted(current_df['연도'].unique(), reverse=True)
        selected_year = st.selectbox("비교할 연도 선택", years, index=0)
        
        fig_bar = viz.plot_bar_chart(selected_year)
        if fig_bar:
            st.plotly_chart(fig_bar, use_container_width=True)
            
    with tab3:
        st.caption("전체적인 분포 패턴을 색상으로 확인합니다.")
        fig_heatmap = viz.plot_heatmap()
        if fig_heatmap:
            st.plotly_chart(fig_heatmap, use_container_width=True)

else:
    st.warning("데이터를 불러올 수 없습니다. CSV 파일 형식을 확인해 주세요.")
