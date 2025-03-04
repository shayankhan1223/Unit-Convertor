import streamlit as st

# Title of the app
st.title("Unit Converter")

# Dictionary of conversion factors (Multiplication & Functions)
conversion_factors = {
    "Meter to Kilometer": 0.001,
    "Kilometer to Meter": 1000,
    "Feet to Inches": 12,
    "Inches to Feet": 1/12,
    "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
    "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9
}

# Dropdown menu for selecting conversion type
conversion_type = st.selectbox("Select Conversion Type", list(conversion_factors.keys()))

# User input field
value = st.number_input("Enter the value:", min_value=0.0, step=0.1)

# Convert button
if st.button("Convert"):
    if callable(conversion_factors[conversion_type]):  
        result = conversion_factors[conversion_type](value)  # Function-based conversion
    else:  
        result = value * conversion_factors[conversion_type]  # Multiplication-based conversion

    # Display result
    st.success(f"Converted Value: {result}")
    