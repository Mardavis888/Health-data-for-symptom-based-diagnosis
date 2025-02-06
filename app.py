import streamlit as st

# Health data for symptom-based diagnosis
health_data = {
    "fever": {
        "possible_illnesses": ["Flu", "COVID-19"],
        "cure": "Rest, stay hydrated, and take antipyretics like paracetamol.",
        "tips": ["Stay hydrated by drinking water regularly.", "Rest and avoid overexertion."]
    },
    "diabetes": {
        "possible_illnesses": ["Type 1 Diabetes", "Type 2 Diabetes"],
        "cure": "Insulin therapy or prescribed oral medications.",
        "tips": ["Avoid sugary foods and drinks.", "Follow a balanced diet and stay active."]
    },
    "lung cancer": {
        "possible_illnesses": ["Lung Cancer"],
        "cure": "Seek immediate medical consultation for chemotherapy or surgery.",
        "tips": ["Avoid smoking or exposure to polluted air.", "Maintain a healthy diet rich in vitamins."]
    },
    "breast cancer": {
        "possible_illnesses": ["Breast Cancer"],
        "cure": "Treatment may involve surgery, radiation therapy, or targeted drugs.",
        "tips": ["Perform regular self-examinations.", "Consult an oncologist for specialized care."]
    },
    "cough": {
        "possible_illnesses": ["Cold", "Bronchitis", "COVID-19"],
        "cure": "Stay hydrated and take over-the-counter cough suppressants if necessary.",
        "tips": ["Drink warm fluids, like tea with honey.", "Use a humidifier to keep the air moist."]
    },
    "headache": {
        "possible_illnesses": ["Migraine", "Tension Headache"],
        "cure": "Rest, avoid stress, and take pain relievers if needed.",
        "tips": ["Rest in a dark, quiet room.", "Apply a cold or warm compress.", "Stay hydrated."]
    },
    "sore throat": {
        "possible_illnesses": ["Cold", "Tonsillitis"],
        "cure": "Gargle with salt water and stay hydrated.",
        "tips": ["Gargle with warm salt water.", "Drink warm liquids, like herbal tea with honey."]
    },
    "fatigue": {
        "possible_illnesses": ["Anemia", "COVID-19"],
        "cure": "Get enough rest and maintain a nutritious diet.",
        "tips": ["Get enough sleep.", "Eat a balanced diet.", "Stay hydrated."]
    },
}

# Function to determine blood pressure status
def check_blood_pressure(bp, age):
    if age < 13:
        normal_range = (80, 120)
    elif 13 <= age <= 19:
        normal_range = (90, 130)
    elif 20 <= age <= 59:
        normal_range = (110, 140)
    else:
        normal_range = (120, 150)

    if bp < normal_range[0]:
        return "Low", f"Your blood pressure ({bp}) is low for your age."
    elif bp > normal_range[1]:
        return "High", f"Your blood pressure ({bp}) is high for your age."
    else:
        return "Normal", f"Your blood pressure ({bp}) is normal for your age."

# Function for BMI calculation
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif 18.5 <= bmi < 24.9:
        return bmi, "Normal weight"
    elif 25 <= bmi < 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obese"

# Function for symptom diagnosis
def diagnose_illness(symptoms):
    possible_illnesses, cures, tips = set(), [], []
    for symptom in symptoms:
        if symptom in health_data:
            illness_info = health_data[symptom]
            possible_illnesses.update(illness_info["possible_illnesses"])
            cures.append(illness_info["cure"])
            tips.extend(illness_info["tips"])
    return possible_illnesses, cures, tips

# Function for vitamins and minerals test
def vitamins_and_minerals_test(symptoms):
    deficiencies = {
        "fatigue": "Iron or Vitamin B12 deficiency",
        "hair loss": "Zinc or Biotin deficiency",
        "dry skin": "Vitamin E or Omega-3 deficiency",
        "muscle cramps": "Magnesium or Potassium deficiency",
    }
    recommendations = {
        "Iron or Vitamin B12 deficiency": "Eat leafy greens, red meat, or take B12 supplements.",
        "Zinc or Biotin deficiency": "Consume nuts, seeds, and whole grains.",
        "Vitamin E or Omega-3 deficiency": "Include fish, nuts, and vegetable oils in your diet.",
        "Magnesium or Potassium deficiency": "Eat bananas, avocados, and nuts.",
    }

    results = []
    for symptom in symptoms:
        if symptom in deficiencies:
            deficiency = deficiencies[symptom]
            results.append((deficiency, recommendations[deficiency]))

    return results

# Streamlit UI
st.title("Smart Medical Check Program")
st.sidebar.header("Navigation")
option = st.sidebar.radio("Choose a function:", ["Find an Illness", "BMI Calculator", "Blood Pressure Check", "Vitamins & Minerals Test"])

# Illness diagnosis
if option == "Find an Illness":
    st.header("Symptom Checker")
    symptoms_input = st.text_input("Enter symptoms (comma-separated):")

    if st.button("Diagnose"):
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        illnesses, cures, tips = diagnose_illness(symptoms)

        if illnesses:
            st.subheader("Possible Illnesses:")
            for illness in illnesses:
                st.write(f"- {illness}")

            st.subheader("Cures:")
            for cure in cures:
                st.write(f"- {cure}")

            st.subheader("Tips:")
            for tip in tips:
                st.write(f"- {tip}")
        else:
            st.warning("No matching illnesses found.")

# BMI Calculator
elif option == "BMI Calculator":
    st.header("BMI Calculator")
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.5, format="%.2f")

    if st.button("Calculate BMI"):
        if height > 0:
            bmi, category = calculate_bmi(weight, height)
            st.success(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
        else:
            st.error("Height must be greater than 0.")

# Blood Pressure Check
elif option == "Blood Pressure Check":
    st.header("Blood Pressure Check")
    age = st.number_input("Enter your age:", min_value=1, max_value=120, step=1)
    bp = st.number_input("Enter your blood pressure (systolic):", min_value=50, max_value=200, step=1)

    if st.button("Check Blood Pressure"):
        bp_status, message = check_blood_pressure(bp, age)
        if bp_status == "Normal":
            st.success(message)
        else:
            st.warning(message)

            st.subheader("Tips to manage until you reach a hospital:")
            st.write("- Stay hydrated by drinking water.")
            st.write("- Rest in a calm, quiet environment.")
            st.write("- Avoid stressful activities.")

# Vitamins & Minerals Test
elif option == "Vitamins & Minerals Test":
    st.header("Vitamins and Minerals Test")
    symptoms_input = st.text_input("Enter symptoms (comma-separated):")

    if st.button("Check Deficiency"):
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        results = vitamins_and_minerals_test(symptoms)

        if results:
            st.subheader("Possible Deficiencies and Recommendations:")
            for deficiency, recommendation in results:
                st.write(f"- *Deficiency:* {deficiency}\n  *Recommendation:* {recommendation}")
        else:
            st.warning("No specific deficiencies detected.")