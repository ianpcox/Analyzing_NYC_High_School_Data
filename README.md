# NYC High School Performance Analysis (Project Elevate)

This repository transforms a basic exploratory data analysis (EDA) notebook into a **production-ready School Insights Platform**.

By merging six fragmented datasets from the NYC Department of Education (SAT results, demographics, AP participation, class sizes, graduation rates, and school directory info), we constructed a unified dataset of 340 high schools. The analysis reveals stark geographic and demographic disparities in standardized test performance, proving that demographic composition alone explains over 80% of the variance in school-level SAT scores.

## Project Structure

* `nyc_pipeline.py` — The core reproducible data pipeline. Merges the datasets, computes correlations, runs OLS regression, and generates all visualizations and the dashboard.
* `merged_schools.csv` — The final, cleaned, and unified dataset of 340 NYC high schools.
* `docs/report.md` — A comprehensive paper-style report detailing the methodology, demographic correlations, and regression findings.
* `docs/dashboard.html` — An interactive Plotly dashboard exploring the data from multiple angles.
* `docs/assets/` — Generated static charts supporting the report.
* `Schools.ipynb` — The original exploratory notebook.

## Key Findings

* **Demographics drive outcomes:** There are strong positive correlations between SAT scores and the percentage of White ($r = +0.64$) and Asian ($r = +0.59$) students, and strong negative correlations with ELL ($r = -0.43$) and Special Education ($r = -0.47$) populations.
* **Geographic inequality:** Staten Island and Queens significantly outperform the Bronx and Brooklyn on average SAT scores.
* **Predictability:** An OLS regression model using just four demographic variables (`% White`, `% Asian`, `% ELL`, `% SpEd`) achieves an $R^2$ of 0.805, explaining 80.5% of the variance in SAT scores.

Read the full analysis in [docs/report.md](docs/report.md).

## How to Run

### 1. Run the Data Pipeline
This script will read the raw CSVs, merge them, run the statistical models, and generate all charts and the interactive dashboard.
```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels plotly
python nyc_pipeline.py
```

### 2. View the Interactive Dashboard
Open `docs/dashboard.html` in any web browser to explore the interactive Plotly visualizations.
