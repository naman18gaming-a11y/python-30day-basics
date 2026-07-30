import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page configuration
st.set_page_config(
    page_title="FIFA World Cup Player Analytics",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI
st.markdown("""
<style>
    /* Gradient metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 10px 0;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }
    
    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        margin: 10px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .metric-label {
        font-size: 0.9em;
        opacity: 0.95;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 500;
    }
    
    /* Section styling */
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2em;
        font-weight: bold;
        margin: 20px 0;
        padding: 10px 0;
    }
    
    /* Player card */
    .player-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
        border-left: 5px solid #667eea;
    }
    
    /* Stats badge */
    .stat-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        font-weight: bold;
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the FIFA World Cup dataset"""
    df = pd.read_csv("fifa_worldcup_players.csv")
    
    # Add derived metrics
    df['Goal_Contribution'] = df['Goals'] + df['Assists']
    df['Goals_Per_90'] = (df['Goals'] / (df['Minutes_Played'] / 90)).round(2)
    df['Assists_Per_90'] = (df['Assists'] / (df['Minutes_Played'] / 90)).round(2)
    df['Efficiency'] = ((df['Goals'] + df['Assists']) / (df['Minutes_Played'] / 90)).round(3)
    
    return df

# Load data
try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ 'fifa_worldcup_players.csv' not found! Please make sure the file is in the same directory.")
    st.stop()

# Animated header
st.markdown("""
<div style="text-align: center; padding: 30px 0; animation: fadeIn 1s ease-in;">
    <h1 style="font-size: 3.5em; font-weight: bold; color: #2c3e50; margin-bottom: 10px;">
        ⚽ FIFA World Cup Analytics
    </h1>
    <p style="font-size: 1.3em; color: #7f8c8d; margin-top: 0;">
        🏆 Interactive Player Performance Dashboard
    </p>
    <p style="color: #95a5a6; font-size: 0.9em;">
        Powered by Streamlit, Plotly & Pandas
    </p>
</div>
""", unsafe_allow_html=True)

# Enhanced Sidebar
with st.sidebar:
    st.markdown("## 🎮 Dashboard Controls")
    st.markdown("---")
    
    # Team Selection
    st.markdown("### 🌍 Team Selection")
    teams = sorted(df["Team"].unique())
    
    # Quick select buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("All", use_container_width=True, key="all_btn"):
            st.session_state.selected_teams = teams
    with col2:
        if st.button("Top 10", use_container_width=True, key="top10_btn"):
            top_teams = df.groupby("Team")["Goals"].sum().nlargest(10).index.tolist()
            st.session_state.selected_teams = top_teams
    with col3:
        if st.button("Clear", use_container_width=True, key="clear_btn"):
            st.session_state.selected_teams = []
    
    if 'selected_teams' not in st.session_state:
        st.session_state.selected_teams = teams[:5]
    
    selected_teams = st.multiselect(
        "Choose Teams",
        options=teams,
        default=st.session_state.selected_teams,
        key="team_multiselect"
    )
    
    # Position Filter
    st.markdown("### 📍 Position Filter")
    positions = sorted(df["Position"].unique())
    selected_positions = st.multiselect(
        "Choose Positions",
        options=positions,
        default=positions,
        key="position_multiselect"
    )
    
    # Age Range
    st.markdown("### 🎂 Age Range")
    selected_age = st.slider(
        "Select Age Bracket",
        min_value=int(df["Age"].min()),
        max_value=int(df["Age"].max()),
        value=(int(df["Age"].min()), int(df["Age"].max())),
        key="age_slider"
    )
    
    # Advanced Filters
    st.markdown("### ⚡ Performance Filters")
    min_goals = st.number_input("Minimum Goals Scored", min_value=0, value=0)
    min_assists = st.number_input("Minimum Assists", min_value=0, value=0)
    min_minutes = st.number_input("Minimum Minutes Played", min_value=0, value=0)
    
    st.markdown("---")
    
    # Database Stats
    st.markdown("### 📊 Database Stats")
    col1, col2 = st.columns(2)
    col1.metric("Total Players", len(df))
    col2.metric("Countries", len(teams))
    
    # Progress indicator
    st.markdown("### 🎯 Goal Achievement")
    total_goals_all = df["Goals"].sum()
    st.progress(min(total_goals_all / 2000, 1.0), text=f"Total Goals: {total_goals_all}")

# Apply filters
filtered_df = df[
    (df["Team"].isin(selected_teams)) &
    (df["Position"].isin(selected_positions)) &
    (df["Age"].between(selected_age[0], selected_age[1])) &
    (df["Goals"] >= min_goals) &
    (df["Assists"] >= min_assists) &
    (df["Minutes_Played"] >= min_minutes)
]

# Main Dashboard with Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", 
    "⚽ Player Analysis", 
    "🏆 Team Analysis", 
    "📈 Advanced Metrics",
    "📋 Data Explorer"
])

