with source as (
    
    {#-
    Normally we would select from the table here, but we are using seeds to load
    our data in this project
    #}
    select * from {{ ref('raw_houses') }}

),

null_instead_of_na as (

    select Id,
              "Street",
              "YearBuilt",
              "Fireplaces",
               NULLIF("FireplaceQu",'NA') as FireplaceQu,
              "1stFlrSF" ,
              "2ndFlrSF" 

    from source


),



renamed as (

    select "Id",
              "Street",
              "YearBuilt",
              "Fireplaces",
              "FireplaceQu",
              "1stFlrSF" as FirstFlrSF,
              "2ndFlrSF" as SecondFlrSF

    from null_instead_of_na


)

select * from renamed

