# Tests

This directory contains unit tests for the solar data analysis project.

## Running Tests

### Run all tests
```bash
pytest
```

### Run with coverage
```bash
pytest --cov=. --cov-report=html
```

### Run specific test file
```bash
pytest tests/test_data_profiler.py
```

### Run specific test
```bash
pytest tests/test_data_profiler.py::TestDataProfiler::test_init
```

### Run with verbose output
```bash
pytest -v
```

## Test Structure

- `test_data_profiler.py` - Tests for DataProfiler class
- `test_data_cleaner.py` - Tests for SolarDataCleaner class
- `test_statistical_tester.py` - Tests for SolarStatisticalTester class
- `test_country_loader.py` - Tests for CleanedCountryDataLoader class
- `conftest.py` - Shared fixtures and configuration

## Test Coverage

The tests cover:
- Data loading and validation
- Summary statistics generation
- Missing value detection and reporting
- Z-score outlier detection
- Missing value imputation
- Outlier removal
- Data export functionality
- Statistical testing (ANOVA, Kruskal-Wallis)
- Cross-country data loading and combination

## Requirements

Tests require:
- pytest >= 7.0.0
- pytest-cov >= 4.0.0 (for coverage reports)

Install with:
```bash
pip install -r requirements.txt
```

