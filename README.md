# 🌍 EcoSmart Web Deployment

This repository contains the **web deployment prototype** of the **EcoSmart waste classification model**, part of the *EcoSmart project* developed during my Master’s thesis in Software Engineering at Constantine 2 University.

The goal of this deployment is to **test and demonstrate the ML model online**: users can upload an image of waste, and the system predicts the correct category (e.g., plastic, paper, metal, glass, organic, etc.) using deep learning.

---

## 🚀 Project Context

EcoSmart is an **AI-powered recycling system** that integrates:

* 🧠 **Machine Learning & Deep Learning** (CNN, XGBoost) for waste classification
* 📡 **IoT sensors** for smart bins (to monitor fill levels)
* 📱 **Mobile application** for user engagement, gamification, and eco-points
* ☁️ **Cloud & Web deployment** for accessibility and scalability

This repository focuses only on the **web deployment of the classification model** using **Flask**.

---

## 🎯 Features

* Upload an image of waste for classification
* ML model predicts the category of waste
* Simple, lightweight web interface for testing the trained CNN
* Flask backend serving predictions in real time

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **ML Frameworks:** TensorFlow / Keras, XGBoost
* **Frontend:** HTML, CSS (basic templates)
* **Environment:** Jupyter Notebook, Anaconda
* **Deployment:** Flask server

---

## 📂 Repository Structure

```
webDeployement/
│── static/              # CSS, images, assets
│── templates/           # HTML templates for the Flask app
│── model/               # Trained model files (CNN, XGBoost)
│── app.py               # Flask main application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Usage

1. Clone the repository

   ```bash
   git clone https://github.com/fadou4/webDeployement.git
   cd webDeployement
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app

   ```bash
   python app.py
   ```

5. Open your browser at **[http://127.0.0.1:5000](http://127.0.0.1:5000)** and test the waste classification.

---

## 📊 Results

* The CNN model achieved high accuracy for distinguishing recyclable categories.
* The web deployment demonstrates how the ML model can be **integrated into a real-world application**.
* This prototype is a proof of concept for the larger EcoSmart ecosystem (IoT smart bins + mobile app).

---
## 👩‍💻 Author

**Fadoua Ounissi**

* GitHub: [@fadou4](https://github.com/fadou4)
* LinkedIn: https://www.linkedin.com/in/fadoua-ounissi-a138b2381/
* Email: fadouaounissi.dev@gmail.com

---

## 🙏 Acknowledgements

* Supervisors & professors at Constantine 2 University
* Open-source libraries: TensorFlow, Flask, XGBoost, Pandas, etc.
* The EcoSmart project team & contributors

---
