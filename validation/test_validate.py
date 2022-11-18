from validate import House, read_csv


def test_csv_read():
    df = read_csv()
    assert len(df) == 1460


def test_columns():
    df = read_csv()
    assert set(df.columns.values) == set(
        ["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"]
    )


def test_create_house():
    house = House(YearBuilt=1800, Id=1, Fireplaces=0, FireplaceQu=None, Street="Sesame")
    assert house.YearBuilt == 1800
