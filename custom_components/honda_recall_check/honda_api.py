import requests

class HondaRecallAPI:
    """Clase que interactúa con la API de Honda para verificar llamadas a revisión."""
    BASE_URL = "https://www.honda.es/cars/owners/recalls-and-updates/_jcr_content/service.submit.html"

    def __init__(self, vin):
        self.vin = vin

    def check_recall(self):
        """Envía el VIN al endpoint y procesa la respuesta JSON."""
        try:
            # Configurar los headers
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            payload = {"vin": self.vin}

            # Realizar la solicitud POST
            response = requests.post(self.BASE_URL, headers=headers, data=payload)
            response.raise_for_status()  # Lanza un error si la respuesta no es 200 OK

            # Parsear la respuesta JSON
            json_response = response.json()

            # Extraer detalles de llamadas a revisión si existen
            if "recall" in json_response and "updateDetails" in json_response["recall"]:
                updates = json_response["recall"]["updateDetails"]
                return [
                    {"campaign": update["campaign"], "description": update["description"]}
                    for update in updates
                ]

            # No hay llamadas a revisión
            return []
        except Exception as e:
            raise Exception(f"Error al consultar Honda API: {e}")




