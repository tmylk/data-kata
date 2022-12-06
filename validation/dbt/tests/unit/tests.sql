
{{
    config(
        tags=['unit-test', 'no-db-dependency']
    )
}}


{% call dbt_unit_testing.test('houses', 'can create a valid house') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as '1stFlrSF', 50 as '2ndFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as '1stFlrSF', 50 as '2ndFlrSF'
  {% endcall %}
{% endcall %}

UNION ALL

{% call dbt_unit_testing.test('houses', 'invalid YearBuilt gets removed') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as '1stFlrSF', 50 as '2ndFlrSF'
    UNION ALL
    select 2 as id, 2000 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as '1stFlrSF', 50 as '2ndFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
  -- number 2 got removed.
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as '1stFlrSF', 50 as '2ndFlrSF'
  {% endcall %}
{% endcall %}
