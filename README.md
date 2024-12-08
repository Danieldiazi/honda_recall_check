![GitHub Activity](https://img.shields.io/github/commit-activity/m/danieldiazi/honda_recall_check?label=commits)
![GitHub Release](https://img.shields.io/github/v/release/danieldiazi/honda_recall_check)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Danieldiazi_honda_recall_checka&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Danieldiazi_honda_recall_check)

# Honda Recall Check

Integración personalizada de Home Assistant para comprobar si un vehículo Honda tiene llamadas a revisión o actualizaciones pendientes.

Proporciona dos sensores:

- Uno boleano, que indica si hay o no una llamada a revisión.
- Otro, que indica el número de llamadas a revisión. Además en los atributos, indica el detalle de cada llamada a revisión.

## Usos
Aquí te pongo algún ejemplo de sus posibles usos, aunque seguro que tienes más imaginación que yo y se te ocurren más :)
### Integración en panel

![imagen](https://github.com/user-attachments/assets/395d21e0-43cb-499b-a30c-929b438bcc3a)


### Incluir en automatizaciones para enviar avisos.
 Puedes incluir en un mensaje los datos de la llamada a revisión, por ejemplo
   - Aviso de llamada a Revisión de Honda: {{state_attr('sensor.honda_recall_count_XXXXXXX','recalls')}}
 Donde sensor.honda_recall_count_XXXXXXX es el sensor que indica el número de llamadas a revisión.
   
## Instalación

### Manual
1. Copia la carpeta `honda_recall_check` en la ruta `custom_components/`.
2. Reinicia Home Assistant.
3. Configura la integración desde **Configuración > Dispositivos e Integraciones**.

### A través de HACS
1. Añade este repositorio como repositorio personalizado en HACS.
2. Busca "Honda Recall Check" en HACS e instálalo.
3. Reinicia Home Assistant.

## Configuración

- Añade el código VIN de tu vehículo durante la configuración desde la UI.
- Puedes configurar el intervalo de comprobación desde las opciones de la integración. Por defecto está a 1440 minutos (24 horas), que es más que suficiente, tampoco hay que estar consultando la web de honda cada minuto.

## A tener en cuenta / Disclaimer
Esta integración navega por la web de Honda para extraer la información, en el momento en que hagan un cambio de su web, esta integración puede fallar y habrá que esperar poder adaptarla (si es posible).
