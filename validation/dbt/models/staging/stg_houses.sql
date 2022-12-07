with source as (
    
    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('raw_houses') }}

),


renamed as (

    select "Id",
              "Street",
              "YearBuilt",
              "Fireplaces",
              "FireplaceQu",
              "1stFlrSF" as FirstFlrSF,
              "2ndFlrSF" as SecondFlrSF

    from source


)

select * from renamed

