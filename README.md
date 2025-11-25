# Streaming-Platform-Content-Analysis-
Streaming Platform Content Analysis

This repository presents an end-to-end machine learning and NLP framework for analyzing content catalogs across Netflix, Hulu, Amazon Prime, and Disney+.
The project unifies fragmented streaming metadata, builds predictive models, extracts thematic patterns, and delivers insights through an interactive dashboard.

📌 Project Overview

Modern streaming platforms host thousands of titles with inconsistent metadata and varied catalog strategies. This project provides a structured, automated approach to understand that ecosystem:

Unified dataset across four platforms

Metadata cleaning and feature engineering

Machine learning models for predicting content type and platform

NLP topic modeling to uncover hidden themes

Streamlit dashboard for real-time insights

📁 Repository Structure
📂 Streaming-Platform-Content-Analysis
│── app.py                                    # Streamlit dashboard
│── merged_streaming_dataset.csv              # Final cleaned dataset
│── Predict_content_type_(Movies_vs_TV).ipynb # Content type model
│── Predict_platform.ipynb                    # Platform prediction model
│── Topic_modelling_using_descriptions.ipynb  # NLP topic modeling
│── best_classification_model Predict content.joblib   # Saved XGBoost model
│── best_model_Predict_platform.joblib        # Saved Random Forest model
│── README.md                                 # Project documentation

📊 Key Features & Results
1. Content Type Classification (Movie vs TV Show)

Model: XGBoost

Accuracy: 99.37%

Precision: 98.31%

Recall: 99.64%

F1-Score: 98.97%

Most important feature: duration_minutes

2. Platform Prediction Model

Model: Random Forest

Accuracy: 95%

Cross-validation Mean: 94.60%

Key predictive attributes:

description_length

release_year

duration_minutes

main_genre categories

country indicators

3. Topic Modeling (NMF + TF-IDF)

Extracted 8 dominant content themes, including:

International dramas

Crime and thriller clusters

Kids and family themes

Comedy and romance patterns

These themes capture deeper content structures beyond traditional metadata.

🧼 Data Preparation Pipeline

✔ Standardized column names
✔ Removed duplicates
✔ Filled missing metadata
✔ Created engineered features:

content_type

main_genre

duration_minutes

description_length

✔ One-hot encoded categorical features
✔ Combined text for NLP modeling

🧠 Technology Stack
Component	Technology
Machine Learning	XGBoost, Random Forest, Logistic Regression
NLP	TF-IDF, NMF, LDA, CountVectorizer
Dashboard	Streamlit
Data Prep & Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
📈 Analytics Pipeline Diagram

Download or embed the flowchart:

/mnt/data/A_flowchart_infographic_titled_"Analytics_Pipeline.png"


To embed in GitHub, paste:

![Analytics Pipeline](/mnt/data/A_flowchart_infographic_titled_"Analytics_Pipeline.png")

▶ How to Run the Dashboard

Install dependencies:

pip install -r requirements.txt


Run Streamlit:

streamlit run app.py

🎯 Conclusion

This project shows how structured metadata and natural language processing can uncover platform strategies, simplify content classification, and support data-driven decision making in the streaming domain.
It provides a fully operational framework for analysis, automation, and insight generation.
