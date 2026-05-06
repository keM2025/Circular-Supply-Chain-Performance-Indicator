import pandas as pd
from src.config import DATA_PATH_SUPERSTORE, DATA_PATH_OLIST

def load_data():
    superstore = pd.read_excel(DATA_PATH_SUPERSTORE)
    olist = pd.read_excel(DATA_PATH_OLIST)

    print("Superstore:", superstore.shape)
    print("Olist:", olist.shape)

    return superstore, olist