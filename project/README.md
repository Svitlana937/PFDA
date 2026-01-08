# Wind Speed Analysis - Ireland

## Overview

This project analyzes historical wind speed data from Ireland provided by Met Éireann. The analysis explores wind speed patterns over time and their implications for wind energy generation.

## Project Structure

```
project/
├── README.md                  # This file
├── wind_analisys.ipynb       # Main analysis notebook
└── data/
    └── Wind_Speed_hourly.csv # Hourly wind speed data from Met Éireann
```

## Data Source

The dataset contains hourly wind speed measurements collected by Met Éireann (the Irish national meteorological service). The data includes:
- **Date and Time**: Timestamp for each measurement (format: DD-MMM-YYYY HH:MM)
- **Wind Speed**: Wind speed measurements in meters per second (m/s)

## Analysis Contents

The notebook includes the following analyses:

### Data Preparation
- Loading and cleaning the wind speed dataset
- Handling missing and inconsistent values
- Feature engineering (Year, Month, Quarter, Season extraction)

### Exploratory Analysis
1. **Yearly Averages**: Line plot showing average wind speed per year
2. **Monthly Patterns**: Bar chart displaying average wind speed by month
3. **Rolling Averages**: 5-year rolling average to identify trends
4. **Quarterly Analysis**: Wind speed distribution across quarters
5. **Distribution Analysis**: Histogram of wind speeds showing frequency distribution
6. **Heatmap**: Monthly wind speed patterns across years

### Seasonal Analysis
- Grouping data by season (Winter, Spring, Summer, Autumn)
- Comparative analysis of wind speeds across seasons

## Requirements

To run this notebook, you need:
- Python 3.x
- pandas
- matplotlib
- seaborn

## How to Run

1. Ensure all dependencies are installed
2. The data file should be located in `data/Wind_Speed_hourly.csv`
3. Open `wind_analisys.ipynb` in Jupyter Notebook or JupyterLab
4. Run all cells to generate the analysis and visualizations

## Key Visualizations

The analysis produces various charts and plots:
- Line plots for yearly trends
- Bar charts for monthly and seasonal comparisons
- Heatmaps showing patterns across time periods
- Histograms for wind speed distribution

## Notes

- The first 23 rows of the CSV file contain metadata and are skipped during loading
- Wind speed is measured in meters per second (m/s)
- The analysis uses hourly data aggregated to daily, monthly, and yearly averages
- The notebook should be run from top to bottom to reproduce the results
