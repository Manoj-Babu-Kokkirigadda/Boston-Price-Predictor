
# Boston House Price Prediction using Linear Regression

This project predicts house prices in Boston using a Linear Regression model. A simple Flask web app is built to take user inputs and display the predicted house price.

# Project Structure

BostonHousePricePrediction/
model_training.ipynb        # Jupyter notebook for training the model
model.pkl                   # Trained model saved using pickle
app.py                      # Flask application
templates/index.html        # HTML page with custom CSS


## How It Works

1. **Model Training**
   - Dataset: `Boston Housing Dataset` from `sklearn.datasets`
   - Algorithm: Linear Regression
   - Features: 13 numerical inputs
   - Output: Estimated house price

2. **Web App (Flask)**
   - Accepts user input for each of the 13 features
   - Predicts house price using the trained model
   - Displays the result on the same page


## How to Run Locally

1. **Clone the repository**
   bash
   git clone https://github.com/yourusername/BostonHousePricePrediction.git
   cd BostonHousePricePrediction
   

2. **Install dependencies**
   bash
   pip install -r requirements.txt
   

3. **Run Flask app**
   bash
   python app.py
   

4. **Visit the app**
   Open your browser and go to: `http://127.0.0.1:5000/`

## Tech Stack

- Python
- Jupyter Notebook
- Scikit-Learn
- Flask
- HTML + CSS

## Features

- Trained regression model using real-world housing data
- Simple and intuitive UI with CSS styling
- Predicts housing price in real-time
- Localhost simulation + screenshot included


## Files to Submit

- model_training.ipynb
- app.py
- model.pkl
- templates/index.html
- README.md
- localhost_screenshot.png

## Author

**Manoj Babu Kokkirigadda**  
[GitHub](https://github.com/Manoj-Babu-Kokkirigadda)
