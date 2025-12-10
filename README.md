# README

[GitHub repo ml-sandbox-non-production](https://github.com/pylabview/ml-sandbox-non-production)

## 1. Preping enviormant

```
$ git clone git@github.com:pylabview/ml-sandbox-non-production.git

$ cd ml-sandbox-non-production

$ uv python install 3.12

$ uv python pin 3.12

$ uv sync

$ uv run python -m ipykernel install \

  --user \

  --name python-playground-3-12-10 \

  --display-name "Python Playground Project (3.12.10)"

$ uv run jupyter lab
```



> Make sure Python Playground Project (3.12.10) is selected

## 2. Download raw dataset, unzipped and drop them in the data 📁

[Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

- [2019-Oct.csv.gz](https://data.rees46.com/datasets/marketplace/2019-Oct.csv.gz) (1.62Gb)
- [2019-Nov.csv.gz](https://data.rees46.com/datasets/marketplace/2019-Nov.csv.gz) (2.69Gb)
- [2019-Dec.csv.gz](https://data.rees46.com/datasets/marketplace/2019-Dec.csv.gz) (2.74Gb)
- [2020-Jan.csv.gz](https://data.rees46.com/datasets/marketplace/2020-Jan.csv.gz) (2.23Gb)
- [2020-Feb.csv.gz](https://data.rees46.com/datasets/marketplace/2020-Feb.csv.gz) (2.19Gb)
- [2020-Mar.csv.gz](https://data.rees46.com/datasets/marketplace/2020-Mar.csv.gz) (2.25Gb)
- [2020-Apr.csv.gz](https://data.rees46.com/datasets/marketplace/2020-Apr.csv.gz) (2.73Gb)

## 3. Run Jupyter Run Books

     - 🐍 config.py -> M2_ EDA V6_1.ipynb: This NB will do the raw CSV files conversion to parquet and the inital EDA
     - 🐍 configm3.py -> M3_ Add in some Machine Learning V5_1.ipynb: Here we are adding some ML model baselines
     - 🐍 configm4.py -> M4_Revise_and_Evaluate_ML_Model_V6_5.ipynb and  The Process Notebook.ipynb: ML Models selection and final process notebook 
     -  📁 Pictures_and_Diagrams 
    




