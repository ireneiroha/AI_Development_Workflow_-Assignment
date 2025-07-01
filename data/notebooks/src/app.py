from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = {'readmitted': 1}
    return jsonify(prediction)

@app.route('/')
def home():
    return "Hospital Readmission Prediction API is running."

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)

