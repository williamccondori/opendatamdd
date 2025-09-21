from app.web.application.dtos.base_dto import BaseDTO


class LayerInformationOptionDTO(BaseDTO):
    id: str
    label: str


class LayerInformationFilterDTO(BaseDTO):
    label: str
    name: str
    options: list[LayerInformationOptionDTO] = []


class LayerInformationTableDTO(BaseDTO):
    columns: list[dict] = []
    data: list[dict] = []
    filters: list[LayerInformationFilterDTO]
