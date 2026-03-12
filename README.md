# Telecom Plan Recommendation ML Project

This repository contains a machine learning project developed to recommend mobile plans (Smart or Ultra) for Megaline subscribers based on their usage behavior.

## Structure

```
telecom-plan-recommendation-ml/
├── data/
│   ├── raw/users_behavior.csv      # original dataset (ignored in Git)
│   └── processed/                  # cleaned/processed data (generated)
├── src/
│   ├── data.py                    # data loading and preprocessing functions
│   ├── models/                    # model training and persistence
│   ├── visualization/             # plotting helper utilities
│   └── config.py                  # configuration constants
├── notebooks/                     # explanatory notebooks and final report
│   └── telecom_plan_recommendation_model.ipynb
├── tests/                         # unit tests for modules
├── requirements.txt               # Python dependencies
├── .gitignore                     # files and folders to ignore
└── README.md
```

## Quickstart

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd telecom-plan-recommendation-ml
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Windows PowerShell: `venv\Scripts\Activate.ps1`)
   pip install -r requirements.txt
   ```

3. Run preprocessing and training script (if implemented):
   ```bash
   python src/models/train.py
   ```

4. View the notebook for detailed analysis:
   ```bash
   jupyter notebook notebooks/telecom_plan_recommendation_model.ipynb
   ```

## Results

- Best model: Random Forest
- Test accuracy: ~0.82
- Baseline accuracy: 0.50

## Contributing

Feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License.