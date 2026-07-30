import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration with custom theme
st.set_page_config(
    page_title="FIFA World Cup Player Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Metric cards styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .metric-label {
        font-size: 1em;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.8em;
        font-weight: bold;
        margin: 20px 0;
    }
    
    /* Player search styling */
    .player-search {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 30px;
        border-radius: 15px;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("fifa_worldcup_players.csv")
    # Add derived metrics for better analytics
    df['Goal_Per_90'] = (df['Goals'] / (df['Minutes_Played'] / 90)).round(2)
    df['Assist_Per_90'] = (df['Assists'] / (df['Minutes_Played'] / 90)).round(2)
    df['Goal_Contribution'] = df['Goals'] + df['Assists']
    return df

df = load_data()

# Header section with animation
st.markdown("""
<div style="text-align: center; padding: 30px 0;">
    <h1 style="font-size: 3em; font-weight: bold; color: #2c3e50;">
        ⚽ FIFA World Cup Player Analytics
    </h1>
    <p style="font-size: 1.2em; color: #7f8c8d; margin-top: 10px;">
        🏆 Interactive Dashboard | Real-time Analytics | Player Insights
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    st.markdown("## 🎮 Dashboard Controls")
    st.markdown("---")
    
    # Team filter with select all option
    st.markdown("### 🌍 Teams")
    teams = sorted(df["Team"].unique())
    col1, col2 = st.columns([3, 1])
    with col1:
        selected_teams = st.multiselect(
            "Select Teams",
            options=teams,
            default=teams[:5],
            key="team_select"
        )
    with col2:
        if st.button("All", key="all_teams"):
            selected_teams = teams
    
    # Position filter with checkboxes
    st.markdown("### 📍 Positions")
    positions = sorted(df["Position"].unique())
    selected_positions = st.multiselect(
        "Select Positions",
        options=positions,
        default=positions,
        key="position_select"
    )
    
    # Age range with custom styling
    st.markdown("### 🎂 Age Range")
    selected_age = st.slider(
        "Select Age",
        min_value=int(df["Age"].min()),
        max_value=int(df["Age"].max()),
        value=(int(df["Age"].min()), int(df["Age"].max())),
        key="age_slider"
    )
    
    # Additional filters
    st.markdown("### 🎯 Performance Filters")
    min_goals = st.number_input("Minimum Goals", min_value=0, value=0)
    min_assists = st.number_input("Minimum Assists", min_value=0, value=0)
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")
    st.markdown(f"Total Players in Database: **{len(df)}**")
    st.markdown(f"Countries Represented: **{len(teams)}**")

# Apply filters
filtered_df = df[
    (df["Team"].isin(selected_teams)) &
    (df["Position"].isin(selected_positions)) &
    (df["Age"].between(selected_age[0], selected_age[1])) &
    (df["Goals"] >= min_goals) &
    (df["Assists"] >= min_assists)
]

# Main dashboard
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🏃 Player Stats", "📈 Team Analysis", "🔍 Deep Dive"])

with tab1:
    # Key metrics in styled cards
    st.markdown('<div class="section-header">Dashboard Overview</div>', unsafe_allow_html=True)
    
    total_players = len(filtered_df)
    total_goals = filtered_df["Goals"].sum()
    total_assists = filtered_df["Assists"].sum()
    average_age = round(filtered_df["Age"].mean(), 1)
    avg_goals_per_player = round(total_goals / total_players, 2) if total_players > 0 else 0
    best_player = filtered_df.loc[filtered_df['Goals'].idxmax()] if not filtered_df.empty and filtered_df['Goals'].max() > 0 else None
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <div class="metric-label">Total Players</div>
            <div class="metric-value">👤 {total_players}</div>
            <div class="metric-label">Active Players</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <div class="metric-label">Total Goals</div>
            <div class="metric-value">⚽ {total_goals}</div>
            <div class="metric-label">Team Goals</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <div class="metric-label">Total Assists</div>
            <div class="metric-value">🎯 {total_assists}</div>
            <div class="metric-label">Team Assists</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <div class="metric-label">Avg Age</div>
            <div class="metric-value">🎂 {average_age}</div>
            <div class="metric-label">Years</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);">
            <div class="metric-label">Goals/Player</div>
            <div class="metric-value">⚡ {avg_goals_per_player}</div>
            <div class="metric-label">Average</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Top performers section
    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("### 🏆 Top 10 Goal Scorers")
        if not filtered_df.empty:
            top_goals = filtered_df.nlargest(10, "Goals").sort_values("Goals", ascending=True)
            fig = go.Figure(data=[
                go.Bar(
                    x=top_goals["Goals"],
                    y=top_goals["Player_Name"],
                    orientation='h',
                    marker=dict(
                        color=top_goals["Goals"],
                        colorscale='Viridis',
                        showscale=True,
                        colorbar=dict(title="Goals")
                    ),
                    text=top_goals["Goals"],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Goals: %{x}<extra></extra>'
                )
            ])
            fig.update_layout(
                height=400,
                margin=dict(l=0, r=0, t=30, b=0),
                xaxis_title="Goals Scored",
                yaxis_title="",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#2c3e50')
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col_right:
        st.markdown("### 🎯 Top 10 Assist Providers")
        if not filtered_df.empty:
            top_assists = filtered_df.nlargest(10, "Assists").sort_values("Assists", ascending=True)
            fig = go.Figure(data=[
                go.Bar(
                    x=top_assists["Assists"],
                    y=top_assists["Player_Name"],
                    orientation='h',
                    marker=dict(
                        color=top_assists["Assists"],
                        colorscale='Plasma',
                        showscale=True,
                        colorbar=dict(title="Assists")
                    ),
                    text=top_assists["Assists"],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Assists: %{x}<extra></extra>'
                )
            ])
            fig.update_layout(
                height=400,
                margin=dict(l=0, r=0, t=30, b=0),
                xaxis_title="Assists Provided",
                yaxis_title="",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#2c3e50')
            )
            st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown('<div class="section-header">Player Performance Analysis</div>', unsafe_allow_html=True)
    
    # Player search with autocomplete
    col_search, col_sort = st.columns([3, 1])
    with col_search:
        player_search = st.text_input("🔍 Search Player by Name", placeholder="Type player name...")
    with col_sort:
        sort_by = st.selectbox("Sort by", ["Goals", "Assists", "Minutes_Played", "Goal_Per_90", "Goal_Contribution"])
    
    if player_search:
        search_results = filtered_df[filtered_df["Player_Name"].str.contains(player_search, case=False)]
        if not search_results.empty:
            # Player card
            for idx, player in search_results.iterrows():
                with st.container():
                    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                    with col1:
                        st.markdown(f"### {player['Player_Name']}")
                        st.markdown(f"**Team:** {player['Team']} | **Position:** {player['Position']} | **Age:** {player['Age']}")
                    with col2:
                        st.metric("Goals", player['Goals'], delta=f"{player['Goal_Per_90']}/90min")
                    with col3:
                        st.metric("Assists", player['Assists'], delta=f"{player['Assist_Per_90']}/90min")
                    with col4:
                        st.metric("Minutes", player['Minutes_Played'], delta=f"G+A: {player['Goal_Contribution']}")
                    st.divider()
    
    # Goals vs Assists scatter plot
    st.markdown("### 📈 Performance Matrix: Goals vs Assists")
    if not filtered_df.empty:
        fig = px.scatter(
            filtered_df,
            x="Goals",
            y="Assists",
            size="Minutes_Played",
            color="Position",
            hover_name="Player_Name",
            hover_data=["Team", "Age", "Goal_Per_90"],
            size_max=50,
            title="Player Performance Distribution",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0.02)',
            xaxis=dict(gridcolor='rgba(0,0,0,0.1)'),
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)')
        )
        # Add quadrant lines
        fig.add_hline(y=filtered_df['Assists'].median(), line_dash="dash", line_color="gray", opacity=0.5)
        fig.add_vline(x=filtered_df['Goals'].median(), line_dash="dash", line_color="gray", opacity=0.5)
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown('<div class="section-header">Team Performance Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Team goals ranking
        team_goals = filtered_df.groupby("Team")["Goals"].sum().sort_values(ascending=True).tail(15)
        if not team_goals.empty:
            fig = go.Figure(data=[
                go.Bar(
                    x=team_goals.values,
                    y=team_goals.index,
                    orientation='h',
                    marker=dict(
                        color=team_goals.values,
                        colorscale='RdYlGn',
                        showscale=True,
                        colorbar=dict(title="Goals")
                    ),
                    text=team_goals.values,
                    textposition='outside'
                )
            ])
            fig.update_layout(
                title="Top Teams by Total Goals",
                height=500,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Position distribution by team
        team_position = pd.crosstab(filtered_df['Team'], filtered_df['Position'])
        fig = px.imshow(
            team_position,
            title="Team Composition Matrix",
            color_continuous_scale='Blues',
            aspect="auto"
        )
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # Age distribution by position
    st.markdown("### 🎂 Age Distribution by Position")
    if not filtered_df.empty:
        fig = px.box(
            filtered_df,
            x="Position",
            y="Age",
            color="Position",
            title="Age Distribution Across Positions",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(
            height=400,
            showlegend=False,
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.markdown('<div class="section-header">Deep Dive Analytics</div>', unsafe_allow_html=True)
    
    # Statistical summary
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Statistical Summary")
        stats_df = filtered_df[['Goals', 'Assists', 'Minutes_Played', 'Age', 'Goal_Per_90']].describe()
        st.dataframe(stats_df.style.highlight_max(axis=0, color='lightgreen')
                    .highlight_min(axis=0, color='lightcoral'), use_container_width=True)
    
    with col2:
        st.markdown("### 🏆 Top Performers (Goals + Assists)")
        top_contributors = filtered_df.nlargest(10, 'Goal_Contribution')[['Player_Name', 'Team', 'Goals', 'Assists', 'Goal_Contribution']]
        fig = go.Figure(data=[
            go.Bar(name='Goals', x=top_contributors['Player_Name'], y=top_contributors['Goals'], marker_color='#667eea'),
            go.Bar(name='Assists', x=top_contributors['Player_Name'], y=top_contributors['Assists'], marker_color='#764ba2')
        ])
        fig.update_layout(
            barmode='stack',
            title="Goal Contributions Breakdown",
            height=400,
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Correlation heatmap
    st.markdown("### 🔥 Performance Correlations")
    numeric_cols = ['Goals', 'Assists', 'Minutes_Played', 'Age', 'Goal_Per_90', 'Assist_Per_90']
    correlation_matrix = filtered_df[numeric_cols].corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='RdBu',
        zmid=0,
        text=np.round(correlation_matrix.values, 2),
        texttemplate='%{text}',
        textfont={"size": 10},
        hoverongaps=False
    ))
    fig.update_layout(
        title="Correlation Matrix of Performance Metrics",
        height=500,
        width=700
    )
    st.plotly_chart(fig, use_container_width=True)

# Footer with download option
st.markdown("---")
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    st.markdown("### 📋 Filtered Dataset")
    st.dataframe(
        filtered_df.style.background_gradient(subset=['Goals', 'Assists'], cmap='YlOrRd'),
        use_container_width=True,
        height=300
    )
    st.caption(f"Showing **{len(filtered_df)}** players | {total_players} of {len(df)} total players")
with col2:
    st.markdown("### 📥 Export Data")
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name='world_cup_analytics.csv',
        mime='text/csv',
        use_container_width=True
    )
with col3:
    st.markdown("### 🎮 Quick Actions")
    if st.button("Reset All Filters", use_container_width=True):
        st.rerun()

# Final summary
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    border-radius: 10px; color: white;">
        <h3>🏆 FIFA World Cup Analytics Dashboard</h3>
        <p>Built with ❤️ using Streamlit, Plotly & Pandas | Interactive Data Visualization</p>
        <p style="font-size: 0.8em; opacity: 0.8;">© 2024 Portfolio Project | Data-Driven Football Analytics</p>
    </div>
    """,
    unsafe_allow_html=True
)