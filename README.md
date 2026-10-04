# 🏦 Lloyds Banking Group Project
### Customer Churn Prediction using Machine Learning

This project was completed as part of the **Lloyds Banking Group Job Simulation**. The goal was to analyze customer data, identify factors linked to customer churn, and build a machine learning solution to help identify customers who may be at risk of leaving the bank.

---

## 🎯 Business Problem

Customer churn can lead to **financial loss and reduced customer lifetime value** for a bank. The challenge is to identify potentially at-risk customers early enough to take retention action.

### 💡 My Solution

- Combined customer demographics, transaction history, customer service interactions, and online activity.
- Performed EDA, data preprocessing, and feature engineering.
- Built and compared multiple classification models.
- Evaluated models using **Accuracy, Precision, Recall, F1 Score, and ROC-AUC**.
- Prioritized **Recall**, as missing a genuine churner can be more costly than contacting some customers who would stay.

---

## 📊 Model Performance

Several machine learning algorithms were evaluated, with the following results:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| **XGBoost** | 22.5% | 20.6% | **97.56%** | 34.0% | 49.7% |
| Logistic Regression | 52.0% | 25.2% | 68.29% | **36.8%** | **60.6%** |
| Random Forest | 54.0% | 20.0% | 41.46% | 27.0% | 50.0% |
| Decision Tree | **74.0%** | 31.0% | 21.95% | 25.7% | 56.1% |
| KNN | 71.5% | 23.3% | 17.07% | 19.7% | 54.2% |

### 🏆 Model Selection

**XGBoost was selected for its 97.56% recall.**

The model successfully identified most actual churners, which fits the project's business objective of **minimizing missed potential churners**. Its lower precision means some customers who would remain were also flagged, so a **low-cost, automated retention strategy** is more suitable.

---

## 🔍 Key Findings

The most important predictive features included:

- **AvgTransactionValue**
- **TotalSpent**
- **MaritalStatus_Single**
- **LoginFrequency**
- **TransactionCount**
- **DaysSinceLastLogin**
- **Age**
- **Income Level**
- **InteractionCount**
- **Digital service usage**

---

## 💼 Business Recommendations

- Use the model to identify as many potential churners as possible.
- Use **low-cost automated advertisements & personalized messages** for customers flagged as at risk.
- Focus retention efforts on higher-risk customer groups.
- Encourage customers to use **online banking and website services** to improve engagement.
- Retrain the model with updated customer data over time.

This can help **Lloyds Banking Group reduce potential customer loss** while keeping retention costs under control through inexpensive automated campaigns.

---

## 🛠️ Skills & Tools

**Machine Learning:** XGBoost, Classification, Model Evaluation  
**Data Science:** EDA, Data Analysis, Feature Engineering, Data Preprocessing  
**Domain:** Banking, Finance, Customer Retention, Churn Analysis  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter, Streamlit

---

## 📚 What I Learned

- Function-based EDA and practical data analysis
- Feature engineering using multiple datasets
- Machine learning model development and comparison
- Hyperparameter tuning and model evaluation
- Understanding the **Precision–Recall trade-off**
- Translating ML results into practical business recommendations
- Applying data science concepts to the **banking and financial services domain**

---

## 📂 Project Structure

```text
Lloyds-Banking-Group-Project/
│
├── data/
│   ├── Customer_Churn_data.csv
│   └── Prepared_Data.csv
│
├── model/
│   ├── best_churn_model.pkl
│   └── feature_columns.pkl
│
├── notebook/
│   └── Analysis.ipynb
│
├── .gitignore 
├── app.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Project Takeaway

* This project helped me understand how machine learning can be applied to a real banking problem, from exploring customer data to building a churn prediction model and turning the results into practical retention strategies.
* The biggest takeaway was that a Data Science project is not only about building a model. It is also about understanding the business problem, selecting the right evaluation metric, and turning model predictions into useful business decisions.
* Through this project, I gained hands-on experience in EDA, data analysis, feature engineering, machine learning, model evaluation, and banking-focused business problem solving.