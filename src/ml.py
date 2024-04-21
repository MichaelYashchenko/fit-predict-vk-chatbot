import requests

from src.schemas import RequestModel, ResponseModel
from src.exceptions import APIError


def inference(input_: RequestModel) -> ResponseModel:
    try:
        response = requests.post(
            "http://localhost:8000/inference/",
            headers=_headers(),
            json=input_.model_dump(),
        )
    except requests.exceptions.Timeout as e:
        raise APIError() from e
    if response.status_code >= 400:
        raise APIError(response.status_code, response.text)
    data = response.json()
    return ResponseModel.parse_obj(data)


def _headers():
    return {
        "Content-type": "application/json; charset=utf8",
        "Accept": "application/json; charset=utf8",
    }
