## Project Name & Pitch

Multiple Disease Prediction (Streamlit)

An interactive Streamlit app that predicts likelihood of three conditions — Diabetes, Heart Disease, and Parkinson's — from user-provided clinical inputs using pre-trained scikit-learn models.

## Project Status

This project is functional and usable as an MVP. Users can input features for each condition and receive model predictions instantly. Future iterations may improve input validation, feature scaling consistency, and model explainability.


## Installation and Setup Instructions

Clone this repository. You will need Python 3.9–3.11 installed on your machine.

Recommended: create and activate a virtual environment.

Installation:

```
pip install -r requirements.txt
```

To Start App (Streamlit):

```
streamlit run main.py
```

To Visit App:

Open your browser to `http://localhost:8501`

Or visit the public deployment: [multiplediseasepredictionweb streamlit app](https://multiplediseasepredictionweb-dp5capykxcxojfjadmansm.streamlit.app/)

Notes:
- The app loads three pre-trained models from files in the repo: `trained_model (1).sav` (diabetes), `heart_model.sav`, and `parkinsons_model.sav`.
- If deploying (e.g., on Heroku), `Procfile`, `runtime.txt`, and `setup.sh` are included to assist. Ensure environment matches `requirements.txt`.

## Reflection

- What was the context for this project?
  - A small end-to-end demo app to showcase multiple disease predictions in one UI, using classic ML models served locally via Streamlit.

- What did you set out to build?
  - A single-page experience with a sidebar to switch between three predictors. Each page collects relevant features and returns a binary prediction.

- Why was this project challenging and a good learning experience?
  - Harmonizing distinct feature sets and UX flows within one interface.
  - Ensuring model artifacts load reliably across environments and that numeric inputs are sanitized before inference.

- What were some unexpected obstacles?
  - Managing feature order consistency between training and inference.
  - Handling string-to-float conversion for all inputs and avoiding crashes from empty/invalid fields.

- What tools did you use and why?
  - Streamlit: rapid prototyping, simple UI for data apps without heavy frontend work.
  - scikit-learn: reliable classic ML library for tabular models.
  - pickle: quick-and-simple model serialization for demos.
  - streamlit-option-menu: convenient sidebar navigation.

In future iterations, I plan to add input validators, consistent scaling with `StandardScaler` persisted from training, and lightweight model interpretability (e.g., feature importances or SHAP for tree-based models).

---

Template format referenced: [Personal project README template](https://gist.github.com/martensonbj/6bf2ec2ed55f5be723415ea73c4557c4)