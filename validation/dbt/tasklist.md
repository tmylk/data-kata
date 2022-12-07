- [x] read raw input data from data/train.csv into raw_housing
    - write failing test for row count in raw/schema.yml using dbt-expectations
    - use DBT seed command (this is against a [DBT best practice](https://docs.getdbt.com/docs/build/seeds) for loading dynamic data into DB, we are using it here just for concise tutorial )

- [ ] staging column stg_houses reads data from the raw table and applys formatting checks. 
    - in staging/schema.yml write failing test for column names using dbt-expectations
    - make the test pass by only selecting the right columns

- [ ] column data types validation
    -  run the test on command line using 'dbt test' or 'dbt test --store-failures' command
       - id you use 'dbt test --store-failures' then you can inspect the failures in db by using 'duckcli houses.duckdb'
       - you can also see what the test actually does by clicking on a link to complied code in the console, like  `compiled Code at target/compiled/houses/models/staging/schema.yml/dbt_expectations_expect_column_dfc73812841a97c03866cb28a5063a04.sql`
    -  see a test for Id column having data type integer in staging/schema.yml line 22 using dbt-expectations

    - add remaining column type tests
    - comment: Unfortunately I don't know how to test this type validation actually works we can't expect a test to produce an exception or faiilure easily. I just did an ad-hoc test and decided to trust DBT expectations after that... :( I experimented with jinja unit tests but the mock data there doesn't go through the dbt-expectations tests.

- [ ] when loading into staging, check the data format rule that FireplaceQuality has to be one of 'Ex', 'Gd', 'TA', 'Fa', 'Po', null
  - add the test to staging/schema.yml using dbt-expectations
  - use 'NA' to denote null in the list
  - check it passes using dbt test command

- [ ] First business rule. Don't load row into the houses prod table if the business rule is failed. 
    - Add a check that If Fireplaces is greater than 0, then FireplaceQu is required.
    - use dbt-expectations expect_column_values_to_be_in_set with row_condition for both cases - 0 and >0

- [ ] data object
    - write a failing test for creating a House object with  yearbuilt 1800
    - make it pass - create with no errors
    - one by one add Id=1, Street = 'Sesame', Fireplaces=0, FireplaceQu=None,  to the test and let it pass each time
    - once on green, think about refactoring. Would you like to rename fields to have more readable names? Do they have to be the same as CSV column names?
    

- [ ] validation YearBuilt
    - write a failing test for creating a House object with  yearbuilt 2000. It should return an error stating YearBuilt as the issue
    - make it pass. 

- [ ] Data object with first floor and second floor footage
    - failing test for creating House with 1stFlrSF=100, 
    -  Think of using an alias as the field as it starts with a not-a-letter
    - make it pass. 
    - Same for 2ndFlrSF=50.

- [ ] validation firstfloor is at least one third of the 2nd floor
    
    - write a failing test for creating a House object with  1stFlrSF=10, 2ndFlrSF=50. Expect a validation error.
    - make it pass. 


- [ ] validation FireplaceQuality is one of 'Ex', 'Gd', 'TA', 'Fa', 'Po', None
  - write a regression test for creating a House object with Fireplaces=5 and  fireplacequality being 'Ex'. Expect a pass  
  - write a failing test for creating a House object with Fireplaces=5 and  fireplacequality being 'OK'. Expect a validation error.
  - make it pass. 

- [ ] validation if Fireplaces is greater than 0, FireplaceQu is required.
   - write a failing test for creating a House object with  fireplacequality being empty while Fireplaces is 1
  - make it pass. Return a validation error
  - check can still create a House object with fireplacequality empty  empty while Fireplaces is 0

- [ ] create a HouseList class to hold multiple houses
    - write a failing test creating a list of two houses
    - make it pass 

- [ ] unique Id validation
    - write a failing test creating a list of two houses with same Id
    - make it pass - Return a validation error

- [ ] HouseList only of valid houses
    - write a failing test creating a list of two houses where one of them is invalid. Check it returns a list with only one valid house.
    - make it pass 

- [ ] HouseList only of valid houses from csv

    - write a failing test to read csv in data/train.csv and only return valid houses. can you assert on number of houses?
    - do you have an error for fireplacequality being NA? what does pandas use for the missing value? is it different to what pydantic expects as the missing value for FireplaceQuality? what is the best way to fix that? 







