
{{
    config(
        tags=['unit-test', 'no-db-dependency']
    )
}}


{% call dbt_unit_testing.test('houses', 'can create a valid house') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as 'FirstFlrSF', 50 as 'SecondFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as 'FirstFlrSF', 50 as 'SecondFlrSF'
  {% endcall %}
{% endcall %}

UNION ALL

{% call dbt_unit_testing.test('houses', 'missing fireplace quality') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 1800 as YearBuilt, 1 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as 'FirstFlrSF', 50 as 'SecondFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
    select null::numeric as id, null::numeric as YearBuilt,  null::numeric as Fireplaces, null as FireplaceQu, null as Street, null::numeric as 'FirstFlrSF', null::numeric  as 'SecondFlrSF'  where false
  {% endcall %}
{% endcall %}

UNION ALL

{% call dbt_unit_testing.test('houses', 'invalid YearBuilt') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 2000 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 100 as 'FirstFlrSF', 50 as 'SecondFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
    select null::numeric as id, null::numeric as YearBuilt,  null::numeric as Fireplaces, null as FireplaceQu, null as Street, null::numeric as 'FirstFlrSF', null::numeric  as 'SecondFlrSF'  where false
  {% endcall %}
{% endcall %}

UNION ALL

{% call dbt_unit_testing.test('houses', 'invalid firstfloor square footage vs second floor') %}
  
  {% call dbt_unit_testing.mock_ref ('stg_houses') %}
    select 1 as id, 1800 as YearBuilt, 0 as Fireplaces, null as FireplaceQu, 'Sesame' as Street, 10 as 'FirstFlrSF', 50 as 'SecondFlrSF'
  {% endcall %}
  
  {% call dbt_unit_testing.expect() %}
    select null::numeric as id, null::numeric as YearBuilt,  null::numeric as Fireplaces, null as FireplaceQu, null as Street, null::numeric as 'FirstFlrSF', null::numeric  as 'SecondFlrSF'  where false
  {% endcall %}
{% endcall %}
