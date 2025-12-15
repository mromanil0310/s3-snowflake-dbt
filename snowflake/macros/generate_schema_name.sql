{% macro generate_schema_name(custom_schema_name, node) -%}
    {%- if custom_schema_name is not none and custom_schema_name | length -%}
        {{ custom_schema_name | upper }}     {# Use schema exactly #}
    {%- else -%}
        {{ target.schema }}                  {# fallback #}
    {%- endif -%}
{%- endmacro %}