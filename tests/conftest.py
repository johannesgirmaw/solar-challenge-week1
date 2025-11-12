"""
Pytest configuration and shared fixtures.
"""
import pytest
import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path

# Add project root to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture
def sample_solar_data():
    """Create comprehensive sample solar data."""
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
        'RH': np.random.normal(60, 10, n_rows),
        'BP': np.random.normal(1013, 10, n_rows),
    }
    return pd.DataFrame(data)


@pytest.fixture
def temp_csv_file(sample_solar_data, tmp_path):
    """Create a temporary CSV file."""
    file_path = tmp_path / "test_solar_data.csv"
    sample_solar_data.to_csv(file_path, index=False)
    return str(file_path)

