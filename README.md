#  Car Price Prediction Web Application

## μLearn Epochs '26 – Day 9 Assignment

**Participant Name:** Emil Tom Joseph  
**MUID:** *emiltomjoseph@mulearn*

---

#  Project Overview

This project is a web-based **Car Price Prediction System** developed as part of the **μLearn Epochs '26 Bootcamp**. The application uses a **Random Forest Regressor** trained on the **CarDekho Used Car Dataset** to estimate the selling price of a used car based on user-provided vehicle details.

The model has been integrated into a **Streamlit** web application, allowing users to enter vehicle information and receive instant price predictions through an interactive interface.

---

#  Project Features

-  Interactive web application built with Streamlit
-  Machine Learning-based price prediction
-  Uses a trained Random Forest Regression model
-  Instant prediction based on user inputs
-  Clean and responsive user interface
-  Ready for online deployment

---

#  Dataset

**Dataset:** CarDekho Used Car Dataset

The dataset includes vehicle information such as:

- Vehicle Age
- Kilometers Driven
- Mileage
- Engine Capacity
- Maximum Power
- Number of Seats
- Brand
- Fuel Type
- Seller Type
- Transmission Type

These features are used to predict the selling price of a used car.

---

#  Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

#  Machine Learning Model

**Algorithm Used:**

- Random Forest Regressor

The trained model was exported using **Joblib** and integrated into the Streamlit application for real-time predictions.

---

#  Deployment Approach

The deployment process involved the following steps:

1. Trained the Machine Learning model using the CarDekho dataset.
2. Saved the trained model and preprocessing objects using Joblib.
3. Developed an interactive web interface using Streamlit.
4. Connected the web interface with the trained model.
5. Tested the application locally.
6. Deployed the application using **Streamlit Community Cloud**.

---

# 📸 Application Preview

> *(Add a screenshot after deployment.)*

```
assets/app_screenshot.png
```

---

#  Key Observations

- Vehicle age significantly affects the predicted selling price.
- Cars with lower mileage generally receive higher predicted values.
- Brand and fuel type influence resale price considerably.
- Random Forest provides stable and accurate predictions for this dataset.
- The web interface enables quick and user-friendly interaction with the model.

---

#  Challenges Faced

- Preparing the trained model for deployment.
- Ensuring the input features matched the training feature order.
- Handling preprocessing consistently between training and prediction.
- Managing Python package compatibility during local development.
- Integrating the saved model with the Streamlit interface.

---

#  Future Improvements

- Add support for more vehicle brands and models.
- Improve UI with charts and prediction confidence.
- Deploy using Docker for easier portability.
- Add model performance metrics to the application.
- Allow users to upload vehicle details from CSV files.
- Experiment with advanced regression algorithms such as XGBoost or LightGBM.

---

#  Live Demo

**Deployment Link:**

```
https://your-app-name.streamlit.app](https://car-price-prediction-epochs.streamlit.app/
```

---

#  Acknowledgements

This project was developed as part of the **μLearn Epochs '26 Bootcamp** to demonstrate the complete Machine Learning workflow—from model development to deployment as a real-world web application.

---
 **Thank you for visiting this project!**
