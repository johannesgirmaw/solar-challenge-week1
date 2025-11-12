"""
Tests for CleanedCountryDataLoader class.
"""
import pytest
import pandas as pd
import numpy as np
import os


class CleanedCountryDataLoader:
    """Test version matching notebook implementation."""
    def __init__(self, file_map: dict):
        self.file_map = file_map
        self.country_dfs = {}

    def load_data(self):
        """Load and validate datasets for each country."""
        for country, path in self.file_map.items():
            if not os.path.exists(path):
                continue

            try:
                df = pd.read_csv(path)
                df['Country'] = country
                self.country_dfs[country] = df
            except Exception as e:
                continue

        if not self.country_dfs:
            raise ValueError("No datasets could be loaded.")
        return self.country_dfs

    def get_combined_dataframe(self):
        """Combine all loaded data into a single DataFrame."""
        if not self.country_dfs:
            raise ValueError("No data available. Did you call `load_data()`?")
        return pd.concat(self.country_dfs.values(), ignore_index=True)


@pytest.fixture
def sample_country_files(tmp_path):
    """Create sample CSV files for different countries."""
    files = {}
    countries = ['Benin', 'Sierra Leone', 'Togo']
    
    for country in countries:
        np.random.seed(42)
        data = pd.DataFrame({
            'GHI': np.random.normal(200, 50, 50),
            'DNI': np.random.normal(150, 40, 50),
            'DHI': np.random.normal(100, 30, 50),
        })
        file_path = tmp_path / f"{country.lower().replace(' ', '_')}.csv"
        data.to_csv(file_path, index=False)
        files[country] = str(file_path)
    
    return files


class TestCleanedCountryDataLoader:
    """Test suite for CleanedCountryDataLoader class."""

    def test_init(self, sample_country_files):
        """Test initialization."""
        loader = CleanedCountryDataLoader(sample_country_files)
        assert loader.file_map == sample_country_files
        assert loader.country_dfs == {}

    def test_load_data(self, sample_country_files):
        """Test data loading."""
        loader = CleanedCountryDataLoader(sample_country_files)
        result = loader.load_data()
        assert len(result) == 3  # Three countries
        assert 'Benin' in result
        assert 'Sierra Leone' in result
        assert 'Togo' in result
        assert all('Country' in df.columns for df in result.values())

    def test_load_data_adds_country_column(self, sample_country_files):
        """Test that Country column is added."""
        loader = CleanedCountryDataLoader(sample_country_files)
        loader.load_data()
        for country, df in loader.country_dfs.items():
            assert 'Country' in df.columns
            assert all(df['Country'] == country)

    def test_load_data_handles_missing_files(self, tmp_path):
        """Test that missing files are handled gracefully."""
        file_map = {
            'Benin': str(tmp_path / 'benin.csv'),
            'Missing': str(tmp_path / 'missing.csv')
        }
        # Create only one file
        data = pd.DataFrame({'GHI': [1, 2, 3]})
        data.to_csv(file_map['Benin'], index=False)
        
        loader = CleanedCountryDataLoader(file_map)
        result = loader.load_data()
        assert 'Benin' in result
        assert 'Missing' not in result

    def test_load_data_raises_error_if_no_files(self, tmp_path):
        """Test that error is raised if no files can be loaded."""
        file_map = {
            'Missing1': str(tmp_path / 'missing1.csv'),
            'Missing2': str(tmp_path / 'missing2.csv')
        }
        loader = CleanedCountryDataLoader(file_map)
        with pytest.raises(ValueError):
            loader.load_data()

    def test_get_combined_dataframe(self, sample_country_files):
        """Test combining dataframes."""
        loader = CleanedCountryDataLoader(sample_country_files)
        loader.load_data()
        combined = loader.get_combined_dataframe()
        assert isinstance(combined, pd.DataFrame)
        assert len(combined) > 0
        assert 'Country' in combined.columns
        assert 'GHI' in combined.columns

    def test_get_combined_dataframe_raises_error_if_no_data(self, sample_country_files):
        """Test that error is raised if no data is loaded."""
        loader = CleanedCountryDataLoader(sample_country_files)
        with pytest.raises(ValueError):
            loader.get_combined_dataframe()

    def test_get_combined_dataframe_preserves_all_countries(self, sample_country_files):
        """Test that all countries are present in combined dataframe."""
        loader = CleanedCountryDataLoader(sample_country_files)
        loader.load_data()
        combined = loader.get_combined_dataframe()
        unique_countries = combined['Country'].unique()
        assert len(unique_countries) == 3
        assert 'Benin' in unique_countries
        assert 'Sierra Leone' in unique_countries
        assert 'Togo' in unique_countries

