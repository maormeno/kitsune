import requests
from args import FoliosRequestArgs, GenerateGuiaDespachoArgs
from fastapi import FastAPI
from logic_functions import auth_to_base64, certificate_file

app = FastAPI()
AUTH = auth_to_base64()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/folios/obtain")
def request_folios(body: FoliosRequestArgs):
    # Access .pfx file and use it to send request to SimpleAPI
    return


@app.post("/folios/available")
def request_available_folios(body: FoliosRequestArgs):
    try:
        url = "https://servicios.simpleapi.cl/api/folios/get/33/"
        payload = {"input": str(dict(body))}
        files = [certificate_file(body.RutEmpresa)]
        headers = {"Authorization": AUTH}
        response = requests.post(url, headers=headers, data=payload, files=files)
        return {
            "status_code": response.status_code,
            "reason": response.reason,
            "text": response.text,
        }
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


@app.post("/dte/guiadespacho")
def generate_dte_guiadespacho(body: GenerateGuiaDespachoArgs):
    # GENERAR DTE GUIA DE DESPACHO
    pass
