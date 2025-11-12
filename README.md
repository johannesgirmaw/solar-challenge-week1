# Solar Challenge Week 1 – Cross-Country Solar Data Analysis

A modular, object-oriented data science project analyzing solar potential across **Benin** , **Sierra Leone** , and **Togo** . The project leverages irradiance metrics (GHI, DNI, DHI) to identify high-potential regions for solar panel investment.

## Project Structure

```
solar-challenge-week0/
├── clean_data/          # Cleaned CSVs for each country (committed to repo)
├── data/                # Raw CSVs from solar dataset (gitignored)
├── notebooks/           # Jupyter Notebooks (EDA + Comparison)
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── scripts/             # Modularized Python scripts
├── src/                 # Source code (Streamlit app)
├── tests/               # Unit test directory
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions CI pipeline
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignored files
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone git@github.com:johannesgirmaw/solar-challenge-week0.git
cd solar-challenge-week0
```

Or if using HTTPS:
```bash
git clone https://github.com/johannesgirmaw/solar-challenge-week0.git
cd solar-challenge-week0
```

### 2. Create & Activate a Virtual Environment

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install all required packages:
- pandas, numpy (data manipulation)
- matplotlib, seaborn, plotly (visualization)
- scipy (statistical analysis)
- jupyter, ipykernel (notebook support)
- streamlit (dashboard)
- windrose (wind visualization)

### 4. Verify Installation

```bash
python --version  # Should show Python 3.8+
pip list  # Verify all packages are installed
```

### 5. Run the Notebooks

**Start Jupyter Notebook:**
```bash
jupyter notebook
```

**Or use Jupyter Lab:**
```bash
jupyter lab
```

Then navigate to and run the notebooks in order:

1. `notebooks/benin_eda.ipynb` - EDA for Benin data
2. `notebooks/sierraleone_eda.ipynb` - EDA for Sierra Leone data
3. `notebooks/togo_eda.ipynb` - EDA for Togo data
4. `notebooks/compare_countries.ipynb` - Cross-country comparison

**Note:** Make sure to run all cells in each notebook to generate the cleaned data files and visualizations.

### 6. Access Cleaned Data

After running the EDA notebooks, cleaned data files will be available in:
- `clean_data/benin_clean.csv`
- `clean_data/sierraleone_clean.csv`
- `clean_data/togo_clean.csv`

---

## Core Functionality

### Task 1: Git & Environment Setup

- `.gitignore`, `requirements.txt`, GitHub Actions CI.
- Virtual environment setup and tested on GitHub workflows.

### Task 2: Data Cleaning & EDA

- Cleaned solar radiation datasets.
- Outlier detection (Z-score), time-series analysis.
- Correlation heatmaps, bubble charts, and wind/temp distribution.

### Task 3: Cross-Country Comparison

- Combined datasets for Benin, Sierra Leone, and Togo.
- Boxplots for GHI, DNI, DHI across countries.
- Summary tables (mean, median, std).
- Statistical testing (ANOVA & Kruskal–Wallis).
- Visual bar chart of average GHI.
- Markdown insights for reporting.

### Task 4: Dashboard using Streamlit

- Widgets to select countries.

* Boxplot of GHI or other plots .
* Top regions table.
* URL : [https://yohannes-solar-dashboard.streamlit.app/](https://yohannes-solar-dashboard.streamlit.app/ "https://yohannes-solar-dashboard.streamlit.app/")

---

## Project Highlights

### Metrics Used

- **GHI** (Global Horizontal Irradiance)
- **DNI** (Direct Normal Irradiance)
- **DHI** (Diffuse Horizontal Irradiance)

### Visualizations

- Boxplots for inter-country comparisons
- Correlation matrices
- Summary bar charts
- Bubble plots for irradiance interaction

### Statistical Analysis

- One-Way ANOVA and Kruskal–Wallis H-test
- p-values to assess cross-country solar differences

---

## Running Tests

The project includes comprehensive unit tests for all major components. To run the tests:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_data_profiler.py

# Run specific test
pytest tests/test_data_profiler.py::TestDataProfiler::test_init
```

### Test Coverage

The test suite includes:
- **DataProfiler**: Data loading, summary statistics, missing value reports
- **SolarDataCleaner**: Z-score outlier detection, missing value imputation, data export
- **SolarStatisticalTester**: ANOVA and Kruskal-Wallis statistical tests
- **CleanedCountryDataLoader**: Multi-country data loading and combination

All tests are automatically run in the CI/CD pipeline on every push and pull request.

For more details, see [tests/README.md](tests/README.md).

---

## Continuous Integration

This project uses **GitHub Actions** :

- Every push and pull request runs an environment install test using `.github/workflows/ci.yml`
- Easily extendable to include linting, tests, and notebooks execution checks.

---

## Usage Scenarios

- Academics: Comparing solar feasibility across West African nations.
- Engineers: Pre-evaluation for solar installation projects.
- Policymakers: Visual insights into clean energy opportunities.
- Developers: Extendable project for solar modeling or ML integration.

## Example Output Snippet

Metric Country Mean Median Std
GHI Benin 236.23 0.7 328.29
GHI Togo 223.86 0.5 317.31
GHI SierraLeone 185.00 -0.4 279.02
...

---

## Key Insights

- **Benin** shows the highest average and median **GHI** , suggesting top solar potential.
- **Togo** has higher GHI variability, indicating less predictability.
- **Sierra Leone** maintains lower but more stable solar irradiance values.

---

## References

- 📘 [10 Academy Challenge Guide](https://docs.google.com/document/d/1HsCSC_RZk_sj39Cc30OwFX9DLvUoh2OW7Eq0y1Dsf8E/edit)
- 📊 [Solar Radiation Dataset](https://energydata.info/dataset/?q=Solar+Radiation+Measurement&vocab_regions=AFR)
- 📚 [Seaborn Documentation](https://seaborn.pydata.org/)
- 📗 [SciPy Stats (ANOVA &amp; Kruskal)](https://docs.scipy.org/doc/scipy/)

---

## Contributing

We welcome contributions:

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request
