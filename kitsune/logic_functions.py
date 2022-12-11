import base64
import os
from dotenv import load_dotenv

load_dotenv()

# This function is used to convert the API key into a base64 string
def auth_to_base64():
    SimpleAPI_KEY = os.getenv("SIMPLEAPI_KEY")
    SimpleAPI_KEY = ("api:" + SimpleAPI_KEY).encode("ascii")
    SimpleAPI_KEY = base64.b64encode(SimpleAPI_KEY)
    base64_message = SimpleAPI_KEY.decode("ascii")
    auth_64_message = "Basic " + base64_message
    return auth_64_message


# This function is used to open the .pfx file and return it in requests format
def certificate_file(rut_empresa):
    certificate_name = "certificado" + rut_empresa[:-2] + ".pfx"
    cert_file = (
        "files",
        (
            certificate_name,
            open(
                "files/" + certificate_name,
                "rb",
            ),
            "application/octet-stream",
        ),
    )
    return cert_file
