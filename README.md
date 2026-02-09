# KOSIS 통계 대시보드 (KOSIS Statistics Dashboard)

이 프로젝트는 KOSIS(국가통계포털) 데이터를 활용하여 통계 데이터를 시각적으로 분석할 수 있는 Streamlit 기반 웹 애플리케이션임.
사용자는 CSV 파일을 업로드하거나 기본 제공되는 예제 데이터를 사용하여 데이터의 추세, 비교, 분포를 인터랙티브하게 확인할 수 있음.

## 📌 주요 기능

1. **데이터 로드 및 선택**
   - 사용자 지정 CSV 파일 업로드 기능 (`file_uploader`) 제공
   - 업로드 파일이 없을 경우 기본 예제 데이터(`data/kosis_population_sample.csv`) 자동 로드

2. **데이터 탐색적 분석 (EDA)**
   - 전체 데이터 행 수, 분석 기간(연도 범위), 지역 수, 평균 값 등의 핵심 지표 요약
   - 원본 데이터 미리보기 제공 (`dataframe`)

3. **다양한 시각화 (Plotly 연동)**
   - **📈 연도별 추세**: 시간의 흐름에 따른 데이터 변화를 꺾은선 그래프로 시각화
   - **📊 지역별 비교**: 특정 연도를 선택하여 지역 간 데이터를 비교하는 막대 그래프 제공
   - **🗺️ 히트맵 분포**: 데이터의 전체적인 밀집도와 패턴을 색상으로 표현

## 📂 프로젝트 구조

```bash
KOSIS_Dashboard/
├── app.py                  # 메인 애플리케이션 실행 파일
├── data/                   # 데이터 파일 디렉토리
│   └── kosis_population_sample.csv  # 기본 제공 예제 데이터
└── modules/                # 기능별 모듈 분리
    ├── data_loader.py      # 데이터 로드 및 전처리 함수 (load_data, get_basic_stats)
    └── plot_utils.py       # 시각화 관련 클래스 (DataVisualizer)
```

## 🚀 실행 방법

필요한 라이브러리가 설치된 환경에서 아래 명령어를 실행.

```bash
streamlit run app.py
```

## 📦 필요 라이브러리

- `streamlit`: 웹 애플리케이션 프레임워크
- `pandas`: 데이터 처리 및 분석
- `plotly`: 인터랙티브 차트 생성
- `os`: 파일 경로 처리 (표준 라이브러리)

