"""
Entry point for Analyzing_NYC_High_School_Data. Loads CSVs and computes key metrics.
"""
import os
import pandas as pd

def main():
    base = os.path.dirname(__file__)
    sat_path = os.path.join(base, "sat_results.csv")
    if not os.path.isfile(sat_path):
        print("=== Analyzing_NYC_High_School_Data ===\nRun from project root. Run 'Schools.ipynb' for full analysis.")
        return
    df = pd.read_csv(sat_path)
    print("=== Analyzing_NYC_High_School_Data ===\nSAT results rows:", len(df))
    if "boro" in df.columns:
        print("Baseline (avg by boro):", df.groupby("boro").size().to_dict())
    print("Full analysis: run 'Schools.ipynb'.")

if __name__ == "__main__":
    main()
