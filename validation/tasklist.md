- [x] read csv
    - write failing test for row count
    - let it pass
    - write failing test for column names
    - make the test pass

- [x] data object
    - write a failing test for creating a House object with  yearbuilt 1800
    - make it pass - create with no errors
    - one by one add Id=1, Street = 'Sesame', Fireplaces=0, FireplaceQu=None,  to the test and let it pass each time
    - once on green, think about refactoring. Would you like to rename fields to have more readable names? Do they have to be the same as CSV column names?
    

- [x] validation YearBuilt
    - write a failing test for creating a House object with  yearbuilt 2000. It should return an error stating YearBuilt as the issue
    - make it pass. 

- [x] Data object with first floor and second floor footage
    - failing test for creating House with 1stFlrSF=100, 
    -  Think of using an alias as the field as it starts with a not-a-letter
    - make it pass. 
    - Same for 2ndFlrSF=50.

- [ ] validation firstfloor is at least one third of the 2nd floor
    - failing test for creating House with 1stFlrSF=100, 2ndFlrSF=50. Think of using an alias as the field as it starts with a not-a-letter
    - 
    - write a failing test for creating a House object with  firstfloor being a quarter of the 2nd floor. Expect a validation error.
    - make it pass. 


- [ ] validation FireplaceQuality is one of 'Ex', 'Gd', 'TA', 'Fa', 'Po', None
  - write a failing test for creating a House object with  fireplacequality being 'OK'. Expect a validation error.
  - make it pass. 

- [ ] validation if Fireplaces is greater than 0, FireplaceQu is required.
   - write a failing test for creating a House object with  fireplacequality being empty while Fireplaces is 1
  - make it pass. Return a validation error

- [ ] create a HouseList class to hold multiple houses
    - write a failing test creating a list of two houses
    - make it pass 

- [ ] unique Id validation
    - - write a failing test creating a list of two houses with same Id
    - make it pass - Return a validation error








