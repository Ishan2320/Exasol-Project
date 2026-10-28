import os
import re
import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from modules.analytics import answer_question, load_sales_data, summarize_result

load_dotenv()
st.set_page_config(page_title="Exasol AI BI Assistant", page_icon="📊", layout="wide")
st.markdown("""
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
div[data-testid="stMetric"] {background:#f7f9fc;border:1px solid #dbe3ef;padding:14px;border-radius:12px}
[data-testid="stSidebar"] {background:#f7f9fc}
</style>
""", unsafe_allow_html=True)

st.title("📊 Exasol AI Business Intelligence Assistant")
st.write("Ask questions about sales data in plain English. This ready-to-run version works locally with sample data; a live Exasol connection is optional.")
with st.sidebar:
    st.header("Data source")
    mode = st.radio("Choose a mode", ["Demo data (ready to run)", "Exasol database (optional)"])
    st.divider()
    st.subheader("Try a question")
    examples = [
        "Which 5 products generated the highest revenue?",
        "Show monthly revenue trends",
        "Which region has the highest revenue?",
        "Show revenue by category",
        "Which customer segment generated the most revenue?",
        "How many orders are there?",
        "Show the top 5 customers by revenue",
        "What is the average order revenue?"
    ]
    for item in examples:
        st.caption("• " + item)
    st.divider()
    st.caption("Demo mode does not require an API key or Exasol account.")

if mode == "Demo data (ready to run)":
    data = load_sales_data()
else:
    st.info("Live Exasol mode is optional. Configure the credentials in `.env`, create/import the SALES table using `sql/schema.sql`, then restart the app.")
    try:
        from modules.exasol import load_exasol_data
        data = load_exasol_data()
    except Exception as exc:
        st.error(f"Exasol connection is not ready: {exc}")
        st.stop()

data["order_date"] = pd.to_datetime(data["order_date"], errors="coerce")
data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce").fillna(0)
data["order_month"] = data["order_date"].dt.to_period("M").astype(str)

st.caption(f"Data source: {'Demo dataset' if mode.startswith('Demo') else 'Exasol'} · {len(data):,} rows")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Total revenue", f"${data['revenue'].sum():,.2f}")
m2.metric("Orders", f"{data['order_id'].nunique():,}")
m3.metric("Customers", f"{data['customer_id'].nunique():,}")
m4.metric("Products", f"{data['product'].nunique():,}")

left, right = st.columns(2)
with left:
    monthly = data.groupby("order_month", as_index=False)["revenue"].sum()
    st.plotly_chart(px.line(monthly, x="order_month", y="revenue", markers=True, title="Monthly revenue"), use_container_width=True)
with right:
    region = data.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    st.plotly_chart(px.bar(region, x="region", y="revenue", title="Revenue by region"), use_container_width=True)

st.subheader("Ask the business assistant")
question = st.text_input("Your question", placeholder="e.g. Which 5 products generated the highest revenue?")
col_a, col_b = st.columns([1, 5])
with col_a:
    run = st.button("Analyze", type="primary", use_container_width=True)
with col_b:
    st.caption("The built-in question engine supports common sales analytics questions and runs without an AI API key.")

if run:
    if not question.strip():
        st.warning("Type a question first.")
    else:
        try:
            result, explanation, sql = answer_question(question, data)
            st.markdown("#### Analysis")
            st.success(explanation)
            with st.expander("View SQL equivalent"):
                st.code(sql, language="sql")
            if isinstance(result, pd.DataFrame):
                st.dataframe(result, use_container_width=True, hide_index=True)
                numeric = result.select_dtypes(include="number").columns.tolist()
                categories = [c for c in result.columns if c not in numeric]
                if numeric and categories and len(result) > 0:
                    xcol = st.selectbox("Chart category", categories, key="chart_x")
                    ycol = st.selectbox("Chart value", numeric, key="chart_y")
                    st.plotly_chart(px.bar(result, x=xcol, y=ycol, title=f"{ycol} by {xcol}"), use_container_width=True)
                st.download_button("Download results CSV", result.to_csv(index=False).encode("utf-8"), "analysis_results.csv", "text/csv")
        except Exception as exc:
            st.error(f"Could not answer that question: {exc}")
            st.info("Try one of the example questions in the sidebar.")

with st.expander("Preview sample data"):
    st.dataframe(data.head(20), use_container_width=True, hide_index=True)

st.divider()
st.caption("Academic prototype · Sample data is synthetic. Validate findings before using them for business decisions.")
