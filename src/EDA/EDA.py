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

BASE_PATH = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = BASE_PATH / 'data' / 'raw'


def explore_raw_data(path: Path = RAW_DATA_PATH) -> None:

    logger.info("Entra en la función")

    if not path.exists():
        logger.warning("Directory %s does not exists", path)
        return 
    
    csv_files = list(path.glob("*.csv"))

    if not csv_files:
        logger.warning("No CSV files found in %s", path)

    for file in csv_files:

        logger.info("Reading file %s", file.name)

        try:

            df = pd.read_csv(file)

            logger.info(
                "Loaded %s | rows = %s | cols = %s",
                file.name,
                df.shape[0],
                df.shape[1]
            )

            df.info(verbose=True)

        except Exception:
            logger.exception("Error processing file: %s", file.name)
            raise

if __name__ == "__main__":
    print(BASE_PATH)
    explore_raw_data()
        