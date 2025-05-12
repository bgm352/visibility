import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
from typing import List, Dict

class PharmaAIVisibilityAnalyzer:
    def __init__(self):
        # Comprehensive list of pharma brands with additional context
        self.pharma_brands = [
            {'name': 'Pfizer', 'specialty': 'Vaccines, Oncology', 'market_cap': 200},
            {'name': 'Moderna', 'specialty': 'mRNA Technologies', 'market_cap': 150},
            {'name': 'Johnson & Johnson', 'specialty': 'Diverse Healthcare', 'market_cap': 250},
            {'name': 'AstraZeneca', 'specialty': 'Oncology, Cardiovascular', 'market_cap': 180},
            {'name': 'Novartis', 'specialty': 'Innovative Medicines', 'market_cap': 220},
            {'name': 'Roche', 'specialty': 'Diagnostics, Oncology', 'market_cap': 210},
            {'name': 'Merck', 'specialty': 'Immunotherapy, Diabetes', 'market_cap': 190}
        ]
        
        # Enhanced AI Platforms with additional context
        self.ai_platforms = [
            {'name': 'ChatGPT', 'user_base': 100, 'accuracy_score': 0.85},
            {'name': 'Microsoft Copilot', 'user_base': 75, 'accuracy_score': 0.78},
            {'name': 'Perplexity', 'user_base': 50, 'accuracy_score': 0.82},
            {'name': 'Claude', 'user_base': 60, 'accuracy_score': 0.87},
            {'name': 'Google Gemini', 'user_base': 90, 'accuracy_score': 0.80}
        ]
        
        # Generate comprehensive visibility data
        self.visibility_data = self.generate_comprehensive_data()
    
    def generate_comprehensive_data(self) -> pd.DataFrame:
        """Generate advanced data simulation for pharma AI visibility"""
        data = []
        for brand in self.pharma_brands:
            for platform in self.ai_platforms:
                # Advanced metrics simulation
                visibility_score = np.random.uniform(20, 80)
                sentiment_score = np.random.uniform(-1, 1)
                engagement_rate = np.random.uniform(0.1, 5.0)
                
                # Industry-specific context metrics
                research_relevance = np.random.uniform(0.1, 1.0)
                clinical_mention_rate = np.random.uniform(0.1, 1.0)
                regulatory_compliance_score = np.random.uniform(0.5, 1.0)
                
                data.append({
                    'Brand': brand['name'],
                    'Brand Specialty': brand['specialty'],
                    'Market Cap ($B)': brand['market_cap'],
                    'Platform': platform['name'],
                    'Platform User Base (M)': platform['user_base'],
                    'Platform Accuracy': platform['accuracy_score'],
                    'Visibility Score': round(visibility_score, 2),
                    'Sentiment Score': round(sentiment_score, 2),
                    'Engagement Rate (%)': round(engagement_rate, 2),
                    'Research Relevance': round(research_relevance, 2),
                    'Clinical Mention Rate': round(clinical_mention_rate, 2),
                    'Regulatory Compliance': round(regulatory_compliance_score, 2)
                })
        
        return pd.DataFrame(data)
    
    def generate_strategic_insights(self) -> Dict[str, str]:
        """Generate strategic insights for decision-makers"""
        insights = {}
        
        # Brand Performance Insights
        brand_performance = self.visibility_data.groupby('Brand')[
            ['Visibility Score', 'Sentiment Score', 'Engagement Rate (%)']
        ].mean()
        top_brand = brand_performance['Visibility Score'].idxmax()
        insights['Top Performing Brand'] = f"{top_brand} leads in AI visibility metrics"
        
        # Platform Strategic Analysis
        platform_performance = self.visibility_data.groupby('Platform')[
            ['Visibility Score', 'Platform User Base (M)', 'Platform Accuracy']
        ].mean()
        top_platform = platform_performance['Visibility Score'].idxmax()
        insights['Strategic Platform'] = (
            f"{top_platform} offers the best combination of user base "
            f"and visibility for pharmaceutical brands"
        )
        
        # Regulatory and Research Insights
        research_relevance = self.visibility_data.groupby('Brand')[
            'Research Relevance'
        ].mean()
        top_research_brand = research_relevance.idxmax()
        insights['Research Leadership'] = (
            f"{top_research_brand} demonstrates highest research relevance "
            "in AI-driven knowledge platforms"
        )
        
        # Sentiment and Compliance Analysis
        sentiment_compliance = self.visibility_data.groupby('Brand')[
            ['Sentiment Score', 'Regulatory Compliance']
        ].mean()
        most_compliant_brand = sentiment_compliance['Regulatory Compliance'].idxmax()
        insights['Regulatory Compliance'] = (
            f"{most_compliant_brand} leads in regulatory compliance "
            "and positive brand sentiment"
        )
        
        return insights
    
    def visualize_advanced_metrics(self):
        """Create comprehensive visualizations for strategic analysis"""
        # Multi-dimensional Bubble Chart
        fig1 = px.scatter(
            self.visibility_data, 
            x='Visibility Score', 
            y='Engagement Rate (%)',
            size='Market Cap ($B)',
            color='Brand',
            hover_name='Brand',
            hover_data={
                'Platform': True,
                'Sentiment Score': ':.2f',
                'Research Relevance': ':.2f',
                'Regulatory Compliance': ':.2f'
            },
            title='Pharma Brand Performance Across AI Platforms',
            labels={
                'Visibility Score': 'AI Visibility',
                'Engagement Rate (%)': 'Engagement Rate',
                'Market Cap ($B)': 'Market Capitalization'
            }
        )
        
        # Compliance and Sentiment Radar Chart
        brands = self.visibility_data['Brand'].unique()
        compliance_data = self.visibility_data.groupby('Brand')[
            ['Sentiment Score', 'Regulatory Compliance', 'Research Relevance']
        ].mean().reset_index()
        
        fig2 = go.Figure()
        for brand in brands:
            brand_data = compliance_data[compliance_data['Brand'] == brand]
            fig2.add_trace(go.Scatterpolar(
                r=brand_data[['Sentiment Score', 'Regulatory Compliance', 'Research Relevance']].values[0],
                theta=['Sentiment', 'Regulatory Compliance', 'Research Relevance'],
                fill='toself',
                name=brand
            ))
        
        fig2.update_layout(
            title='Brand Strategic Performance Radar',
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=True
        )
        
        # Platform Comparative Analysis
        platform_metrics = self.visibility_data.groupby('Platform')[
            ['Visibility Score', 'Platform User Base (M)', 'Platform Accuracy']
        ].mean().reset_index()
        
        fig3 = go.Figure(data=[
            go.Bar(name='Visibility Score', x=platform_metrics['Platform'], y=platform_metrics['Visibility Score']),
            go.Bar(name='User Base (Millions)', x=platform_metrics['Platform'], y=platform_metrics['Platform User Base (M)']),
            go.Bar(name='Accuracy Score', x=platform_metrics['Platform'], y=platform_metrics['Platform Accuracy'])
        ])
        fig3.update_layout(
            title='AI Platform Comparative Analysis',
            xaxis_title='Platforms',
            yaxis_title='Normalized Metrics',
            barmode='group'
        )
        
        return fig1, fig2, fig3

