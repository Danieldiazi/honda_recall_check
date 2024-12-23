import requests
import json

class HondaRecallAPIError(Exception):
    """Excepción personalizada para errores en la consulta a la API de Honda."""
    pass

class HondaRecallAPI:
    """Clase que interactúa con la API de Honda para verificar llamadas a revisión."""
    BASE_URL = "https://www.honda.es/cars/owners/recalls-and-updates/_jcr_content/service.submit.html"

    def __init__(self, vin):
        self.vin = vin

    def check_recall(self):
        """Envía el VIN al endpoint y procesa la respuesta JSON."""
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            payload = {"vin": self.vin}

            response = requests.post(self.BASE_URL, headers=headers, data=payload)
            response.raise_for_status()  # Lanza requests.exceptions.HTTPError si no es 200 OK

            json_response = response.json()

            if "recall" in json_response and "updateDetails" in json_response["recall"]:
                updates = json_response["recall"]["updateDetails"]
                return [
                    {"campaign": update["campaign"], "description": update["description"]}
                    for update in updates
                ]
            return []
        except requests.exceptions.RequestException as e:
            # Error relacionado con la solicitud HTTP
            raise HondaRecallAPIError(f"Error de red o HTTP al consultar Honda API: {e}")
        except json.JSONDecodeError as e:
            # Error al parsear el JSON
            raise HondaRecallAPIError(f"Error al parsear la respuesta JSON: {e}")
        except KeyError as e:
            # Error al acceder a llaves inexistentes en el JSON
            raise HondaRecallAPIError(f"La estructura del JSON no es la esperada: faltante {e}")




