import pandas as pd

# Load the processed dataset
df = pd.read_csv("data/india_housing_prices_cleaned.csv")

print("Dataset loaded successfully!")
print("Dataset Shape:", df.shape)

# Average property price by city
city_prices = df.groupby("City")["Price_in_Lakhs"].mean()
city_prices = city_prices.sort_values(ascending=False)

print("\nAverage Property Price by City (in Lakhs):")
print(city_prices)

# Five most expensive cities by average property price
print("\nTop 5 Cities by Average Property Price:")
print(city_prices.head(5))

# Five most affordable cities by average property price
print("\nTop 5 Cities by Average Property Price (Lowest):")
print(city_prices.tail(5))
import matplotlib.pyplot as plt

# Find the 10 cities with the highest average property prices
top_10_cities = city_prices.head(10)

# Create a bar chart
plt.figure(figsize=(10, 6))
top_10_cities.plot(kind="bar")

plt.title("Top 10 Cities by Average Property Price")
plt.xlabel("City")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("data/top_10_city_prices.png")

plt.show()

print("\nChart saved successfully!")
# Average property price by property type
property_type_prices = (
    df.groupby("Property_Type")["Price_in_Lakhs"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Property Price by Property Type:")
print(property_type_prices)

# Create a bar chart
plt.figure(figsize=(8, 5))
property_type_prices.plot(kind="bar")

plt.title("Average Property Price by Property Type")
plt.xlabel("Property Type")
plt.ylabel("Average Price (in Lakhs)")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("data/property_type_prices.png")

plt.show()

print("\nProperty type chart saved successfully!")
# Average property price by property age
age_prices = (
    df.groupby("Age_of_Property")["Price_in_Lakhs"]
    .mean()
)

print("\nAverage Property Price by Age:")
print(age_prices)

# Create a line chart
plt.figure(figsize=(10, 6))
age_prices.plot(kind="line", marker="o")

plt.title("Property Age vs Average Property Price")
plt.xlabel("Property Age (Years)")
plt.ylabel("Average Property Price (in Lakhs)")
plt.grid(True)
plt.tight_layout()

# Save the chart
plt.savefig("data/property_age_prices.png")

plt.show()

print("\nProperty age chart saved successfully!")
# Analyze nearby schools and property prices
school_prices = (
    df.groupby("Nearby_Schools")["Price_in_Lakhs"]
    .mean()
)

print("\nAverage Property Price by Number of Nearby Schools:")
print(school_prices)

# Create a chart
plt.figure(figsize=(8, 5))
school_prices.plot(kind="bar")

plt.title("Nearby Schools vs Average Property Price")
plt.xlabel("Number of Nearby Schools")
plt.ylabel("Average Property Price (in Lakhs)")
plt.tight_layout()

plt.savefig("data/schools_vs_property_prices.png")
plt.show()

print("\nSchools analysis chart saved successfully!")
# Analyze nearby hospitals and property prices
hospital_prices = (
    df.groupby("Nearby_Hospitals")["Price_in_Lakhs"]
    .mean()
)

print("\nAverage Property Price by Number of Nearby Hospitals:")
print(hospital_prices)

# Create a chart
plt.figure(figsize=(8, 5))
hospital_prices.plot(kind="bar")

plt.title("Nearby Hospitals vs Average Property Price")
plt.xlabel("Number of Nearby Hospitals")
plt.ylabel("Average Property Price (in Lakhs)")
plt.tight_layout()

plt.savefig("data/hospitals_vs_property_prices.png")
plt.show()

print("\nHospital analysis chart saved successfully!")
# Analyze property amenities and prices
df["Has_Pool"] = df["Amenities"].str.contains(
    "Pool", case=False, na=False
)

pool_prices = (
    df.groupby("Has_Pool")["Price_in_Lakhs"]
    .mean()
)

print("\nAverage Property Price by Pool Availability:")
print(pool_prices)

# Create a chart
plt.figure(figsize=(7, 5))
pool_prices.plot(kind="bar")

plt.title("Pool Availability vs Average Property Price")
plt.xlabel("Has Swimming Pool")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(
    ticks=[0, 1],
    labels=["No Pool", "Has Pool"],
    rotation=0
)
plt.tight_layout()

plt.savefig("data/pool_vs_property_prices.png")
plt.show()

print("\nPool analysis chart saved successfully!")
# Analyze public transport accessibility
transport_prices = (
    df.groupby("Public_Transport_Accessibility")["Price_in_Lakhs"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Property Price by Transport Accessibility:")
print(transport_prices)

# Create a chart
plt.figure(figsize=(8, 5))
transport_prices.plot(kind="bar")

plt.title("Public Transport Accessibility vs Property Price")
plt.xlabel("Public Transport Accessibility")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/transport_vs_property_prices.png")
plt.show()

print("\nTransport analysis chart saved successfully!")
# Analyze furnishing status and property prices
furnishing_prices = (
    df.groupby("Furnished_Status")["Price_in_Lakhs"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Property Price by Furnishing Status:")
print(furnishing_prices)

# Create a chart
plt.figure(figsize=(8, 5))
furnishing_prices.plot(kind="bar")

plt.title("Furnishing Status vs Average Property Price")
plt.xlabel("Furnishing Status")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/furnishing_vs_property_prices.png")
plt.show()

print("\nFurnishing analysis chart saved successfully!")
# Analyze availability status and property prices
availability_prices = (
    df.groupby("Availability_Status")["Price_in_Lakhs"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Property Price by Availability Status:")
print(availability_prices)

# Create a bar chart
plt.figure(figsize=(8, 5))
availability_prices.plot(kind="bar")

plt.title("Availability Status vs Average Property Price")
plt.xlabel("Availability Status")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/availability_vs_property_prices.png")
plt.show()

print("\nAvailability analysis chart saved successfully!")
# Analyze BHK and property prices
bhk_prices = (
    df.groupby("BHK")["Price_in_Lakhs"]
    .mean()
)

print("\nAverage Property Price by BHK:")
print(bhk_prices)

# Create a bar chart
plt.figure(figsize=(8, 5))
bhk_prices.plot(kind="bar")

plt.title("BHK vs Average Property Price")
plt.xlabel("Number of Bedrooms (BHK)")
plt.ylabel("Average Property Price (in Lakhs)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("data/bhk_vs_property_prices.png")
plt.show()

print("\nBHK analysis chart saved successfully!")