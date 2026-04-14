def generate_health_recommendations(input_data):
    """
    input_data: dict containing patient input values
    returns: list of personalized health recommendations
    """

    recommendations = []

    age = input_data.get("age", 0)
    systolic_bp = input_data.get("systolic_bp", 0)
    diastolic_bp = input_data.get("diastolic_bp", 0)
    cholesterol = input_data.get("cholesterol", 0)
    diabetes = input_data.get("diabetes", 0)
    smoker = input_data.get("smoker", 0)
    physical_activity = input_data.get("physical_activity", 0)
    family_history = input_data.get("family_history", 0)

    # -------- Blood Pressure --------
    if systolic_bp >= 140 or diastolic_bp >= 90:
        recommendations.append(
            "Reduce salt intake and monitor blood pressure regularly."
        )

    # -------- Cholesterol --------
    if cholesterol >= 240:
        recommendations.append(
            "Adopt a low-fat, heart-healthy diet and increase fiber intake."
        )

    # -------- Smoking --------
    if smoker == 1:
        recommendations.append(
            "Quit smoking to significantly reduce cardiovascular risk."
        )

    # -------- Diabetes --------
    if diabetes == 1:
        recommendations.append(
            "Maintain proper blood sugar control through diet, exercise, and medication if prescribed."
        )

    # -------- Physical Activity --------
    if physical_activity == 0:
        recommendations.append(
            "Engage in at least 30 minutes of moderate physical activity daily."
        )

    # -------- Age & Family History --------
    if age >= 50 or family_history == 1:
        recommendations.append(
            "Schedule regular cardiovascular health check-ups."
        )

    # -------- Default Message --------
    if not recommendations:
        recommendations.append(
            "Maintain your current healthy lifestyle and continue regular health monitoring."
        )

    return recommendations


# ------------------- TEST BLOCK -------------------
if __name__ == "__main__":

    sample_input = {
        "age": 48,
        "gender": 1,
        "systolic_bp": 132,
        "diastolic_bp": 85,
        "cholesterol": 215,
        "diabetes": 0,
        "smoker": 0,
        "physical_activity": 1,
        "family_history": 1
    }

    recs = generate_health_recommendations(sample_input)

    print("\nPersonalized Health Recommendations:")
    for r in recs:
        print("-", r)
