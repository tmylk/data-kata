
Read the data in train.csv and check:

 - id is unique
 - Street column is a string
 - YearBuilt minimal value is between 1700 and 1900.
 - FireplaceQuality - FireplaceQu - optional - nullable - enum values of 'Ex', 'Gd', 'TA', 'Fa', 'Po'. If Fireplaces is greater than 0, FireplaceQu is required.
 - firstfloor bigger than 2nd floor


Try it with several frameworks - pandas, pydantic, Great Expectations, Pandera, mage, DBT.


## Credit

Exercises taken from a much more extensive tutorial and talk by Natan Mish
https://github.com/NatanMish/data_validation/


## Data

Datasetis taken from the [House prices 
prediction competition on Kaggle](https://www.kaggle.com/competitions/home-data-for-ml-course/data). 
