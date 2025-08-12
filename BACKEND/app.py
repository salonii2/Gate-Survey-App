from flask import Flask, request, jsonify
import pickle
import json
import pandas as pd
import sklearn

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Load the trained model and metadata
# with open('https://github.com/Salonii2/a1-backend/blob/169eb132f0cf590985b2a96026971b2ada9eae1b/best_model.pkl', 'rb') as model_file:
with open('best_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model_metadata.json', 'r') as json_file:
    model_metadata = json.load(json_file)

expected_features = ['Height (ft)', 'Width (ft)', 'Material', 'Location', 'Use_Case', 
                     'Budget', 'Parking_Space', 'Cable_Layout', 'Storage_Space', 
                     'Security_Features', 'Climate_Suitability']
# Step 3: Define a prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON input from the user
        input_data = request.json
        
        # Convert input JSON to a DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Ensure the input data has the same columns as training data (excluding target variable)
        # expected_columns = model.named_steps['preprocessor'].transformers_[0][2] + model.named_steps['preprocessor'].transformers_[1][2]
        missing_cols = set(expected_features) - set(input_df.columns)
        
        if missing_cols:
            return jsonify({"error": f"Missing columns in input data: {missing_cols}"}), 400

        # Predict using the loaded model
        prediction = model.predict(input_df)[0]
        
        # Prepare response with prediction
        response = {
            'input': input_data,
            'predicted_opening_mechanism': prediction,
            'model_metadata': model_metadata
        }
        
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Step 4: Define a health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running"})

# Step 5: Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# {
#     {
#         "best_score": 0.857,
#         "test_score": 0.8455,
#         "training_score": 0.89725
#     },
#     "predicted_opening_mechanism": "Folding"
# }
