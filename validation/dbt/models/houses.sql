with source as (
    
    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('stg_houses') }}

),


renamed as (

    select "Id",
              "Street",
              "YearBuilt",
              "Fireplaces",
              "FireplaceQu",
              FirstFlrSF,
              SecondFlrSF

    from source


),


FireplaceQu_required as (

    select *

    from renamed
    where
    (Fireplaces > 0 and
    FireplaceQu is not null) 
    OR
    (Fireplaces == 0 and
    FireplaceQu is null) 



),

YearBuilt_range as (

    select *

    from FireplaceQu_required
    where
    (YearBuilt > 1700 and
    YearBuilt < 1900) 



),

'1stFloor2ndFloorSF_check_passed' as (

    select *

    from YearBuilt_range
    where
    FirstFlrSF  > SecondFlrSF/3



)


select * from '1stFloor2ndFloorSF_check_passed'

