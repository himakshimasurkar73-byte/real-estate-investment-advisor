import pandas as pd

# Load processed property data
df = pd.read_csv("data/india_housing_prices_cleaned.csv")

# Function to evaluate a property
def evaluate_property(property_data):

    score = 0
    reasons = []

    # Rule 1: Property price compared with dataset average
    average_price = df["Price_in_Lakhs"].mean()

    if property_data["Price_in_Lakhs"] < average_price:
        score += 1
        reasons.append("Price is below the dataset average.")
    else:
        reasons.append("Price is at or above the dataset average.")

    # Rule 2: Property age
    if property_data["Age_of_Property"] <= 10:
        score += 1
        reasons.append("Property is relatively new.")
    else:
        reasons.append("Property is more than 10 years old.")

    # Rule 3: Nearby schools
    if property_data["Nearby_Schools"] >= 5:
        score += 1
        reasons.append("Several nearby schools are listed.")
    else:
        reasons.append("Fewer nearby schools are listed.")

    # Rule 4: Nearby hospitals
    if property_data["Nearby_Hospitals"] >= 5:
        score += 1
        reasons.append("Several nearby hospitals are listed.")
    else:
        reasons.append("Fewer nearby hospitals are listed.")

    # Rule 5: Security
    if str(property_data["Security"]).strip().lower() in ["yes", "available", "true"]:
        score += 1
        reasons.append("Security is available.")
    else:
        reasons.append("Check the property's security arrangements.")

    # Investment category
    if score >= 4:
        category = "Potentially Good Investment"
    elif score >= 2:
        category = "Moderate Investment"
    else:
        category = "Needs Careful Evaluation"

    return category, score, reasons


print("Investment Advisor loaded successfully!")
print("Dataset average property price:",
      round(df["Price_in_Lakhs"].mean(), 2), "lakhs")
# Test the Investment Advisor with one property
sample_property = {
    "Price_in_Lakhs": 200,
    "Age_of_Property": 5,
    "Nearby_Schools": 7,
    "Nearby_Hospitals": 6,
    "Security": "Yes"
}

# Evaluate the sample property
category, score, reasons = evaluate_property(sample_property)

print("\n----- INVESTMENT ADVISOR RESULT -----")
print("Property Price: ₹200 Lakhs")
print("Investment Score:", score, "/ 5")
print("Investment Category:", category)

print("\nReasons:")
for reason in reasons:
    print("-", reason)
    # Estimate future property value after 5 years

def predict_future_value(current_price, annual_growth_rate=0.06, years=5):
    future_value = current_price * (1 + annual_growth_rate) ** years
    return future_value
# Test future value prediction
current_price = 200

future_price = predict_future_value(current_price)

print("\n----- FUTURE PROPERTY VALUE -----")
print("Current Property Price: ₹", current_price, "Lakhs")
print("Estimated Value After 5 Years: ₹", round(future_price, 2), "Lakhs")