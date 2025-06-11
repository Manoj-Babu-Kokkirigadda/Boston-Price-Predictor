from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_input = np.array(features).reshape(1, -1)
    prediction = model.predict(final_input)[0]
    return render_template('index.html', prediction_text=f'Estimated House Price: ${prediction:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
