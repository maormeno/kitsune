from pydantic import BaseModel


class FoliosRequestArgs(BaseModel):
    RutCertificado: str
    Password: str
    RutEmpresa: str
    Ambiente: int = 1


class GenerateGuiaDespachoArgs(BaseModel):
    tipoDTE: int = 56
