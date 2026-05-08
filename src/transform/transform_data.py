import pandas as pd

from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)

BASE_PATH = Path(__name__).resolve().parents[1]
RAW_DATA_PATH = BASE_PATH / 'data' / 'raw'

def default_transform(df: pd.DataFrame) -> pd.DataFrame:

    logger.info("There is no specific transformation for this data")
    
    return df

def transform_categories(df: pd.DataFrame) -> pd.DataFrame:
    
    logger.info("Applying specific transformations to ecommerce_categories.csv")

    df_clean = df.copy()
    df_clean['parent_category_id'] = df_clean["parent_category_id"].fillna(0) # Fill empty values with 0 to express that they have no parent_category_id

    empty_rows = df['parent_category_id'].isnull().sum()

    logging.info("File modifed")

    return df_clean

def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    
    logger.info("Applying specific transformations to ecommerce_categories.csv")
    
    df_clean = df.copy()
    df_clean['notes'] = df_clean['notes'].fillna('No note')

    logger.info("File modified")

    return df_clean

def apply_transform():
    pass