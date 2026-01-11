# Wind Speed Analysis – Ireland (Dublin Airport)

## Project Overview
This project analyses historical wind speed data from Met Éireann to explore wind behaviour over time and assess its relevance for wind energy applications.

The analysis focuses on Dublin Airport using long-term hourly observations.

## Data Source
The dataset was obtained from Met Éireann’s Historical Data service.
- Station: Dublin Airport
- Data resolution: Hourly
- Time span: Mid-20th century to recent years

The original dataset required preprocessing due to non-standard CSV formatting.

## Tools and Technologies
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Data Preparation
The following steps were performed:
- Removal of metadata and descriptive header rows
- Robust CSV parsing using the Python engine
- Datetime parsing of the `date` column
- Selection of wind speed (`wdsp`) as the primary variable

## Analysis Performed
- Visualisation of raw hourly wind speed data
- Monthly aggregation to identify seasonal patterns
- Yearly aggregation to examine long-term trends

## Key Findings
- Hourly data shows high short-term variability
- Monthly averages reveal clearer seasonal behaviour
- Yearly averages suggest relatively stable wind conditions over time

## Conclusion
This analysis demonstrates how real-world meteorological data can be cleaned, processed, and analysed using Python. Aggregating wind speed data at different temporal resolutions provides meaningful insight into both short-term variability and long-term trends, which are relevant for renewable energy considerations.

## References
- Met Éireann – Historical Weather Data (https://www.met.ie)
