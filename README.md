# Diabetes Prediction Application

This Streamlit application predicts whether a patient has diabetes based on various health metrics. The prediction model (`best_model.pkl`) is trained on a dataset containing diagnostic measurements.

## Features

-   Predicts diabetes likelihood based on user input.
-   Provides prediction probability.
-   Simple and intuitive user interface.
-   Visually appealing design with custom CSS.

## Setup Instructions

Follow these steps to set up and run the application locally:

1.  **Navigate to the project directory:**

    ```bash
    cd "Diabetes_prediction"
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   **On Windows:**

        ```bash
        .\venv\Scripts\activate
        ```

    *   **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    The application will open in your web browser.

## Model Information

The prediction model (`best_model.pkl`) takes the following input features:

-   **Pregnancies:** Number of times pregnant.
-   **Glucose:** Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
-   **Blood Pressure:** Diastolic blood pressure (mm Hg).
-   **Skin Thickness:** Triceps skin fold thickness (mm).
-   **Insulin:** 2-Hour serum insulin (mu U/ml).
-   **BMI:** Body mass index (weight in kg/(height in m)^2).
-   **Diabetes Pedigree Function:** A function that scores likelihood of diabetes based on family history.
-   **Age:** Age in years.

The model outputs a binary prediction: 0 for Non-Diabetic and 1 for Diabetic, along with the probability of each outcome.