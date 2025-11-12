"""
Tests for SolarStatisticalTester class.
"""
import pytest
import pandas as pd
import numpy as np
from scipy.stats import f_oneway, kruskal


class SolarStatisticalTester:
    """Test version matching notebook implementation."""
    def __init__(self, df: pd.DataFrame, group_col='Country'):
        self.df = df
        self.group_col = group_col

    def _prepare_groups(self, metric: str):
        """Split metric values by country."""
        if self.group_col not in self.df.columns:
            raise ValueError(f"Missing grouping column '{self.group_col}' in DataFrame.")
        if metric not in self.df.columns:
            raise ValueError(f"Metric '{metric}' not found in DataFrame.")

        grouped = self.df.groupby(self.group_col)[metric].apply(list)
        if len(grouped) < 2:
            raise ValueError("Need at least two groups for statistical testing.")
        return grouped

    def run_anova(self, metric: str):
        """Run one-way ANOVA."""
        try:
            groups = self._prepare_groups(metric)
            stat, p_value = f_oneway(*groups)
            return {'method': 'ANOVA', 'stat': stat, 'p_value': p_value}
        except Exception as e:
            return None

    def run_kruskal(self, metric: str):
        """Run Kruskal-Wallis H-test."""
        try:
            groups = self._prepare_groups(metric)
            stat, p_value = kruskal(*groups)
            return {'method': 'Kruskal-Wallis', 'stat': stat, 'p_value': p_value}
        except Exception as e:
            return None


@pytest.fixture
def sample_country_data():
    """Create sample data for multiple countries."""
    np.random.seed(42)
    data = []
    countries = ['Benin', 'Sierra Leone', 'Togo']
    
    for country in countries:
        n = 50
        country_data = pd.DataFrame({
            'Country': [country] * n,
            'GHI': np.random.normal(200 + np.random.randint(-20, 20), 50, n),
            'DNI': np.random.normal(150 + np.random.randint(-15, 15), 40, n),
            'DHI': np.random.normal(100 + np.random.randint(-10, 10), 30, n),
        })
        data.append(country_data)
    
    return pd.concat(data, ignore_index=True)


class TestSolarStatisticalTester:
    """Test suite for SolarStatisticalTester class."""

    def test_init(self, sample_country_data):
        """Test initialization."""
        tester = SolarStatisticalTester(sample_country_data)
        assert tester.df is not None
        assert tester.group_col == 'Country'

    def test_prepare_groups(self, sample_country_data):
        """Test group preparation."""
        tester = SolarStatisticalTester(sample_country_data)
        groups = tester._prepare_groups('GHI')
        assert len(groups) == 3  # Three countries
        assert all(isinstance(g, list) for g in groups)

    def test_prepare_groups_missing_column(self, sample_country_data):
        """Test error when metric column is missing."""
        tester = SolarStatisticalTester(sample_country_data)
        with pytest.raises(ValueError):
            tester._prepare_groups('NonExistentColumn')

    def test_prepare_groups_missing_group_column(self):
        """Test error when group column is missing."""
        df = pd.DataFrame({'GHI': [1, 2, 3]})
        tester = SolarStatisticalTester(df, group_col='Country')
        with pytest.raises(ValueError):
            tester._prepare_groups('GHI')

    def test_prepare_groups_insufficient_groups(self):
        """Test error when there's only one group."""
        df = pd.DataFrame({
            'Country': ['Benin', 'Benin', 'Benin'],
            'GHI': [1, 2, 3]
        })
        tester = SolarStatisticalTester(df)
        with pytest.raises(ValueError):
            tester._prepare_groups('GHI')

    def test_run_anova(self, sample_country_data):
        """Test ANOVA execution."""
        tester = SolarStatisticalTester(sample_country_data)
        result = tester.run_anova('GHI')
        assert result is not None
        assert result['method'] == 'ANOVA'
        assert 'stat' in result
        assert 'p_value' in result
        assert isinstance(result['stat'], (int, float))
        assert isinstance(result['p_value'], (int, float))
        assert 0 <= result['p_value'] <= 1

    def test_run_anova_different_metric(self, sample_country_data):
        """Test ANOVA with different metric."""
        tester = SolarStatisticalTester(sample_country_data)
        result = tester.run_anova('DNI')
        assert result is not None
        assert result['method'] == 'ANOVA'

    def test_run_kruskal(self, sample_country_data):
        """Test Kruskal-Wallis execution."""
        tester = SolarStatisticalTester(sample_country_data)
        result = tester.run_kruskal('GHI')
        assert result is not None
        assert result['method'] == 'Kruskal-Wallis'
        assert 'stat' in result
        assert 'p_value' in result
        assert isinstance(result['stat'], (int, float))
        assert isinstance(result['p_value'], (int, float))
        assert 0 <= result['p_value'] <= 1

    def test_run_kruskal_different_metric(self, sample_country_data):
        """Test Kruskal-Wallis with different metric."""
        tester = SolarStatisticalTester(sample_country_data)
        result = tester.run_kruskal('DHI')
        assert result is not None
        assert result['method'] == 'Kruskal-Wallis'

    def test_run_anova_handles_errors(self):
        """Test that ANOVA handles errors gracefully."""
        df = pd.DataFrame({'GHI': [1, 2, 3]})
        tester = SolarStatisticalTester(df, group_col='Country')
        result = tester.run_anova('GHI')
        # Should return None when error occurs
        assert result is None

    def test_run_kruskal_handles_errors(self):
        """Test that Kruskal-Wallis handles errors gracefully."""
        df = pd.DataFrame({'GHI': [1, 2, 3]})
        tester = SolarStatisticalTester(df, group_col='Country')
        result = tester.run_kruskal('GHI')
        # Should return None when error occurs
        assert result is None

