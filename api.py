from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained pipeline
pipeline = joblib.load('dsp_bid_model.pkl')

# Define the Flask app
app = Flask(__name__)

# Define the expected feature names and types
expected_features = {
    "pub_id": str,
    "ad_unit_id": str,
    "ad_type_id": str,
    "platform_id": str,
    "country": str,
    "make": str,
    "model": str,
    "dsp_id": str,
    "tmax": float,
    "schain_length": float,
    "day_of_week": int,
    "hour_of_day": int
}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        input_data = request.get_json()

        # Validate input
        missing_features = [f for f in expected_features if f not in input_data]
        if missing_features:
            return jsonify({'error': f'Missing features: {missing_features}'}), 400

        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data])

        # Ensure columns are in the correct format
        for feature, dtype in expected_features.items():
            if feature in input_df:
                input_df[feature] = input_df[feature].astype(dtype)

        # Make predictions using the pipeline
        prediction = pipeline.predict(input_df)
        prediction_proba = pipeline.predict_proba(input_df)[:, 1]  # Get probability

        # Prepare the response
        response = {
            'prediction': int(prediction[0]),
            'probability': float(prediction_proba[0])
        }
        return jsonify(response)

    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
