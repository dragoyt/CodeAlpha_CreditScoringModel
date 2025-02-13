
---

# Credit Scoring Model with Streamlit

This project is a **credit scoring model** that predicts the creditworthiness of applicants based on features like income, debt, and credit history. The model is deployed as a web application using **Streamlit**, and all calculations are performed in **Indian Rupees (INR)**.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

The goal of this project is to build a machine learning model that predicts whether an applicant is creditworthy based on their financial profile. The model uses features such as:
- **Annual Income (INR)**
- **Total Debt (INR)**
- **Credit History** (poor, fair, good, excellent)
- **Debt-to-Income Ratio**

The model is deployed as a **Streamlit web application**, allowing users to input applicant details and receive a prediction in real-time.

---

## Features

- **Input Fields**: Users can input the applicant's annual income, total debt, and credit history.
- **Real-Time Prediction**: The app predicts whether the applicant is creditworthy and provides the probability of the prediction.
- **INR Support**: All calculations are performed in Indian Rupees (INR).
- **User-Friendly Interface**: Built with Streamlit for a simple and intuitive user experience.

---

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dragoyt/CodeAlpha_CreditScoringModel
   cd credit-scoring-model
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pre-Trained Model**:
   - Ensure you have the pre-trained model (`credit_scoring_model.joblib`) and preprocessor (`preprocessor.joblib`) in the project directory. If not, train the model using the provided notebook or script.

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

6. **Access the App**:
   Open your browser and go to `http://localhost:8501`.

---

## Usage

1. **Input Applicant Details**:
   - Use the sidebar to input the applicant's annual income, total debt, and credit history.
   - All values should be in INR.

2. **View Prediction**:
   - The app will display whether the applicant is creditworthy (`Creditworthy ✅` or `Not Creditworthy ❌`).
   - It will also show the probability of the prediction.

3. **Example Input**:
   - **Annual Income**: `1,000,000 INR`
   - **Total Debt**: `200,000 INR`
   - **Credit History**: `good`

4. **Example Output**:
   - **Prediction**: `Creditworthy ✅`
   - **Probability**: `0.85`

---

## File Structure

```
credit-scoring-model/
├── app.py                  # Streamlit application
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
├── preprocessor.joblib     # Preprocessor for input data
├── credit_scoring_model.joblib  # Pre-trained model
├── data/                   # Dataset used for training (if applicable)
├── notebooks/              # Jupyter notebooks for model development (if applicable)
└── scripts/                # Scripts for training and evaluation (if applicable)
```

---

## Deployment

To deploy this app for public use:
1. **Streamlit Sharing**:
   - Upload the project to GitHub.
   - Go to [Streamlit Sharing](https://share.streamlit.io/) and deploy the app by linking your GitHub repository.

2. **Heroku**:
   - Follow Heroku's guide for deploying Streamlit apps: [Deploy Streamlit on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).

3. **Docker**:
   - Containerize the app using Docker and deploy it to any cloud platform.

---

## Contributing

Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/).
- Model trained using [Scikit-learn](https://scikit-learn.org/) and [XGBoost](https://xgboost.ai/).

---
