# 🚲 Bike Price Prediction

A Machine Learning project that predicts the selling price of used bikes based on various features such as brand, model, year, kilometers driven, ownership details, and other specifications.

## 📌 Project Overview

Buying or selling a used bike often involves uncertainty regarding its fair market value. This project uses Machine Learning techniques to analyze historical bike data and predict an estimated selling price.

The goal is to help buyers and sellers make informed decisions by providing accurate price predictions.

---

## 🚀 Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Model Training
* Model Evaluation and Performance Analysis
* Price Prediction for Used Bikes
* Visualization of Important Insights

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Jupyter Notebook

---

## 📂 Project Structure

```bash
bike-price-prediction/
│
├── Bike_Price_Prediction.ipynb
├── dataset.csv
├── README.md
├── requirements.txt
└── model.pkl
```

---

## 📊 Dataset

The dataset contains information related to used bikes, including:

* Brand
* Model
* Year
* Kilometers Driven
* Owner Type
* Engine Capacity
* Fuel Type
* Selling Price (Target Variable)

---

## ⚙️ Workflow

### 1. Data Collection

Collected historical bike sales data.

### 2. Data Preprocessing

* Handling missing values
* Removing duplicates
* Encoding categorical variables
* Feature scaling

### 3. Exploratory Data Analysis

* Distribution analysis
* Correlation analysis
* Feature importance analysis

### 4. Model Building

Different regression models were tested:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

### 5. Model Evaluation

Performance was evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

---

## 📈 Results

The trained model successfully predicts the selling price of used bikes with good accuracy.

Example Prediction:

| Feature         | Value   |
| --------------- | ------- |
| Brand           | Honda   |
| Year            | 2020    |
| KM Driven       | 18,000  |
| Owner           | First   |
| Predicted Price | ₹65,000 |

---

## 📷 Visualizations

The project includes:

* Price Distribution
* Brand-wise Analysis
* Correlation Heatmap
* Feature Importance Charts

---

## 🎯 Future Improvements

* Deploy the model using Streamlit
* Add real-time bike valuation
* Improve accuracy with advanced ensemble models
* Integrate with a web application

---

## 👨‍💻 Author

**Vaidik Khandelwal**

* GitHub: https://github.com/Vaidikkh
* LinkedIn: https://www.linkedin.com/in/vaidik-kh/

---

## ⭐ If you found this project useful, consider giving it a star!
