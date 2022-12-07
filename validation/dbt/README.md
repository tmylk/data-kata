# data-kata in DBT
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tmylk/data-kata/)

Coding exercise for improving Data skills

This repo is for a solution using DBT and DuckDB. For Pydantic, see another repo.

## Exercise

Load only valid rows from 'data/train.csv' 

Only read these columns = ['Id','Street','YearBuilt','Fireplaces', 'FireplaceQu','1stFlrSF', '2ndFlrSF']


If a format rule changes, then stop the load of any data and ouput the error.

Format rules (abort load):
 - id is int and unique
 - Street column is a string
 - YearBuilt is a int
 - firstfloor and second floor square feet are numerical
 - FireplaceQuality - FireplaceQu is one of 'Ex', 'Gd', 'TA', 'Fa', 'Po'. 
 
 
If a business rule fails then skip this row and continue the load

Business rules (skip record)
 - firstfloor is at least one third of the 2nd floor
 - If Fireplaces is greater than 0, FireplaceQu is required.

### Tasklist

For step-by-step guide with pydantic see [the tasklist]()./pydantic/tasklist.md) and files in pydantic/test_validate.py, pydandti/validate.py

For solutions see Pull Requests.

### Setup

In Gitpod these commands run automatically. They are here for completeness

run commands:


python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
#install dbt-expectations
dbt deps 
dbt build