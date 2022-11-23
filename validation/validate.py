from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

import numpy as np
import pandas as pd
from pydantic import BaseModel, Field, root_validator, validator


class FireplaceQualityEnum(str, Enum):
    Ex = "Ex"
    Gd = "Gd"
    TA = "TA"
    Fa = "Fa"
    Po = "Po"


class House(BaseModel):
    YearBuilt: int
    Id: int
    Fireplaces: int
    FireplaceQuality: Optional[FireplaceQualityEnum] = Field(alias="FireplaceQu")
    Street: str
    SecondFlrSF: int = Field(alias="2ndFlrSF")
    FirstFlrSF: int = Field(alias="1stFlrSF")

    @validator("YearBuilt")
    def check_year_built(cls, v):
        assert (v > 1700) and (v < 1900), "Yearbuilt not in 1700-1900"
        return v

    @validator("FirstFlrSF")
    def check_first_floor_at_least_third_of_second(cls, v, values, **kwargs):
        assert (
            3 * v >= values["SecondFlrSF"]
        ), "First floor must be at least one third of the 2nd floor"
        return v

    @validator("FireplaceQuality")
    def check_fireplace_quality(cls, v, values, **kwargs):
        if values["Fireplaces"] > 0:
            assert v is not None, "No fireplace quality while fireplaces exist"
        return v


class HouseList(BaseModel):
    houses: List[House]

    @root_validator(pre=True)
    def check_id_unique(cls, values):
        root_values = values.get("houses")
        value_set = set()
        for value in root_values:
            if value.Id in value_set:
                raise ValueError("Id should be unique")
            else:
                value_set.add(value.Id)
        return values


def read_csv(csv_file: str = "data/train.csv") -> pd.DataFrame:
    return pd.read_csv(
        csv_file,
        usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"],
    )


def convert_and_filter_to_valid_house_list(house_dicts: List[dict]) -> List[House]:
    house_list = []
    for house_dict in house_dicts:
        try:
            house = House(**house_dict)
            house_list.append(house)

        except ValueError:
            continue

    return house_list


def read_valid_house_list_from_csv(csv_file: str = "data/train.csv") -> HouseList:
    df = read_csv(csv_file=csv_file)
    # convert pandas float nan to None so that Pydantic Optional works for fireplace quality
    df = df.replace({np.nan: None})
    house_list = convert_and_filter_to_valid_house_list(df.to_dict("index").values())

    return house_list
