import plotly.express as px

class DataVisualizer:
    def __init__(self, df):
        self.df = df
        # 전국 데이터는 합계이므로 시각화에서 제외하거나 별도로 처리
        if '시도별' in df.columns:
            self.df_filtered = df[df['시도별'] != '전국']
        else:
            self.df_filtered = df

    def plot_trend(self):
        """
        연도별 인구 변화 추세 (Line Chart)
        """
        if self.df_filtered.empty: return None

        fig = px.line(self.df_filtered, 
                      x='연도', 
                      y='인구수', 
                      color='시도별', 
                      title='연도별 시/도 인구 추이',
                      markers=True)
        fig.update_layout(xaxis_title="연도", yaxis_title="인구수 (명)")
        return fig

    def plot_bar_chart(self, year=None):
        """
        특정 연도의 시도별 인구 비교 (Bar Chart)
        """
        if self.df_filtered.empty: return None

        # 연도 기본값 설정 (가장 최신 연도)
        if year is None:
            year = self.df_filtered['연도'].max()

        data_year = self.df_filtered[self.df_filtered['연도'] == year]
        
        # 인구 많은 순으로 정렬
        data_year = data_year.sort_values(by='인구수', ascending=False)

        fig = px.bar(data_year, 
                     x='시도별', 
                     y='인구수', 
                     text='인구수',
                     color='인구수',
                     color_continuous_scale='Blues',
                     title=f'{year}년 시/도별 인구 비교')
        
        fig.update_layout(xaxis_title="시/도", yaxis_title="인구수 (명)")
        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        return fig
    
    def plot_heatmap(self):
        """
        연도 vs 시도 Heatmap
        """
        if self.df_filtered.empty: return None

        # Pivot: 행(시도), 열(연도), 값(인구)
        pivot_df = self.df_filtered.pivot(index='시도별', columns='연도', values='인구수')
        
        fig = px.imshow(pivot_df, 
                        labels=dict(x="연도", y="시도", color="인구수"),
                        x=pivot_df.columns,
                        y=pivot_df.index,
                        title="연도별 인구 분포 (Heatmap)",
                        color_continuous_scale='Viridis')
        return fig
