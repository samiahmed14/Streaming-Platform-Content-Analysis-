# Streaming Platform Content Analysis

An end-to-end Machine Learning and Natural Language Processing framework for analyzing content catalogs across **Netflix**, **Hulu**, **Amazon Prime**, and **Disney+**.

This project unifies fragmented streaming metadata, builds predictive models, extracts thematic patterns, and delivers insights through an interactive **Streamlit** dashboard.

---

## 📌 Project Overview

Modern streaming platforms host thousands of titles with inconsistent metadata and varied catalog strategies. This project provides a structured and automated approach to understand that ecosystem.

**Core objectives:**
- Unify datasets across four major streaming platforms  
- Clean and standardize metadata  
- Engineer predictive and NLP-ready features  
- Build high-performing classification models  
- Discover latent content themes using topic modeling  
- Present insights through an interactive dashboard  

---

## 📁 Repository Structure

```

Streaming-Platform-Content-Analysis/
│
├── app.py                                     # Streamlit dashboard
├── merged_streaming_dataset.csv               # Final cleaned dataset
├── Predict_content_type_(Movies_vs_TV).ipynb  # Content type classification
├── Predict_platform.ipynb                     # Platform prediction model
├── Topic_modelling_using_descriptions.ipynb   # NLP topic modeling
├── best_classification_model_Predict_content.joblib
│                                              # Saved XGBoost model
├── best_model_Predict_platform.joblib         # Saved Random Forest model
└── README.md                                  # Project documentation

````

---

## 📊 Key Features and Results

### 1. Content Type Classification (Movie vs TV Show)

- **Model:** XGBoost  
- **Accuracy:** 99.37 percent  
- **Precision:** 98.31 percent  
- **Recall:** 99.64 percent  
- **F1 Score:** 98.97 percent  

**Most important feature:**  
- `duration_minutes`

---

### 2. Platform Prediction Model

- **Model:** Random Forest  
- **Accuracy:** 95 percent  
- **Cross-validation Mean Accuracy:** 94.60 percent  

**Key predictive attributes:**
- `description_length`  
- `release_year`  
- `duration_minutes`  
- `main_genre` categories  
- Country indicators  

---

### 3. Topic Modeling (NMF with TF-IDF)

- Extracted **8 dominant content themes**
- Captures latent patterns beyond structured metadata  

**Key themes include:**
- International dramas  
- Crime and thriller clusters  
- Kids and family content  
- Comedy and romance patterns  

---

## 🧼 Data Preparation Pipeline

**Cleaning and standardization steps:**
- Standardized column names  
- Removed duplicate entries  
- Handled missing metadata  

**Feature engineering:**
- `content_type`  
- `main_genre`  
- `duration_minutes`  
- `description_length`  

**Encoding and transformation:**
- One-hot encoding for categorical variables  
- Text aggregation for NLP pipelines  

---

## 🧠 Technology Stack

| Component | Technologies |
|---------|--------------|
| Machine Learning | XGBoost, Random Forest, Logistic Regression |
| NLP | TF-IDF, NMF, LDA, CountVectorizer |
| Dashboard | Streamlit |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |

---

## 📈 Analytics Pipeline Diagram

To embed the pipeline flowchart in GitHub:

```md
![Analytics Pipeline](/mnt/data/A_flowchart_infographic_titled_"Analytics_Pipeline.png")
````

---

## ▶️ How to Run the Dashboard

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Launch Streamlit application

```bash
streamlit run app.py
```

---

## 🎯 Conclusion

This project demonstrates how structured metadata combined with Natural Language Processing can uncover platform strategies, simplify content classification, and support data-driven decision making in the streaming ecosystem.

It provides a complete and extensible framework for:

* Content analytics
* Predictive modeling
* NLP-driven insights
* Interactive visualization

This repository is suitable for further research, production extension, or portfolio demonstration.

---
