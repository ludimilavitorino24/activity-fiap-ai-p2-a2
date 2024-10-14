# Relatório de Saúde Animal: {{ date }}
{% if species_list|length == 0 %}
Nenhum dado por espécie encontrado.
{% else %}
{% for species in species_list %}
## Espécie: {{ species.name }}

- **Raça: {{ species.breed }}**
    - **Quantidade Total de Animais:** {{ species.total_quantity }}
    - **Temperatura Média:** {{ species.average_temperature }}°C
    - **Temperatura Máxima:** {{ species.max_temperature }}°C
    - **Temperatura Mínima:** {{ species.min_temperature }}°C
    - **Deslocamento Total:** {{ species.total_distance }} km
    - **Deslocamento Médio por Animal:** {{ species.average_distance }} km
    - **Deslocamento Máximo:** {{ species.max_distance }} km
    - **Deslocamento Mínimo:** {{ species.min_distance }} km
{% endfor %}
{% endif %}