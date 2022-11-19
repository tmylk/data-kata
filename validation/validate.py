from dataclasses import dataclass
from typing import Optional

import pandas as pd
from pydantic import BaseModel, Field, validator


class House(BaseModel):
    YearBuilt: int
    Id: int
    Fireplaces: int
    FireplaceQu: Optional[str]
    Street: str
    FirstFlrSF: int = Field(alias="1stFlrSF")
    SecondFlrSF: int = Field(alias="2ndFlrSF")

    @validator("YearBuilt")
    def check_year_built(cls, v):
        assert (v > 1700) and (v < 1900), "Yearbuilt not in 1700-1900"
        return v


def read_csv(csv_file: str = "data/train.csv") -> pd.DataFrame:
    return pd.read_csv(
        csv_file,
        usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"],
    )
