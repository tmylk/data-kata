# data-kata in DBT
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tmylk/data-kata/)

Coding exercise for improving Data skills

This repo is for a solution using DBT and DuckDB. For Pydantic, see another repo.

## Why DBT?

The idea is to code only in SQL as there are Data Analyts who work in SQL and, say, PowerBI and are not proficient in Python.

Curious to explore the third-party SQL unit-testing library https://github.com/EqualExperts/dbt-unit-testing/

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
 - If Fireplaces is greater than 0, FireplaceQu is required.
 - YearBuilt value is between 1700 and 1900.
 - firstfloor is at least one third of the 2nd floor

### Tasklist

For step-by-step guide with pydantic see [the tasklist]()./dbt/tasklist.md) 

For solution see Pull Request.



## Mob programming

To read about mob programming setup, read 

- [How to configure tech for mob programming](mob-programming.md)



### Setup

In Gitpod these commands run automatically. They are here for completeness

run commands:


python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
#install dbt-expectations and dbt-unit-tests
dbt deps 
dbt build