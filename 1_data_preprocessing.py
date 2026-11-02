import pandas as pd

# Load the dataset
df = pd.read_csv("data/india_housing_prices.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Check dataset size
print("\nDataset Shape:")
print(df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Check missing values in each column
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Check duplicate records
print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())
# Check numerical values
print("\nNumerical Data Summary:")
print(df.describe())

# Check invalid property prices
print("\nProperties with price <= 0:")
print((df["Price_in_Lakhs"] <= 0).sum())

# Check invalid property sizes
print("\nProperties with size <= 0:")
print((df["Size_in_SqFt"] <= 0).sum())

# Check invalid BHK values
print("\nProperties with BHK <= 0:")
print((df["BHK"] <= 0).sum())
# Create Price per Square Foot feature
df["Price_per_SqFt"] = (
    df["Price_in_Lakhs"] * 100000
) / df["Size_in_SqFt"]

print("\nPrice per Square Foot - First 5 Properties:")
print(df[["City", "Size_in_SqFt", "Price_in_Lakhs", "Price_per_SqFt"]].head())
# Calculate property age
current_year = 2026

df["Age_of_Property"] = current_year - df["Year_Built"]

print("\nProperty Age - First 5 Records:")
print(df[["Year_Built", "Age_of_Property"]].head())
# Create School Density Score
df["School_Density_Score"] = (
    df["Nearby_Schools"] / df["Size_in_SqFt"]
) * 1000

print("\nSchool Density Score - First 5 Properties:")
print(
    df[["City", "Nearby_Schools", "Size_in_SqFt",
        "School_Density_Score"]].head()
)
# Save the processed dataset
df.to_csv("data/india_housing_prices_cleaned.csv", index=False)

print("\nProcessed dataset saved successfully!")
print("Final Dataset Shape:", df.shape)