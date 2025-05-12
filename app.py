import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import requests
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class PharmaAIVisibilityAnalyzer:
    def __init__(self):
        # Sample pharmaceutical brands (you can expand this list)
        self.pharma_brands = [
            'Pfizer', 'Moderna', 'Johnson & Johnson', 
            'AstraZeneca', 'Novartis', 'Roche', 'Merck'
        ]
        
        # AI Platforms to analyze
        self.ai_platforms = [
            'ChatGPT', 'Microsoft Copilot', 
            'Perplexity', 'Claude', 'Google Gemini'
        ]
        
        # Placeholder for brand visibility data
        self.visibility_data = self.generate_sample_data()
    
    def generate_sample_data(self):
        """Generate sample data for visualization"""
        data = []
        for brand in self.pharma_brands:
            for platform in self.ai_platforms:
                # Simulating visibility metrics
                visibility_score = np.random.uniform(20, 80)
                sentiment_score = np.random.uniform(-1, 1)
                engagement_rate = np.random.uniform(0.1, 5.0)
                
                data.append({
                    'Brand': brand,
                    'Platform': platform,
                    'Visibility Score': round(visibility_score, 2),
                    'Sentiment Score': round(sentiment_score, 2),
                    'Engagement Rate': round(engagement_rate, 2)
                })
        
        return pd.DataFrame(data)
    
    def visualize_brand_visibility(self):
        """Create visualizations for brand visibility"""
        # Visibility Heatmap
        fig1 = px.density_heatmap(
            self.visibility_data, 
            x='Platform', 
            y='Brand', 
            z='Visibility Score',
            title='Pharma Brand Visibility Across AI Platforms',
            labels={'Visibility Score': 'Visibility %'}
        )
        
        # Sentiment Analysis
        fig2 = px.bar(
            self.visibility_data, 
            x='Brand', 
            y='Sentiment Score', 
            color='Platform',
            title='Brand Sentiment Across AI Platforms',
            labels={'Sentiment Score': 'Sentiment (-1 to 1)'}
        )
        
        # Engagement Rates
        fig3 = px.scatter(
            self.visibility_data, 
            x='Visibility Score', 
            y='Engagement Rate',
            color='Brand',
            size='Visibility Score',
            title='Visibility vs Engagement Rate',
            labels={
                'Visibility Score': 'Visibility %', 
                'Engagement Rate': 'Engagement Rate (%)'
            }
        )
        
        return fig1, fig2, fig3

def main():
    st.set_page_config(
        page_title="Pharma AI Visibility Analyzer", 
        page_icon="💊",
        layout="wide"
    )
    
    # App Title
    st.title("🧬 Pharma AI Visibility Dashboard")
    st.write("Analyze your pharmaceutical brand's presence in AI-powered search platforms")
    
    # Initialize Analyzer
    analyzer = PharmaAIVisibilityAnalyzer()
    
    # Display Raw Data
    if st.checkbox("Show Raw Visibility Data"):
        st.dataframe(analyzer.visibility_data)
    
    # Visualizations
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.plotly_chart(analyzer.visualize_brand_visibility()[0], use_container_width=True)
    
    with col2:
        st.plotly_chart(analyzer.visualize_brand_visibility()[1], use_container_width=True)
    
    with col3:
        st.plotly_chart(analyzer.visualize_brand_visibility()[2], use_container_width=True)
    
    # Insights Section
    st.header("Key Insights")
    top_brand = analyzer.visibility_data.groupby('Brand')['Visibility Score'].mean().idxmax()
    top_platform = analyzer.visibility_data.groupby('Platform')['Visibility Score'].mean().idxmax()
    
    st.write(f"🏆 Top Performing Brand: {top_brand}")
    st.write(f"🌐 Most Visibility Platform: {top_platform}")
    
    # Methodology Note
    st.info("""
    ### Methodology
    - **Visibility Score**: Frequency and prominence of brand mentions
    - **Sentiment Score**: Quality and context of brand mentions (-1 to 1)
    - **Engagement Rate**: Potential interaction and impact of AI mentions
    
    Note: This is a simulated dataset. Real-world data requires 
    advanced AI monitoring tools and APIs.
    """)

if __name__ == "__main__":
    main()
