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

## Running Tests (Optional)

If tests are defined inside `tests/`, you can run:

<pre class="overflow-visible!" data-start="3119" data-end="3144"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-[5px]">bash</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center rounded-sm px-2 font-sans text-xs"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button><span class="" data-state="closed"><button class="flex items-center gap-1 px-4 py-1 select-none"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pytest tests/
</span></span></code></div></div></pre>

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
