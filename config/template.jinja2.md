# Relatório de Saúde Animal: {{ date }}

{% if species_list|length == 0 %}
Nenhum dado por espécie encontrado.
{% else %}
{% for item in species_list %}
## Espécie: {{ item.name }}

### **Raça: {{ item.breed }}**

Análise Exploratória:

- **Quantidade Total de Animais:** {{ item.total_quantity }}
- **Temperatura Média:** {{ item.average_temperature }}°C
- **Temperatura Máxima:** {{ item.max_temperature }}°C
- **Temperatura Mínima:** {{ item.min_temperature }}°C
- **Deslocamento Total:** {{ item.total_distance }} km
- **Deslocamento Médio por Animal:** {{ item.average_distance }} km
- **Deslocamento Máximo:** {{ item.max_distance }} km
- **Deslocamento Mínimo:** {{ item.min_distance }} km

{% if item.alerts_data %}
Alertas:
- **Animais com Temperatura Elevada:** {{ item.alerts_data.animals_with_high_temperature }}
- **Animais com Temperatura Baixa:** {{ item.alerts_data.animals_with_low_temperature }}
- **Aniamis com Batimentos Cardíacos Elevados:** {{ item.alerts_data.animals_with_high_heart_rate }}
- **Animais com Batimentos Cardíacos Baixos:** {{ item.alerts_data.animals_with_low_heart_rate }}
- **Animais com Deslocamento Elevado:** {{ item.alerts_data.animals_with_high_distance }}
- **Animais com Deslocamento Baixo:** {{ item.alerts_data.animals_with_low_distance }}
{% endif %}

{% endfor %}
{% endif %}