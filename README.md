# Exasol AI Business Intelligence Assistant

## Run it with almost no setup (Windows)
1. Download and extract the ZIP.
2. Install Python 3.11 or 3.12 from https://www.python.org/downloads/ if it is not already installed. Enable **Add Python to PATH**.
3. Double-click `run_windows.bat`.
4. The script creates a local virtual environment, installs dependencies, and launches the dashboard in your browser.
5. In the sidebar, keep **Demo data (ready to run)** selected.
6. Ask one of the example questions.

No API key or Exasol account is needed for the demo application.

## Run manually
```bash
py -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Supported built-in questions
- Which 5 products generated the highest revenue?
- Show monthly revenue trends
- Which region has the highest revenue?
- Show revenue by category
- Which customer segment generated the most revenue?
- How many orders are there?
- Show the top 5 customers by revenue
- What is the average order revenue?
- What is the total revenue?

This is a rule-based natural-language question handler for the supplied demo dataset, not a general-purpose LLM. It works offline after dependencies are installed. The app displays an equivalent SQL query for learning and demonstration.

## Optional live Exasol database
1. Ask your institution/admin for authorized Exasol access.
2. Copy `.env.example` to `.env` and fill in the connection values.
3. Install optional dependencies with `pip install -r requirements-exasol.txt`.
4. Run `sql/schema.sql` in your authorized Exasol schema and import `data/sample_sales.csv` into `SALES`.
5. Restart the app and select **Exasol database (optional)**.

Use credentials with read-only access where possible. Never commit `.env` or database credentials to GitHub. Live mode assumes the table columns in `sql/schema.sql` and the default schema setting are correct for your environment.

## Project contents
- `app.py`: Streamlit UI and charts
- `modules/analytics.py`: built-in question handler and sample data loader
- `modules/exasol.py`: optional Exasol integration
- `data/sample_sales.csv`: synthetic sample sales records
- `sql/schema.sql`: table schema and example query
- `PROJECT_REPORT.md`: initial report draft
- `run_windows.bat`: one-click Windows setup and launcher

## Limitations
The demo uses synthetic data and a fixed set of supported question patterns. The displayed SQL is explanatory in demo mode; the app calculates results using Pandas. Live Exasol mode queries the SALES table. This is an academic prototype, not a production security or decision system.
