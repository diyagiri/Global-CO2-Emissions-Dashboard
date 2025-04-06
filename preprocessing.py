import pandas as pd

# Load the dataset
file_path = "owid-co2-data.csv"  # Update this if needed
df = pd.read_csv("data/owid-co2-data.csv")

# Step 1: Filter to include data from 1990 onwards
df = df[df["year"] >= 1990]

# Step 2: Remove aggregates like 'World', 'Asia', etc. — keep only countries with ISO codes
df = df[df["iso_code"].notna()]

# Step 3: Select only relevant columns required for your Tableau dashboard
columns_to_keep = [
    "country", "iso_code", "year", "population", "gdp",
    "co2", "co2_per_capita", "co2_growth_prct", "co2_including_luc",
    "coal_co2", "oil_co2", "gas_co2", "cement_co2",
    "share_global_co2", "cumulative_co2",
    "temperature_change_from_co2", "total_ghg"
]
df = df[columns_to_keep]

# Step 4: Drop rows where essential values are missing
df = df.dropna(subset=["co2", "year"])

# Step 5: Export cleaned data for Tableau
df.to_csv("data/cleaned_co2_data_for_tableau.csv", index=False)

print("✅ Cleaned dataset saved as 'cleaned_co2_data_for_tableau.csv'")
