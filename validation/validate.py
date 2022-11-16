import pandas as pd


def read_and_validate(csv_file: str = "data/train.csv"):
    df = pd.read_csv(
        csv_file,
        usecols=["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"],
    )
    return df
