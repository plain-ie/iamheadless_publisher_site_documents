from typing import List, Optional

from iamheadless_publisher_site.pydantic_models import BaseItemContentsPydanticModel, BaseItemDataPydanticModel, BaseItemPydanticModel

from .conf import settings


class DocumentContentPydanticModel(BaseItemContentsPydanticModel):
    file_name: str
    language: str
    summary: Optional[str]
    title: str


class DocumentDataPydanticModel(BaseItemDataPydanticModel):
    contents: List[DocumentContentPydanticModel]


class DocumentPydanticModel(BaseItemPydanticModel):
    _content_model = DocumentContentPydanticModel
    _data_model = DocumentDataPydanticModel
    _display_name_plural = 'documents'
    _display_name_singular = 'document'
    _item_type = 'document'

    data: DocumentDataPydanticModel
