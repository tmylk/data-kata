from dataclasses import dataclass

import pandas as pd


@dataclass
class House:
    YearBuilt: int
    Id: int
    Fireplaces: int
    FireplaceQu: str
    Street: str


def read_csv(csv_file: str = "data/train.csv") -> pd.DataFrame:
    return pd.read_csv(
        csv_file,
        usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"],
    )