def main():
    st.set_page_config(
        page_title="Pharma AI Visibility Intelligence", 
        page_icon="💊",
        layout="wide"
    )
    
    # Advanced Branding
    st.markdown("""
    # 🧬 Pharmaceutical AI Visibility Intelligence
    ## Strategic Insights for Market Leadership
    """)
    
    # Initialize Advanced Analyzer
    analyzer = PharmaAIVisibilityAnalyzer()
    
    # Strategic Insights Section
    st.header("🔍 Strategic Insights")
    insights = analyzer.generate_strategic_insights()
    for title, insight in insights.items():
        st.markdown(f"### {title}")
        st.write(insight)
    
    # Visualization Columns
    st.header("🌐 Comprehensive Performance Metrics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.plotly_chart(analyzer.visualize_advanced_metrics()[0], use_container_width=True)
    
    with col2:
        st.plotly_chart(analyzer.visualize_advanced_metrics()[1], use_container_width=True)
    
    with col3:
        st.plotly_chart(analyzer.visualize_advanced_metrics()[2], use_container_width=True)
    
    # Advanced Data Exploration
    if st.checkbox("Explore Detailed Dataset"):
        st.dataframe(analyzer.visibility_data)
    
    # Value Proposition Section
    st.markdown("""
    ## 💡 Why AI Visibility Matters
    
    ### For Pharmaceutical Decision Makers
    - **Strategic Positioning**: Understand your brand's AI presence
    - **Competitive Intelligence**: Track industry visibility trends
    - **Research Impact**: Measure knowledge dissemination
    - **Regulatory Insights**: Monitor compliance and sentiment
    
    ### Methodology
    - Advanced multi-platform AI visibility tracking
    - Comprehensive performance metrics
    - Machine learning-driven insights
    """)
    
    # Call to Action
    st.markdown("""
    ### Ready to Elevate Your Brand's AI Strategy?
    [Request a Personalized Consultation](#)
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
