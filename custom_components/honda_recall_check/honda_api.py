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
                "Host": "www.honda.es",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer": "https://www.honda.es/cars/owners/recalls-and-updates.html",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "https://www.honda.es",
            }

            payload = {"vin": self.vin}

            response = requests.post(self.BASE_URL, headers=headers, data=payload, timeout=20)
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
            response = getattr(e, "response", None)
            if response is not None:
               status = response.status_code
               text_preview = response.text[:200]  # primeras 200 letras para no saturar logs
               raise HondaRecallAPIError(
               f"Error de red o HTTP (status {status}) al consultar Honda API: {e}\nRespuesta: {text_preview}")
            else:
               raise HondaRecallAPIError(f"Error de red o HTTP al consultar Honda API: {e}"    )
        except json.JSONDecodeError as e:
            # Error al parsear el JSON
            raise HondaRecallAPIError(f"Error al parsear la respuesta JSON: {e}")
        except KeyError as e:
            # Error al acceder a llaves inexistentes en el JSON
            raise HondaRecallAPIError(f"La estructura del JSON no es la esperada: faltante {e}")