# Tab 1: Overview
with tab1:
    st.markdown('<div class="section-header">Dashboard Overview</div>', unsafe_allow_html=True)
    
    # Key Metrics
    total_players = len(filtered_df)
    total_goals = filtered_df["Goals"].sum()
    total_assists = filtered_df["Assists"].sum()
    average_age = round(filtered_df["Age"].mean(), 1)
    avg_goals = round(total_goals / total_players, 2) if total_players > 0 else 0
    best_scorer = filtered_df.loc[filtered_df['Goals'].idxmax()] if not filtered_df.empty else None
    
    # Metric Cards in 2 rows
    st.markdown("### 📈 Key Performance Indicators")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #667eea, #764ba2);">
            <div class="metric-label">👤 Active Players</div>
            <div class="metric-value">{total_players}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #f093fb, #f5576c);">
            <div class="metric-label">⚽ Total Goals</div>
            <div class="metric-value">{total_goals}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #4facfe, #00f2fe);">
            <div class="metric-label">🎯 Total Assists</div>
            <div class="metric-value">{total_assists}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #43e97b, #38f9d7);">
            <div class="metric-label">🎂 Avg Age</div>
            <div class="metric-value">{average_age}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #fa709a, #fee140);">
            <div class="metric-label">⚡ Goals/Player</div>
            <div class="metric-value">{avg_goals}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Top Performer Highlight
    if best_scorer is not None:
        st.markdown("---")
        st.markdown("### 🌟 Best Performer")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"""
            <div class="player-card" style="text-align: center;">
                <h2>🏆 {best_scorer['Player_Name']}</h2>
                <p style="font-size: 1.2em;">
                    <span class="stat-badge">⚽ {best_scorer['Goals']} Goals</span>
                    <span class="stat-badge">🎯 {best_scorer['Assists']} Assists</span>
                    <span class="stat-badge">⏱️ {best_scorer['Minutes_Played']} min</span>
                </p>
                <p>Team: <b>{best_scorer['Team']}</b> | Position: <b>{best_scorer['Position']}</b> | Age: <b>{best_scorer['Age']}</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Charts Row 1
    st.markdown("---")
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🏆 Top 10 Goal Scorers")
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
                        colorbar=dict(title="Goals", thickness=15)
                    ),
                    text=top_goals["Goals"],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Goals: %{x}<br>Team: %{customdata}<extra></extra>',
                    customdata=top_goals["Team"]
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
        else:
            st.info("No data to display with current filters")
    
    with col_right:
        st.subheader("🎯 Top 10 Assist Providers")
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
                        colorbar=dict(title="Assists", thickness=15)
                    ),
                    text=top_assists["Assists"],
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Assists: %{x}<br>Team: %{customdata}<extra></extra>',
                    customdata=top_assists["Team"]
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
        else:
            st.info("No data to display with current filters")

# Tab 2: Player Analysis
with tab2:
    st.markdown('<div class="section-header">Player Performance Analysis</div>', unsafe_allow_html=True)
    
    # Player Search
    col1, col2 = st.columns([3, 1])
    with col1:
        player_search = st.text_input(
            "🔍 Search Player by Name",
            placeholder="Type player name (e.g., Messi, Ronaldo)...",
            key="player_search"
        )
    with col2:
        sort_by = st.selectbox(
            "Sort by",
            ["Goals", "Assists", "Goal_Contribution", "Minutes_Played", "Goals_Per_90", "Efficiency"],
            key="sort_players"
        )
    
    if player_search:
        search_results = filtered_df[filtered_df["Player_Name"].str.contains(player_search, case=False)]
        
        if not search_results.empty:
            st.success(f"Found {len(search_results)} player(s) matching '{player_search}'")
            
            for idx, player in search_results.iterrows():
                with st.expander(f"⭐ {player['Player_Name']} - {player['Team']} ({player['Position']})", expanded=True):
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(
                            "Goals",
                            player['Goals'],
                            delta=f"{player['Goals_Per_90']} per 90min",
                            delta_color="normal"
                        )
                    
                    with col2:
                        st.metric(
                            "Assists",
                            player['Assists'],
                            delta=f"{player['Assists_Per_90']} per 90min",
                            delta_color="normal"
                        )
                    
                    with col3:
                        st.metric(
                            "Minutes Played",
                            player['Minutes_Played'],
                            delta=f"G+A: {player['Goal_Contribution']}"
                        )
                    
                    with col4:
                        efficiency_color = "normal" if player['Efficiency'] > 0.5 else "off"
                        st.metric(
                            "Efficiency",
                            f"{player['Efficiency']:.2f}",
                            delta="G+A per 90min",
                            delta_color=efficiency_color
                        )
                    
                    # Progress bars for visual representation
                    st.markdown(f"**Goal Contribution Rate**")
                    st.progress(
                        min(player['Goal_Contribution'] / 20, 1.0),
                        text=f"{player['Goal_Contribution']} total contributions"
                    )
        else:
            st.warning(f"No players found matching '{player_search}'")
    
    # Performance Scatter Plot
    st.markdown("---")
    st.subheader("📈 Performance Matrix: Goals vs Assists")
    
    if not filtered_df.empty:
        fig = px.scatter(
            filtered_df,
            x="Goals",
            y="Assists",
            color="Position",
            size="Minutes_Played",
            hover_name="Player_Name",
            hover_data={
                "Team": True,
                "Age": True,
                "Goal_Contribution": True,
                "Efficiency": ':.2f',
                "Goals_Per_90": ':.2f'
            },
            size_max=55,
            color_discrete_sequence=px.colors.qualitative.Set2,
            title="Player Performance Distribution"
        )
        
        # Add reference lines
        median_goals = filtered_df['Goals'].median()
        median_assists = filtered_df['Assists'].median()
        
        fig.add_hline(
            y=median_assists,
            line_dash="dash",
            line_color="gray",
            opacity=0.5,
            annotation_text=f"Median Assists: {median_assists}",
            annotation_position="top right"
        )
        
        fig.add_vline(
            x=median_goals,
            line_dash="dash",
            line_color="gray",
            opacity=0.5,
            annotation_text=f"Median Goals: {median_goals}",
            annotation_position="top right"
        )
        
        fig.update_layout(
            height=600,
            plot_bgcolor='rgba(0,0,0,0.02)',
            paper_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(gridcolor='rgba(0,0,0,0.1)', title="Goals Scored"),
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)', title="Assists Provided"),
            hovermode='closest'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data to display with current filters")

# Tab 3: Team Analysis
with tab3:
    st.markdown('<div class="section-header">Team Performance Analysis</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏆 Teams by Total Goals")
        if not filtered_df.empty:
            team_goals = filtered_df.groupby("Team")["Goals"].sum().sort_values(ascending=True).tail(15)
            
            fig = go.Figure(data=[
                go.Bar(
                    x=team_goals.values,
                    y=team_goals.index,
                    orientation='h',
                    marker=dict(
                        color=team_goals.values,
                        colorscale='RdYlGn',
                        showscale=True,
                        colorbar=dict(title="Total Goals", thickness=15)
                    ),
                    text=team_goals.values,
                    textposition='outside',
                    hovertemplate='<b>%{y}</b><br>Total Goals: %{x}<extra></extra>'
                )
            ])
            
            fig.update_layout(
                height=500,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                xaxis_title="Total Goals",
                yaxis_title=""
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data to display")
    
    with col2:
        st.subheader("📊 Team Composition Matrix")
        if not filtered_df.empty:
            team_position = pd.crosstab(filtered_df['Team'], filtered_df['Position'])
            
            fig = px.imshow(
                team_position,
                title="Position Distribution by Team",
                color_continuous_scale='Blues',
                aspect="auto",
                labels=dict(x="Position", y="Team", color="Players")
            )
            
            fig.update_layout(
                height=500,
                xaxis_tickangle=-45
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data to display")
    
    st.markdown("---")
    
    # Team Statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Team Statistics")
        if not filtered_df.empty:
            team_stats = filtered_df.groupby("Team").agg({
                'Goals': 'sum',
                'Assists': 'sum',
                'Minutes_Played': 'mean',
                'Age': 'mean',
                'Efficiency': 'mean'
            }).round(2)
            
            team_stats.columns = ['Total Goals', 'Total Assists', 'Avg Minutes', 'Avg Age', 'Avg Efficiency']
            st.dataframe(
                team_stats.sort_values('Total Goals', ascending=False),
                use_container_width=True,
                height=400
            )
        else:
            st.info("No data to display")
    
    with col2:
        st.subheader("🎂 Age Distribution by Position")
        if not filtered_df.empty:
            fig = px.box(
                filtered_df,
                x="Position",
                y="Age",
                color="Position",
                title="Age Distribution Across Positions",
                color_discrete_sequence=px.colors.qualitative.Pastel,
                points="all",
                hover_data=['Player_Name', 'Team']
            )
            
            fig.update_layout(
                height=400,
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data to display")

# Tab 4: Advanced Metrics
with tab4:
    st.markdown('<div class="section-header">Advanced Performance Metrics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Statistical Summary")
        if not filtered_df.empty:
            stats_df = filtered_df[['Goals', 'Assists', 'Minutes_Played', 'Age', 'Goals_Per_90', 'Efficiency']].describe()
            
            # Style the dataframe
            styled_stats = stats_df.style.background_gradient(
                subset=['Goals', 'Assists', 'Efficiency'],
                cmap='YlOrRd'
            ).format("{:.2f}")
            
            st.dataframe(styled_stats, use_container_width=True, height=300)
        else:
            st.info("No data to display")
    
    with col2:
        st.subheader("🔥 Performance Correlations")
        if not filtered_df.empty:
            numeric_cols = ['Goals', 'Assists', 'Minutes_Played', 'Age', 'Goals_Per_90', 'Efficiency']
            corr_matrix = filtered_df[numeric_cols].corr()
            
            fig = go.Figure(data=go.Heatmap(
                z=corr_matrix.values,
                x=corr_matrix.columns,
                y=corr_matrix.columns,
                colorscale='RdBu',
                zmid=0,
                text=np.round(corr_matrix.values, 2),
                texttemplate='%{text}',
                textfont={"size": 10},
                hoverongaps=False,
                colorbar=dict(title="Correlation")
            ))
            
            fig.update_layout(
                title="Correlation Matrix of Performance Metrics",
                height=450,
                width=700
            )
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data to display")
    
    st.markdown("---")
    
    # Top Contributors
    st.subheader("🏆 Top Contributors (Goals + Assists)")
    if not filtered_df.empty:
        top_contributors = filtered_df.nlargest(15, 'Goal_Contribution')[
            ['Player_Name', 'Team', 'Position', 'Goals', 'Assists', 'Goal_Contribution', 'Efficiency']
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Goals',
            x=top_contributors['Player_Name'],
            y=top_contributors['Goals'],
            marker_color='#667eea',
            text=top_contributors['Goals'],
            textposition='auto'
        ))
        
        fig.add_trace(go.Bar(
            name='Assists',
            x=top_contributors['Player_Name'],
            y=top_contributors['Assists'],
            marker_color='#764ba2',
            text=top_contributors['Assists'],
            textposition='auto'
        ))
        
        fig.update_layout(
            barmode='stack',
            title="Goal Contributions Breakdown (Top 15 Players)",
            height=500,
            xaxis_tickangle=-45,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data to display")

# Tab 5: Data Explorer
with tab5:
    st.markdown('<div class="section-header">Data Explorer</div>', unsafe_allow_html=True)
    
    # Column selector
    col1, col2 = st.columns([2, 1])
    
    with col1:
        display_columns = st.multiselect(
            "Select columns to display",
            options=filtered_df.columns.tolist(),
            default=['Player_Name', 'Team', 'Position', 'Goals', 'Assists', 'Minutes_Played', 'Age'],
            key="display_columns"
        )
    
    with col2:
        st.download_button(
            label="📥 Download Filtered Data",
            data=filtered_df.to_csv(index=False),
            file_name='fifa_worldcup_filtered_data.csv',
            mime='text/csv',
            use_container_width=True
        )
    
    if display_columns:
        st.dataframe(
            filtered_df[display_columns].style.background_gradient(
                subset=['Goals', 'Assists'],
                cmap='YlOrRd'
            ),
            use_container_width=True,
            height=500,
            hide_index=True
        )
    else:
        st.dataframe(filtered_df, use_container_width=True, height=500, hide_index=True)
    
    st.caption(f"📊 Showing **{len(filtered_df)}** players from **{filtered_df['Team'].nunique()}** teams")

# Footer
st.markdown("---")

# Final summary section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
    border-radius: 15px; color: white; margin: 20px 0;">
        <h3>🏆 FIFA World Cup Analytics Dashboard</h3>
        <p style="font-size: 1.1em;">Advanced Player Performance Analytics</p>
        <p style="font-size: 0.9em; opacity: 0.9;">
            Built with ❤️ using Streamlit {{ st.__version__ }} | Plotly | Pandas
        </p>
        <p style="font-size: 0.8em; opacity: 0.8;">© 2024 Portfolio Project</p>
    </div>
    """, unsafe_allow_html=True)

# Quick action buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔄 Reset All Filters", use_container_width=True):
        st.rerun()
with col2:
    if st.button("📊 Show All Players", use_container_width=True):
        st.session_state.selected_teams = teams
        st.rerun()
with col3:
    st.markdown(f"**Session Stats:** {len(filtered_df)} players filtered")
