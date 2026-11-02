import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Real Estate Investment Advisor",
    page_icon="🏡",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("🏡 Real Estate Advisor")

page = st.sidebar.radio(
    "Navigate to:",
    [
        "Dashboard",
        "Investment Calculator",
        "Future Value Predictor",
        "Market Trends",
        "Property Search"
    ]
)

st.sidebar.divider()
st.sidebar.info("Explore property investment opportunities.")

# Load dataset
df = pd.read_csv("data/india_housing_prices_cleaned.zip", compression="zip")

# Dashboard
if page == "Dashboard":
    st.title("🏡 Real Estate Investment Advisor")
    st.subheader("Predict Property Profitability and Estimate Future Value")

    st.write(
        "Analyze property details, evaluate investment potential, "
        "and estimate future property value."
    )

    st.success("Property dataset loaded successfully!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Properties", f"{len(df):,}")

    with col2:
        st.metric(
            "Average Property Price",
            f"₹{df['Price_in_Lakhs'].mean():.2f} Lakhs"
        )

    with col3:
        st.metric("Cities Covered", df["City"].nunique())

    st.divider()
    st.subheader("📊 Property Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

elif page == "Investment Calculator":
    st.title("🏠 Investment Calculator")

    st.write(
        "Evaluate a property's investment potential "
        "using five simple criteria."
    )

    with st.form("property_form"):

        property_price = st.number_input(
            "Property Price (₹ Lakhs)",
            min_value=1.0,
            value=200.0
        )

        property_age = st.number_input(
            "Property Age (Years)",
            min_value=0,
            max_value=200,
            value=5
        )

        nearby_schools = st.number_input(
            "Number of Nearby Schools",
            min_value=0,
            value=7
        )

        nearby_hospitals = st.number_input(
            "Number of Nearby Hospitals",
            min_value=0,
            value=6
        )

        security = st.selectbox(
            "Is Security Available?",
            ["Yes", "No"]
        )

        submit = st.form_submit_button(
            "Evaluate Investment"
        )

    if submit:
        score = 0
        reasons = []

        average_price = df["Price_in_Lakhs"].mean()

        if property_price < average_price:
            score += 1
            reasons.append(
                "Property price is below the dataset average."
            )
        else:
            reasons.append(
                "Property price is at or above the dataset average."
            )

        if property_age <= 10:
            score += 1
            reasons.append("Property is relatively new.")
        else:
            reasons.append(
                "Property is more than 10 years old."
            )

        if nearby_schools >= 5:
            score += 1
            reasons.append(
                "Several nearby schools are listed."
            )
        else:
            reasons.append(
                "Fewer nearby schools are listed."
            )

        if nearby_hospitals >= 5:
            score += 1
            reasons.append(
                "Several nearby hospitals are listed."
            )
        else:
            reasons.append(
                "Fewer nearby hospitals are listed."
            )

        if security == "Yes":
            score += 1
            reasons.append("Security is available.")
        else:
            reasons.append(
                "Check the property's security arrangements."
            )

        if score >= 4:
            category = "Potentially Good Investment"
        elif score >= 2:
            category = "Moderate Investment"
        else:
            category = "Needs Careful Evaluation"

        st.subheader("📋 Investment Assessment")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Investment Score", f"{score}/5")

        with col2:
            st.write("**Category:**")
            st.info(category)

        st.write("**Assessment Details:**")

        for reason in reasons:
            st.write("•", reason)

        st.caption(
            "This is a rule-based assessment, not a guarantee "
            "of profitability. It does not account for all costs, "
            "rental income, or market risks."
        )

elif page == "Future Value Predictor":
    st.title("📈 Future Property Value Predictor")

    st.write(
        "Estimate a property's future value using an assumed "
        "annual growth rate."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        current_price = st.number_input(
            "Current Property Price (₹ Lakhs)",
            min_value=1.0,
            value=200.0,
            key="future_price"
        )

    with col2:
        growth_rate = st.number_input(
            "Annual Growth Rate (%)",
            min_value=0.0,
            max_value=30.0,
            value=6.0,
            step=0.5
        )

    with col3:
        years = st.number_input(
            "Number of Years",
            min_value=1,
            max_value=30,
            value=5
        )

    if st.button("Predict Future Value"):

        future_value = current_price * (
            1 + growth_rate / 100
        ) ** years

        total_growth = future_value - current_price

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Estimated Future Value",
                f"₹{future_value:.2f} Lakhs"
            )

        with col2:
            st.metric(
                "Estimated Value Increase",
                f"₹{total_growth:.2f} Lakhs"
            )

        st.info(
            f"At an assumed annual growth rate of {growth_rate}%, "
            f"the estimated property value after {years} years "
            f"is ₹{future_value:.2f} Lakhs."
        )

        st.caption(
            "This is a mathematical estimate, not a guaranteed "
            "market forecast. Actual property prices may rise or fall."
        )

elif page == "Market Trends":
    st.title("📊 Property Market Trends")

    st.write(
        "Explore insights from the Indian housing dataset."
    )

    chart_options = {
        "Top 10 Cities by Average Property Price":
            "top_10_city_prices.png",
        "Average Price by Property Type":
            "property_type_prices.png",
        "Property Age vs Average Price":
            "property_age_prices.png",
        "Nearby Schools vs Property Prices":
            "schools_vs_property_prices.png",
        "Nearby Hospitals vs Property Prices":
            "hospitals_vs_property_prices.png",
        "Pool Availability vs Average Price":
            "pool_vs_property_prices.png",
        "Public Transport vs Average Price":
            "transport_vs_property_prices.png",
        "Furnishing Status vs Average Price":
            "furnishing_vs_property_prices.png",
        "Availability Status vs Average Price":
            "availability_vs_property_prices.png",
        "BHK vs Average Property Price":
            "bhk_vs_property_prices.png"
    }

    selected_chart = st.selectbox(
        "Choose a chart to explore:",
        list(chart_options.keys())
    )

    from pathlib import Path
    chart_path = Path(__file__).parent / "data" / chart_options[selected_chart] 

    try:
        st.image(
            chart_path,
            caption=selected_chart,
            use_container_width=True
        )
    except Exception:
        st.warning(
            "Chart not found. Check that the PNG file "
            "exists in your data folder."
        )

elif page == "Property Search":
    st.title("🔎 Property Search")

    st.write("Find properties using filters.")

    # City filter
    cities = ["All Cities"] + sorted(
        df["City"].dropna().unique().tolist()
    )

    selected_city = st.selectbox(
        "Select City",
        cities
    )

    # Property type filter
    property_types = ["All Types"] + sorted(
        df["Property_Type"].dropna().unique().tolist()
    )

    selected_type = st.selectbox(
        "Select Property Type",
        property_types
    )

    # BHK filter
    bhk_options = ["All BHK"] + sorted(
        df["BHK"].dropna().unique().tolist()
    )

    selected_bhk = st.selectbox(
        "Select BHK",
        bhk_options
    )

    # Apply filters
    filtered_df = df.copy()

    if selected_city != "All Cities":
        filtered_df = filtered_df[
            filtered_df["City"] == selected_city
        ]

    if selected_type != "All Types":
        filtered_df = filtered_df[
            filtered_df["Property_Type"] == selected_type
        ]

    if selected_bhk != "All BHK":
        filtered_df = filtered_df[
            filtered_df["BHK"] == selected_bhk
        ]

    # Display results
    st.subheader("🏘️ Matching Properties")

    st.write(f"Properties found: {len(filtered_df):,}")

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True
    )
