---

## Car Price Prediction Using Machine Learning

This project is a machine learning-based web application that predicts the price of a car based on its specifications such as engine size, horsepower, fuel type, and more. It uses a trained Random Forest Regressor model and is deployed via a simple Streamlit interface.

---

### Features

* Predict car prices based on input features
* Interactive and user-friendly web interface using Streamlit
* Machine learning model trained on real-world car dataset
* Supports prediction in **Indian Rupees (INR)**

---

### Dataset

The dataset includes various attributes of cars such as:

* Make (Car Brand)
* Fuel Type
* Aspiration
* Number of Doors
* Body Style
* Drive Type
* Engine Location
* Wheelbase, Length, Width, Height
* Engine Size, Horsepower, RPM
* City and Highway Mileage
* Price (Target Variable)

**Source**: A modified version of the UCI Automobile dataset.

---

### Technologies Used

* Python
* pandas, numpy, scikit-learn
* Random Forest Regressor
* joblib (for model serialization)
* Streamlit (for web deployment)

---

### How to Run Locally

#### 1. Clone the Repository

```bash
mkdir car-price-prediction
cd car-price-prediction
git clone https://github.com/Deepan-CodeBuster/Car-Price-Prediction.git
```

#### 2. Install Dependencies

Create a virtual environment (optional but recommended), then:

```bash
pip install -r requirements.txt
```

#### 3. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

### Project Files

* `app.py` – Streamlit app for prediction
* `model_train.ipynb` – Model training Code 
* `car_price_model.pkl` – Trained Random Forest model
* `scaler.pkl` – Trained StandardScaler for input preprocessing
* `CarPrice_Assignment.csv` – Dataset used for training
* `requirements.txt` – Python dependencies
* `README.md` – Project documentation

---

### Model Training

If you want to retrain the model:

1. Use the dataset (`CarPrice_Assignment.csv`)
2. Run the training script (you can create a separate `model_train.ipynb`)
3. Save the model and scaler using `joblib`

Example:

```python
joblib.dump(model, 'car_price_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

---

### Price Conversion

The model predicts price in USD. The app converts it to INR using a fixed rate (e.g., 1 USD = 83 INR). You can adjust the rate in the `app.py` file.

---

### License

This project is for educational and learning purposes.

---

