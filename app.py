
from flask import Flask, render_template, request

from model_pipeline import predict_heart_disease

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Collect the 13 Cleveland dataset features
        input_data = {
            "age": int(request.form["age"]),
            "sex": int(request.form["sex"]),
            "cp": int(request.form["cp"]),
            "trestbps": int(request.form["trestbps"]),
            "chol": int(request.form["chol"]),
            "fbs": int(request.form["fbs"]),
            "restecg": int(request.form["restecg"]),
            "thalach": int(request.form["thalach"]),
            "exang": int(request.form["exang"]),
            "oldpeak": float(request.form["oldpeak"]),
            "slope": int(request.form["slope"]),
            "ca": int(request.form["ca"]),
            "thal": int(request.form["thal"])
        }

        # Validate numerical ranges against the dataset
        numeric_ranges = {
            "age": (29, 77),
            "trestbps": (94, 200),
            "chol": (126, 564),
            "thalach": (71, 202),
            "oldpeak": (0, 6.2)
        }

        for feature, (minimum, maximum) in numeric_ranges.items():
            value = input_data[feature]

            if not minimum <= value <= maximum:
                return (
                    f"Invalid {feature}. "
                    f"Expected a value between {minimum} and {maximum}.",
                    400
                )

        # Validate categorical values
        valid_categories = {
            "sex": [0, 1],
            "cp": [1, 2, 3, 4],
            "fbs": [0, 1],
            "restecg": [0, 1, 2],
            "exang": [0, 1],
            "slope": [1, 2, 3],
            "ca": [0, 1, 2, 3],
            "thal": [3, 6, 7]
        }

        for feature, allowed_values in valid_categories.items():
            if input_data[feature] not in allowed_values:
                return f"Invalid value for {feature}.", 400


        # Get prediction and model probability
        prediction, probability = predict_heart_disease(input_data)

        if prediction == 1:
            prediction_label = "Disease recorded"
            result_color = "danger"
        else:
            prediction_label = "No disease recorded"
            result_color = "success"

        return render_template(
            "result.html",
            prediction_label=prediction_label,
            probability=probability,
            result_color=result_color
        )

    except (KeyError, ValueError):
        return "Invalid or missing input. Please check the form.", 400

    except Exception as error:
        app.logger.exception("Prediction failed")
        return "Unable to generate prediction. Please try again.", 500


if __name__ == "__main__":
    app.run(debug=True)
