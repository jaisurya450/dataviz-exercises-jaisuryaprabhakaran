# World Happiness Dashboard (2023)

Interactive Streamlit app displaying two charts:
1. Happiness rankings of the top countries (class-provided chart).
2. GDP contribution versus happiness score (additional scatter plot).

## Run locally

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

The dataset should be at `data/world_happiness_2023.csv` (World Happiness Report 2023, Kaggle).

## Deploy
Push `app.py`, `requirements.txt`, and `data/world_happiness_2023.csv` to a GitHub repository. Deploy with Streamlit Community Cloud using `app.py` as the main file.
