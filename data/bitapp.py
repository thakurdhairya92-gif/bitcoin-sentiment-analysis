import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Crypto Sentiment Dashboard",
    page_icon="📈",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

h1, h2, h3 {
    color: white;
}

[data-testid="stMetric"] {
    background-color: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 15px;
}

.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    fg_df = pd.read_csv("data/fear_greed.csv")
    hist_df = pd.read_csv("data/historical_data.csv")
    # Convert date column safely
    if "date" in fg_df.columns:
        fg_df["date"] = pd.to_datetime(fg_df["date"])

    return fg_df, hist_df

fg_df, hist_df = load_data()

# =========================
# HEADER
# =========================
st.markdown("""
<div style='text-align:center'>
    <h1>🚀 Crypto Market Sentiment Dashboard</h1>
    <p style='font-size:20px;color:lightgray;'>
        Fear & Greed Analysis + Trading Insights
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚙️ Filters")

if "classification" in fg_df.columns:
    sentiments = fg_df["classification"].unique()

    selected = st.sidebar.multiselect(
        "Select Sentiment",
        sentiments,
        default=sentiments
    )

    filtered_fg = fg_df[fg_df["classification"].isin(selected)]

else:
    filtered_fg = fg_df

# =========================
# METRICS
# =========================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📅 Total Records", len(fg_df))

with col2:
    if "classification" in fg_df.columns:
        fear_days = len(
            fg_df[
                fg_df["classification"]
                .astype(str)
                .str.contains("Fear", case=False)
            ]
        )
        st.metric("😨 Fear Days", fear_days)

with col3:
    if "Closed PnL" in hist_df.columns:
        total_pnl = hist_df["Closed PnL"].sum()
        st.metric("💰 Total PnL", f"${total_pnl:,.2f}")

with col4:
    st.metric("📊 Total Trades", len(hist_df))

st.markdown("---")

# =========================
# CHARTS
# =========================
col1, col2 = st.columns(2)

# Fear & Greed Trend
with col1:
    st.subheader("📈 Fear & Greed Trend")

    if "date" in filtered_fg.columns and "value" in filtered_fg.columns:
        fig = px.line(
            filtered_fg,
            x="date",
            y="value",
            color="classification" if "classification" in filtered_fg.columns else None,
            markers=True,
            template="plotly_dark"
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

# Sentiment Distribution
with col2:
    st.subheader("🧠 Sentiment Distribution")

    if "classification" in filtered_fg.columns:
        pie_fig = px.pie(
            filtered_fg,
            names="classification",
            hole=0.5,
            template="plotly_dark"
        )

        pie_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=450
        )

        st.plotly_chart(pie_fig, use_container_width=True)

st.markdown("---")

# =========================
# TRADING ANALYSIS
# =========================
st.subheader("💹 Trading Analysis")

col3, col4 = st.columns(2)

# Buy/Sell Chart
with col3:

    possible_side_cols = ["Side", "side"]

    side_col = None

    for col in possible_side_cols:
        if col in hist_df.columns:
            side_col = col
            break

    if side_col:
        side_counts = (
            hist_df[side_col]
            .value_counts()
            .reset_index()
        )

        side_counts.columns = ["Side", "Count"]

        bar_fig = px.bar(
            side_counts,
            x="Side",
            y="Count",
            color="Side",
            template="plotly_dark"
        )

        bar_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=450
        )

        st.plotly_chart(bar_fig, use_container_width=True)

# PnL Distribution
with col4:

    pnl_col = None

    for col in ["Closed PnL", "closedPnL", "pnl"]:
        if col in hist_df.columns:
            pnl_col = col
            break

    if pnl_col:
        pnl_fig = px.histogram(
            hist_df,
            x=pnl_col,
            nbins=50,
            template="plotly_dark"
        )

        pnl_fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=450
        )

        st.plotly_chart(pnl_fig, use_container_width=True)

st.markdown("---")

# =========================
# DATA PREVIEW
# =========================
st.subheader("📋 Dataset Preview")

option = st.radio(
    "Choose Dataset",
    ["Fear & Greed Data", "Historical Trading Data"],
    horizontal=True
)

if option == "Fear & Greed Data":
    st.dataframe(fg_df.head(50), use_container_width=True)

else:
    st.dataframe(hist_df.head(50), use_container_width=True)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown("""
<div style='text-align:center'>
    <h4>✨ Built with Streamlit & Plotly</h4>
    <p style='color:gray'>
        Interactive Crypto Analytics Dashboard
    </p>
</div>
""", unsafe_allow_html=True)
