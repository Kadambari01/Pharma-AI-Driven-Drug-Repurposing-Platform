# 💊 Pharma AI-Driven Drug Repurposing Platform

An AI-powered web application that predicts new therapeutic uses for existing drugs using Machine Learning and Blockchain technology. The platform integrates biomedical datasets, applies predictive models, and provides a secure environment for sharing clinical trial information.

---

## 📌 Overview

Traditional drug discovery is expensive, time-consuming, and often takes over a decade before a drug reaches the market. This project focuses on **Drug Repurposing**, where existing approved drugs are analyzed to discover new therapeutic applications.

The platform leverages **Artificial Intelligence**, **Machine Learning**, and **Blockchain** to accelerate drug discovery while ensuring secure data sharing and transparency.

---

## 🚀 Features

- 🔹 Secure User Registration & Login
- 🔹 Biomedical Dataset Upload
- 🔹 Data Preprocessing
- 🔹 CNN-based Drug Prediction
- 🔹 Random Forest Classification
- 🔹 Drug–Disease Association Prediction
- 🔹 Clinical Trial Sharing
- 🔹 Blockchain-based Secure Data Storage
- 🔹 Interactive Web Interface

---

## 🏗️ System Architecture

The platform follows four major stages:

1. Data Collection
2. Data Preprocessing
3. AI Model Training
4. Drug Prediction & Blockchain Storage

---

## 🧠 Machine Learning Models

### Convolutional Neural Network (CNN)

- Feature Extraction
- Drug Pattern Learning
- Drug–Disease Prediction
- High Prediction Accuracy

### Random Forest

- Classification
- Ensemble Learning
- Robust Predictions
- Improved Reliability

---

## 🔐 Blockchain Integration

Blockchain technology is integrated to enhance security, transparency, and trust within the platform.

Key functionalities include:

- Secure User Authentication
- Smart Contract Deployment using Solidity
- Immutable Storage of Clinical Trial Information
- Transparent and Tamper-Proof Data Sharing
- Decentralized Record Management using Ethereum

---

## 🛠️ Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Django

### Machine Learning
- TensorFlow
- Scikit-learn
- NumPy
- Pandas
- Matplotlib

### Blockchain
- Solidity
- Truffle
- Ethereum (Local Development Network)

### Database
- SQLite3

### Development Tools
- Node.js
- Python IDE / VS Code

---

## 📂 Project Structure

```text
Pharma-AI-Driven-Drug-Repurposing-Platform
│
├── Dataset/
├── Drug/
├── DrugApp/
├── model/
├── hello-eth/
├── manage.py
├── requirements.txt
├── Drug.json
├── Drug.sol
├── datasetLink.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Project Setup

### Clone the repository

```bash
git clone https://github.com/Kadambari01/Pharma-AI-Driven-Drug-Repurposing-Platform.git
```

### Navigate to the project directory

```bash
cd Pharma-AI-Driven-Drug-Repurposing-Platform
```

### Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Follow the steps below to run the Pharma AI-Driven Drug Repurposing Platform.

### Step 1: Start the Local Ethereum Blockchain

Open **Node.js Command Prompt** and keep it open throughout the execution.

Navigate to the blockchain directory:

```text
hello-eth/
└── hello-eth/
    └── node_modules/
        └── .bin/
```

Run the `runblockchain.bat` file.

This will launch the **Truffle Development Console**.

---

### Step 2: Deploy the Smart Contract

In the Truffle console, execute:

```bash
migrate
```

Wait until the deployment completes successfully.

A successful deployment will display:

- Smart contract compiled successfully
- Network: `develop`
- Smart contract deployed
- Contract address generated
- Migration completed successfully

Keep this terminal running.

---

### Step 3: Start the Django Development Server

Open a **new Command Prompt**.

Navigate to the project root directory:

```bash
cd Pharma-AI-Driven-Drug-Repurposing-Platform
```

Run the Django server:

```bash
python manage.py runserver
```

If successful, you will see:

```text
Starting development server at:
http://127.0.0.1:8000/
```

---

### Step 4: Launch the Application

Open your browser and visit:

```text
http://127.0.0.1:8000/index.html
```

The Pharma AI-Driven Drug Repurposing Platform is now ready to use.

---

## 🔄 Execution Workflow

```text
Start Node.js Command Prompt
            │
            ▼
Run runblockchain.bat
            │
            ▼
Truffle Development Console
            │
            ▼
Execute: migrate
            │
            ▼
Open New Command Prompt
            │
            ▼
python manage.py runserver
            │
            ▼
Open Browser
            │
            ▼
http://127.0.0.1:8000/index.html
```

---

## 📊 Project Modules

- User Registration
- User Login
- Data Acquisition
- Data Preprocessing
- CNN Model Training
- Random Forest Model Training
- Drug–Disease Prediction
- Clinical Trial Sharing
- Trial Viewing

---

## 🎯 Objectives

- Reduce drug discovery time and development cost.
- Predict new therapeutic uses for existing drugs.
- Improve prediction accuracy using AI and Machine Learning.
- Secure biomedical data using Blockchain technology.
- Support scalable and reliable pharmaceutical research.

---

## 📈 Results

The proposed AI-Driven Drug Repurposing Platform was successfully implemented and tested using biomedical datasets. The system integrates Machine Learning and Blockchain technologies to predict potential drug–disease associations while ensuring secure data management.

Key achievements include:

- Faster identification of potential drug candidates.
- Improved prediction accuracy using CNN and Random Forest.
- Secure blockchain-based storage of clinical trial information.
- Transparent and tamper-proof data sharing.
- Reliable AI-assisted decision support for researchers.

---

## 🔮 Future Enhancements

- Explainable AI (XAI)
- Graph Neural Networks (GNN)
- Real-Time Biomedical APIs
- Cloud Deployment
- Electronic Health Record (EHR) Integration
- Personalized Medicine Support

---

## 📚 References

- Nature Biotechnology
- Bioinformatics
- Briefings in Bioinformatics
- Nature Reviews Drug Discovery
- Scientific Reports

---

