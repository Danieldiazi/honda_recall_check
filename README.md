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
- Puedes configurar el intervalo de comprobación desde las opciones de la integración.

## A tener en cuenta / Disclaimer
Esta integración navega por la web de Honda para extraer la información, en el momento en que hagan un cambio de su web, esta integración puede fallar y habrá que esperar poder adaptarla (si es posible).
