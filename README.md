# Telecom Plan Recommendation ML Project

This repository contains a machine learning classification project developed to recommend mobile plans (Smart or Ultra) for Megaline subscribers based on their monthly usage behavior.

The goal is to predict which modern plan is most suitable for a user based on features such as call frequency, call duration, number of messages, and internet usage.

---

## Project Overview

Mobile carrier Megaline discovered that many customers are still using legacy plans.  
To improve customer experience and encourage migration to newer plans, the company wants a model that recommends either the **Smart** or **Ultra** plan.

Several machine learning models were evaluated to determine which provides the most accurate predictions.

Models tested:

- Decision Tree
- Random Forest
- Logistic Regression

---

## Results

| Model | Accuracy |
|------|------|
| Decision Tree | ~0.79 |
| Random Forest | **~0.82** |
| Logistic Regression | ~0.74 |
| Baseline | ~0.69 |

The **Random Forest model** produced the best performance and exceeded the required accuracy threshold of **0.75**.

---

## Repository Structure

```
telecom-plan-recommendation-ml/
│
├── telecom_plan_recommendation_model.ipynb   # main analysis notebook
├── requirements.txt                          # Python dependencies
├── README.md                                 # project documentation
├── tests/                                    # optional testing scripts
└── data/                                     # dataset (not tracked in Git)
```

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

## How to Run

1. Clone the repository

```
git clone https://github.com/mrbutler35-wq/telecom-plan-recommendation-ml
cd telecom-plan-recommendation-ml
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Launch the notebook

```
jupyter notebook telecom_plan_recommendation_model.ipynb
```

---

## License

This project is licensed under the MIT License.
