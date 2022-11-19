- [x] read csv
    - write failing test for row count
    - let it pass
    - write failing test for column names
    - make the test pass

- [x] data object
    - write a failing test for creating a House object with  yearbuilt 1800
    - make it pass - create with no errors
    - one by one add Id=1, Street = 'Sesame', Fireplaces=0, FireplaceQu=None, 1stFlrSF=100, 2ndFlrSF=50 to the test and let it pass each time
    

- [x] validation YearBuilt
    - write a failing test for creating a House object with  yearbuilt 2000. It should return an error stating YearBuilt as the issue
    - make it pass. 

- [ ] validation firstfloor is at least one third of the 2nd floor
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








