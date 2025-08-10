# Oura Insights App

A small command line utility that analyzes your Oura Ring readiness data from a CSV export and provides a simple trend analysis.

## Usage

1. Export your readiness data as a CSV file from cloud.ouraring.com.
2. Run the app: `python oura_app.py path/to/readiness.csv`

The script compares the average readiness score of the last seven days with the previous week and prints whether your readiness has improved, declined, or remained stable.
