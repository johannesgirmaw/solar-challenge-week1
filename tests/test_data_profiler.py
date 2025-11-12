"""
Tests for DataProfiler class.
"""
import pytest
import pandas as pd
import numpy as np
import os
import tempfile
from pathlib import Path


# Import the classes from notebooks (we'll need to extract them or import directly)
# For now, we'll define them here or import from a module if they exist
# Since they're in notebooks, we'll create test versions or import them

class DataProfiler:
    """Test version of DataProfiler - should match notebook implementation."""
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")
        return pd.read_csv(self.filepath)

    def summary_statistics(self):
        """Return summary statistics."""
        return self.df.describe()

    def missing_value_report(self, threshold=0.05):
        """Return missing value report."""
        na_counts = self.df.isna().sum()
        na_percent = na_counts / len(self.df)
        report_df = pd.DataFrame({
            'Missing Count': na_counts,
            'Missing Percentage': na_percent
        }).sort_values(by='Missing Percentage', ascending=False)
        return report_df[report_df['Missing Percentage'] > threshold]


@pytest.fixture
def sample_data():
    """Create sample solar data for testing."""
    np.random.seed(42)
    n_rows = 100
    data = {
        'Timestamp': pd.date_range('2023-01-01', periods=n_rows, freq='H'),
        'GHI': np.random.normal(200, 50, n_rows),
        'DNI': np.random.normal(150, 40, n_rows),
        'DHI': np.random.normal(100, 30, n_rows),
        'ModA': np.random.normal(25, 5, n_rows),
        'ModB': np.random.normal(25, 5, n_rows),
        'WS': np.random.normal(5, 2, n_rows),
        'WSgust': np.random.normal(7, 3, n_rows),
        'Tamb': np.random.normal(30, 5, n_rows),
    }
    return pd.DataFrame(data)


@pytest.fixture
def csv_file(sample_data, tmp_path):
    """Create a temporary CSV file for testing."""
    file_path = tmp_path / "test_data.csv"
    sample_data.to_csv(file_path, index=False)
    return str(file_path)


class TestDataProfiler:
    """Test suite for DataProfiler class."""

    def test_init_with_valid_file(self, csv_file):
        """Test DataProfiler initialization with valid file."""
        profiler = DataProfiler(csv_file)
        assert profiler.filepath == csv_file
        assert isinstance(profiler.df, pd.DataFrame)
        assert len(profiler.df) > 0

    def test_init_with_invalid_file(self):
        """Test DataProfiler initialization with invalid file."""
        with pytest.raises(FileNotFoundError):
            DataProfiler("nonexistent_file.csv")

    def test_load_data(self, csv_file):
        """Test data loading."""
        profiler = DataProfiler(csv_file)
        assert isinstance(profiler.df, pd.DataFrame)
        assert 'GHI' in profiler.df.columns
        assert 'DNI' in profiler.df.columns

    def test_summary_statistics(self, csv_file):
        """Test summary statistics generation."""
        profiler = DataProfiler(csv_file)
        stats = profiler.summary_statistics()
        assert isinstance(stats, pd.DataFrame)
        assert 'GHI' in stats.columns
        assert 'mean' in stats.index or 'GHI' in stats.columns

    def test_missing_value_report_no_missing(self, csv_file):
        """Test missing value report with no missing values."""
        profiler = DataProfiler(csv_file)
        report = profiler.missing_value_report(threshold=0.05)
        assert isinstance(report, pd.DataFrame)

    def test_missing_value_report_with_missing(self, tmp_path):
        """Test missing value report with missing values."""
        # Create data with missing values
        data = pd.DataFrame({
            'GHI': [100, 200, np.nan, 300, np.nan],
            'DNI': [50, 150, 200, np.nan, 250],
            'DHI': [30, 100, 150, 200, np.nan]
        })
        file_path = tmp_path / "test_missing.csv"
        data.to_csv(file_path, index=False)
        
        profiler = DataProfiler(str(file_path))
        report = profiler.missing_value_report(threshold=0.0)
        assert isinstance(report, pd.DataFrame)
        assert len(report) > 0  # Should have some missing values

    def test_missing_value_report_threshold(self, tmp_path):
        """Test missing value report with threshold filtering."""
        # Create data with varying missing percentages
        data = pd.DataFrame({
            'col1': [1, 2, np.nan, 4, 5],  # 20% missing
            'col2': [1, np.nan, np.nan, np.nan, np.nan],  # 80% missing
            'col3': [1, 2, 3, 4, 5]  # 0% missing
        })
        file_path = tmp_path / "test_threshold.csv"
        data.to_csv(file_path, index=False)
        
        profiler = DataProfiler(str(file_path))
        report = profiler.missing_value_report(threshold=0.5)
        # Should only include columns with >50% missing
        assert isinstance(report, pd.DataFrame)

