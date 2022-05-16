from typing import Optional, Union
from fastapi import Body, FastAPI, Form, HTTPException
from pydantic import BaseModel, Field, validator, EmailStr
import uuid
from urllib.parse import urlparse


class RequestModel(BaseModel):
    """
    Description:
        Request object for the GET request
    """
    url: str = Field(
        title="URL",
        description="URL to scrape", min_length=1)

    # Custom validator to check the validity of the url, using the url schema and urlparse
    @validator('url')
    def validate_is_url(cls, value):
        result = urlparse(value)

        if result.scheme != "https" and result.scheme != "http":
            raise HTTPException(
                status_code=400, detail="Enter a valid url. Url schema should be HTTP or HTTPS")

        return value


class ScrapeModel(BaseModel):
    """
    Description:
        Request object for the POST request
    """

    url: str = Field(
        title="URL",
        description="URL to scrape", min_length=1)

    headers: dict = Field(...,
                          title="Headers",
                          description="Optional custom headers"
                          )

    cookies: dict = Field(...,
                          title="Cookies",
                          description="Optional custom cookies"
                          )

    payload: dict = Field(...,
                          title="Payload",
                          description="Optional data payload"
                          )

    # Custom validator to check the validity of the url, using the url schema and urlparse
    @validator('url')
    def validate_is_url(cls, value):
        result = urlparse(value)
        if result.scheme != "https" and result.scheme != "http":
            raise HTTPException(
                status_code=400, detail="Enter a valid url. Url schema should be HTTP or HTTPS")

        return value

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "url": "http://httpbin.org/post",
                "headers": {
                    "header-1": "value-1"
                },
                "cookies": {
                    "cookie1": "cookievalue"
                },
                "payload": {
                    "key1": "value1",
                    "key2": "value2"

                }
            }
        }
