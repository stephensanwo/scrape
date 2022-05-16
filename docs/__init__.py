from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def my_schema(server):
    openapi_schema = get_openapi(
        title="Python Scraping Engineering Task",
        version="1.0",
        routes=server.routes,
    )
    openapi_schema["info"] = {
        "title": "Python Scraping Engineering Task",
        "version": "1.0",
        "description": "Python Scraping Engineering Task",
        "contact": {
            "name": "Stephen Sanwo",
            "url": "https://www.stephensanwo.dev",
            "email": "stephen.sanwo@icloud.com"
        },

    }
    server.openapi_schema = openapi_schema
    return server.openapi_schema

    server.openapi = my_schema
