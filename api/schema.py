from typing import Optional, Union
from fastapi import Body, FastAPI, Form
from pydantic import BaseModel, Field, validator, EmailStr
import uuid
from urllib.parse import urlparse


class RequestModel(BaseModel):
    url: str = Field(
        title="URL",
        description="URL to scrape", min_length=1)

    @validator('url')
    def validate_is_url(cls, v):
        try:
            result = urlparse(v)
            # return all([result.scheme, result.netloc, result.path])
            return v
        except:
            raise ValueError(
                'Enter a valid url')

            # @validator('status')
            # def validate_status(cls, v):
            #     if v != "new" and v != "current" and v != "closed":
            #         raise ValueError(
            #             'Wrong input for game master status, status should be either new, current or deprecated')
            #     return v

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        # schema_extra = {
        #     "example": {
        #         "name": "Ayinke Ade",
        #         "email": "ayinke.ade@email.com"
        #     }
        # }
