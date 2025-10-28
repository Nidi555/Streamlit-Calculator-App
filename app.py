import streamlit as st

# 🎨 App title
st.set_page_config(page_title="Calculator App", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Perform basic arithmetic operations easily!")

# 📥 User input
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# ⚙️ Operation selection
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# 🧠 Calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"✅ Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"✅ Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"✅ Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("⚠️ Cannot divide by zero!")
        else:
            result = num1 / num2
            st.success(f"✅ Result: {num1} ÷ {num2} = {result}")

# ✨ Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")
