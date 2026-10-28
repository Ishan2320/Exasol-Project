# PROJECT REPORT
## Exasol AI Business Intelligence Assistant

### Abstract
This project demonstrates a business intelligence dashboard that helps users explore sales data through a simple natural-language question interface. It displays key performance indicators, revenue charts, result tables, and SQL equivalents for common analytical questions. The ready-to-run demo uses a bundled synthetic sales dataset and does not require an API key. An optional Exasol integration is included for environments where database access is available.

### 1. Introduction
Business intelligence is used to understand sales, revenue, customer segments, and product performance. This project provides a simple interface for common questions, making basic analytics more accessible to users who may not be comfortable writing SQL.

### 2. Problem Statement
Users often need to write queries or manually prepare reports to answer routine questions about sales performance. The project aims to simplify this process with an interactive dashboard and a natural-language question handler.

### 3. Objectives
1. Build an interactive business analytics dashboard.
2. Present revenue, order, customer, and product metrics.
3. Support common sales questions in plain English.
4. Display the SQL equivalent of each supported question.
5. Visualize results using charts and tables.
6. Provide CSV export.
7. Include an optional Exasol database connection.

### 4. Proposed System
The system uses Streamlit for the user interface, Pandas for the demo analytics, Plotly for visualization, and Exasol as an optional analytical database. In demo mode, a rule-based question handler maps supported questions to calculations on synthetic sales data. In live mode, the app retrieves data from an Exasol SALES table.

### 5. Technology Stack
- Python
- Exasol (optional live database)
- SQL
- Streamlit
- Pandas
- Plotly
- SQLAlchemy and Exasol SQLAlchemy driver (optional live connection)

### 6. Modules
**Dashboard module:** Shows headline metrics and monthly/regional revenue charts.

**Question handling module:** Recognizes supported natural-language sales questions and calculates results.

**SQL display module:** Shows an equivalent SQL query for learning purposes.

**Visualization module:** Displays result tables and interactive bar charts.

**Export module:** Allows the user to download query results as CSV.

**Exasol connector:** Optional connection to an authorized Exasol database.

### 7. Methodology
1. Load the sales dataset.
2. Calculate headline metrics and revenue trends.
3. Accept a business question.
4. Match the question to a supported analytics operation.
5. Calculate results using Pandas in demo mode.
6. Display a corresponding SQL example.
7. Show a result table, chart, and CSV download option.

### 8. Expected Results
The demo dashboard should show headline metrics, monthly revenue, regional revenue, and results for supported questions. The live database functionality depends on valid Exasol credentials and a correctly populated SALES table. Results should be validated against the underlying data.

### 9. Applications
- Sales reporting
- Product performance analytics
- Regional comparisons
- Customer segment analysis
- Introductory self-service business intelligence demonstrations

### 10. Limitations and Future Enhancements
The current demo supports a fixed set of question patterns and uses synthetic data. Future work can add LLM-based question interpretation, authentication, query auditing, stronger access controls, broader schema support, and forecasting using suitable historical data.

### 11. Conclusion
The project demonstrates a compact business intelligence application combining Python, data processing, SQL concepts, and interactive visualization. Its demo mode is easy to run, while the optional Exasol connector provides a path toward live analytical database integration.

### References
1. Exasol documentation: https://docs.exasol.com/
2. Streamlit documentation: https://docs.streamlit.io/
3. Pandas documentation: https://pandas.pydata.org/docs/
4. Plotly Python documentation: https://plotly.com/python/
