
Predictive Maintenance ML Pipeline

"Kaggle" (https://road-to-kaggle-grandmaster.vercel.app/api/simple/{juanclopezdec})
"Python" (https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
"Scikit-Learn" (https://img.shields.io/badge/Scikit_Learn-Machine_Learning-F7931E?style=flat-square&logo=scikit-learn)
"Pandas" (https://img.shields.io/badge/Pandas-Data_Processing-150458?style=flat-square&logo=pandas)
"Streamlit" (https://img.shields.io/badge/Streamlit-Web_Deployment-FF4B4B?style=flat-square&logo=streamlit)

1. Project Description

An end-to-end predictive system designed to anticipate critical mechanical failures in industrial CNC machinery by analyzing real-time IIoT sensor telemetry.

The project addresses the high operational cost of unplanned downtime in manufacturing lines by enabling the transition from a reactive maintenance model to a condition-based maintenance (CBM) approach driven by data.

«[!IMPORTANT]
For version control and confidentiality purposes, the original dataset is not included in this repository. To reproduce the training process from the Notebook, download the "AI4I 2020 Predictive Maintenance Dataset" and place it in the "data/raw/" directory.»

2. Analytical Impact

* Downtime Optimization: The system achieved a 69% early failure detection rate (Sensitivity/Recall) for critical industrial milling machine failures, addressing an asymmetric error margin through the implementation of a class-weighted Random Forest algorithm using Scikit-Learn.

* Reliability Diagnostics: Operational accuracy was improved, achieving 70% precision in maintenance alerts by applying variance standardization ("StandardScaler") to raw thermodynamic and torque measurements.

* Operational Deployment: Access to the mathematical inference engine was simplified, reducing manual diagnostic time to milliseconds through the development of a reactive web interface using Streamlit and the serialization of machine learning artifacts with Joblib.

3. Technology Stack

Technology| Version| Role in the Architecture
Python| 3.10+| Core programming language for script development and the data pipeline.
Scikit-Learn| 1.2+| Mathematical standardization, algorithmic modeling, and statistical evaluation.
Pandas| 2.0+| Multi-source data ingestion, tabular data manipulation, and feature engineering.
Streamlit| 1.20+| Declarative framework for building and deploying the analytical frontend.
Joblib| 1.3+| Persistence and serialization of machine learning models to disk.

4. Project Structure

predictive-maintenance-ml-pipeline/
├── app/
│   └── app.py                  # User interface and inference engine (Streamlit)
├── data/
│   ├── processed/              # (Ignored by Git) Directory for cleaned data
│   │   └── .gitkeep
│   └── raw/                    # (Ignored by Git) Original dataset
│       └── .gitkeep
├── models/
│   ├── rf_model.joblib         # Exported machine learning model
│   └── scaler.joblib           # Statistical preprocessing artifact
├── notebooks/
│   └── 01_eda_and_cleaning.ipynb # EDA, validation, and model training
├── venv/                       # Isolated virtual environment
├── .gitignore
├── requirements.txt            # Strict dependencies for reproducibility
├── report.md                   # Qualitative analysis of results
└── README.md

5. Operational Workflow

The system architecture abstracts the statistical complexity behind a structured linear inference cycle:

graph TD
    A[Plant Operator] -->|Telemetry Input| B(Streamlit UI)
    B -->|Engineered Features| C{Selected Model Pipeline}
    C --> D[Failure Probability or Torque Prediction]

«[!TIP]
Local Execution: Place the AI4I dataset at `data/raw/ai4i2020.csv`, install dependencies from `requirements.txt`, then run these commands from the repository root:

`python -m app.train_models`

`python -m streamlit run app/app.py`»

6. Documentation and Business Reports

The ultimate goal of the mathematical modeling is to support operational decision-making. For a detailed breakdown of the technical findings, the business justification based on the confusion matrix, and the operational action plan, refer to the attached management documentation:

* "Executive Report: Implementation of Predictive Maintenance in CNC Machinery" (report.md)

* "Interactive Notebook available on Kaggle" (https://www.kaggle.com/code/juanclopezdec/iiot-cnc-predictive-maintenance-random-forest)

---

## PBL 1 & 2 Extension (Machine Learning Course)

* `notebooks/02_pbl1_ml_analysis.ipynb`: full ML analysis (EDA, linear/Bayesian/kernel regression & classification, **Unsupervised Clustering**, **Hidden Markov Model (HMM)**, and **Ensemble Learning**), executed with outputs and plots.
* `app/model_pipeline.py` & `app/app.py`: interactive Streamlit dashboard and pipeline supporting Classification, Regression, Clustering (`K-Means`, `GMM/EM`), Hidden Markov Model (`GaussianHMMClassifier` with Baum-Welch EM & Viterbi decoding), and Ensemble Learning (`Random Forest`, `Gradient Boosting`, `AdaBoost`, `Stacking`).
* `PBL1_report.md`: written summary report covering all implemented paradigms.
* `data/processed/regression_results.csv`, `classification_results.csv`, `clustering_results.csv`, `hmm_results.csv`: quantitative evaluation tables.
* Dataset expected at `data/raw/ai4i2020.csv`.
