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
              "1stFlrSF",
              "2ndFlrSF"

    from source


),


fireplacequ_required as (

    select *

    from renamed
    where
    (Fireplaces > 0 and
    "FireplaceQu" is not null) 
    OR
    (Fireplaces == 0 and
    "FireplaceQu" is null) 



)

select * from fireplacequ_required

