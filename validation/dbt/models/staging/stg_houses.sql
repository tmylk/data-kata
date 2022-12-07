with source as (

    select * from {{ ref('raw_houses') }}
),
renamed as (
    select *
    from source
)
select * from renamed