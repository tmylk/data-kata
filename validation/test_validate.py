from pydantic import ValidationError
from validate import House, HouseList, read_csv


def test_csv_read():
    df = read_csv()
    assert len(df) == 1460


def test_columns():
    df = read_csv()
    assert set(df.columns.values) == set(
        ["Id", "Street", "YearBuilt", "Fireplaces", "FireplaceQu", "1stFlrSF", "2ndFlrSF"]
    )


def create_house():
    d = {
        "YearBuilt": 1800,
        "Id": 1,
        "Fireplaces": 0,
        "FireplaceQu": None,
        "Street": "Sesame",
        "1stFlrSF": 100,
        "2ndFlrSF": 50,
    }

    return House(**d)


def test_create_house_YearBuilt():
    house = create_house()
    assert house.YearBuilt == 1800


def test_create_house_id():
    house = create_house()

    assert house.Id == 1


def test_create_house_Fireplaces():
    house = create_house()
    assert house.Fireplaces == 0


def test_create_house_FireplaceQu():
    house = create_house()
    assert house.FireplaceQuality is None


def test_create_house_Street():
    house = create_house()
    assert house.Street == "Sesame"


def test_YearBuilt_error():
    try:
        d = {
            "YearBuilt": 2000,
            "Id": 1,
            "Fireplaces": 0,
            "FireplaceQu": None,
            "Street": "Sesame",
            "1stFlrSF": 100,
            "2ndFlrSF": 50,
        }
        house = House(**d)
        assert False, "Expect error"

    except ValidationError as e:

        print(f"Bad data: {e.errors()}")
        assert e.errors() == [
            {"loc": ("YearBuilt",), "msg": "Yearbuilt not in 1700-1900", "type": "assertion_error"}
        ]


def test_create_house_FirstFlrSF():
    house = create_house()
    assert house.FirstFlrSF == 100


def test_create_house_SecondFlrSF():
    house = create_house()
    assert house.SecondFlrSF == 50


def test_FirstFloor_SecondFloor_error():
    try:
        d = {
            "YearBuilt": 1800,
            "Id": 1,
            "Fireplaces": 0,
            "FireplaceQu": None,
            "Street": "Sesame",
            "1stFlrSF": 10,
            "2ndFlrSF": 50,
        }
        house = House(**d)
        assert False, "Expect error"

    except ValidationError as e:

        print(f"Bad data: {e.errors()}")
        assert e.errors() == [
            {
                "loc": ("1stFlrSF",),
                "msg": "First floor must be at least one third of the 2nd floor",
                "type": "assertion_error",
            }
        ]


def test_FireplaceQuality_Ex():

    d = {
        "YearBuilt": 1800,
        "Id": 1,
        "Fireplaces": 5,
        "FireplaceQu": "Ex",
        "Street": "Sesame",
        "1stFlrSF": 100,
        "2ndFlrSF": 50,
    }
    house = House(**d)
    assert house.FireplaceQuality == "Ex"


def test_FireplaceQuality_enum_error():
    try:
        d = {
            "YearBuilt": 1800,
            "Id": 1,
            "Fireplaces": 5,
            "FireplaceQu": "OK",
            "Street": "Sesame",
            "1stFlrSF": 100,
            "2ndFlrSF": 50,
        }
        house = House(**d)
        assert False, "Expect error"

    except ValidationError as e:

        print(f"Bad data: {e.errors()}")
        errors = e.errors()[0]

        assert errors["loc"] == ("FireplaceQu",)
        assert (
            errors["msg"]
            == "value is not a valid enumeration member; permitted: 'Ex', 'Gd', 'TA', 'Fa', 'Po'"
        )
        assert errors["type"] == "type_error.enum"


def test_FireplaceQuality_missing_error():
    try:
        d = {
            "YearBuilt": 1800,
            "Id": 1,
            "Fireplaces": 5,
            "FireplaceQu": None,
            "Street": "Sesame",
            "1stFlrSF": 100,
            "2ndFlrSF": 50,
        }
        house = House(**d)
        assert False, "Expect error"

    except ValidationError as e:

        print(f"Bad data: {e.errors()}")
        errors = e.errors()[0]

        assert errors["loc"] == ("FireplaceQu",)
        assert errors["msg"] == "No fireplace quality while fireplaces exist"
        assert errors["type"] == "assertion_error"


def test_house_list():

    d_house_one = {
        "YearBuilt": 1800,
        "Id": 1,
        "Fireplaces": 0,
        "FireplaceQu": None,
        "Street": "Sesame",
        "1stFlrSF": 100,
        "2ndFlrSF": 50,
    }
    house_one = House(**d_house_one)

    d_house_two = {
        "YearBuilt": 1800,
        "Id": 1,
        "Fireplaces": 5,
        "FireplaceQu": "Ex",
        "Street": "Elm",
        "1stFlrSF": 100,
        "2ndFlrSF": 50,
    }
    house_two = House(**d_house_two)

    house_list = HouseList([house_one, house_two])
    assert len(house_list.houses) == 2
