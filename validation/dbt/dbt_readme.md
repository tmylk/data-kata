The task is modified slightly:

If a format rule changes, then stop the load of any data

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