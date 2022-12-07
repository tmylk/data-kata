- [x] read raw input data from data/train.csv into raw_housing
    - write failing test for row count in raw/schema.yml using dbt-expectations
    - use DBT seed command (this is against a [DBT best practice](https://docs.getdbt.com/docs/build/seeds) for loading dynamic data into DB, we are using it here just for concise tutorial )

- [ ] add a check for Id field unique and not null in raw_houses/schema.yml
  - comment: Unfortunately I don't know how to test this type validation actually works we can't expect a test to produce an exception or faiilure easily. I just did an ad-hoc test and decided to trust after that... :( I experimented with jinja unit tests but the mock data there doesn't go through the schema tests.


- [ ] staging column stg_houses reads data from the raw table and applies formatting checks. 
    - in staging/schema.yml write failing test for column names using dbt-expectations
    - make the test pass by only selecting the right columns
    - on green, think about refactoring. Would you like to rename fields to have more readable names? Do they have to be the same as CSV column names? Renaming in staging is a DBT best practice in the Do Not Repeat Yourself principle.
    - run `dbt build --full-refresh` to recreate the DB and run everything
    

- [ ] column data types validation
    -  run the test on command line using 'dbt test' or 'dbt test --store-failures' command
       - id you use 'dbt test --store-failures' then you can inspect the failures in db by using 'duckcli houses.duckdb'
       - you can also see what the test actually does by clicking on a link to complied code in the console, like  `compiled Code at target/compiled/houses/models/staging/schema.yml/dbt_expectations_expect_column_dfc73812841a97c03866cb28a5063a04.sql`
    -  see a test for Id column having data type integer in staging/schema.yml line 22 using dbt-expectations

    - add remaining column type tests
  
- [ ] Null values
  - how are null values marked in the CSV? It is NA word, not null
  - use NULLIF to convert the columns to nulls 

- [ ] when loading into staging, check the data format rule that FireplaceQuality has to be one of 'Ex', 'Gd', 'TA', 'Fa', 'Po', null
  - add the test to staging/schema.yml using dbt-expectations
  - use 'NA' to denote null in the list
  - check it passes using dbt test command

- [ ] First business rule. "If Fireplaces is greater than 0, then FireplaceQu is required." Don't load row into the houses prod table from staging stg_houses if the business rule is failed. 
    - See a regression unit test for creating a valid house in staging, and then checking it is copied to prod table in tests/unit_tests.sql It is using the clever dbt-testing library from Equal Experts
    - uncomment a failing test that creates two rows in staging - one valid and one invalid. And expects only one of them to pass to prod. 
    - see the nice error message running dbt test
    - Add another common table SQL expression in houses.sql to make the test pass


- [ ] validation YearBuilt
    - write a failing test in tests/unit_tests.sql for creating a House row with  yearbuilt 2000.
    - make it pass by creating another CTE in houses.sql only taking rows with YearBuilt value is between 1700 and 1900.
 

- [ ] validation firstfloor is at least one third of the 2nd floor
    
    - write a failing test for creating a House staging row with  1stFlrSF=10, 2ndFlrSF=50. Expect the house prod table to be empty.
    - make it pass. 

- [ ] check output
    - this is not required but you can see the output in terminal with `duckcli houses.duckdb` and `select * from houses`
    - expect to see 15 houses, just as in the pydantic solution






