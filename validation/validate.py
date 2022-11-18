from enum import Enum
from typing import Any, List, Optional

import numpy as np
import pandas as pd
from pydantic import BaseModel, Field, ValidationError, root_validator, validator


class FireplaceQualityEnum(str, Enum):
    Ex = "Ex"
    Gd = "Gd"
    TA = "TA"
    Fa = "Fa"
    Po = "Po"


class House(BaseModel):
    Id: int
    Street: str
    YearBuilt: int
    Fireplaces: int
    FireplaceQuality: Optional[FireplaceQualityEnum] = Field(alias="FireplaceQu")
    FirstFloorSquareFootage: int = Field(alias="1stFlrSF")
    SecondFloorSquareFootage: int = Field(alias="2ndFlrSF")

    @validator("YearBuilt")
    def check_year_built(cls, v):
        assert (v > 1700) and (v < 2020), "Yearbuilt not in 1700-1900"

    @validator("SecondFloorSquareFootage")
    def check_second_floor_footage(cls, v, values, **kwargs):
        assert 3 * values["FirstFloorSquareFootage"] >= v, "Second floor bigger than the first"

    @validator("FireplaceQuality")
    def check_fireplace_quality(cls, v, values, **kwargs):
        if values["Fireplaces"] > 0:
            assert v, "No fireplace quality while fireplaces exist"


class HouseList(BaseModel):
    houses: List[House]

    @root_validator(pre=True)
    def check_id_unique(cls, values):
        root_values = values.get("houses")
        value_set = set()
        for value in root_values:
            if value.Id in value_set:
                raise ValueError(f"Duplicate Id")
            else:
                value_set.add(value.Id)
        return values


def read_and_validate(csv_file: str = "data/train.csv") -> HouseList:
    df = pd.read_csv(
        csv_file,
        usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"],
    )
    # News to convert pandas float nan to None so that Pydantic Optional works.
    df = df.replace({np.nan: None})
    houses = [House(**house_dict) for house_dict in df.to_dict("index").values()]
    house_list = HouseList(houses=houses)

    return house_list
