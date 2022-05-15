from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def my_schema(server):
    openapi_schema = get_openapi(
        title="Wager-Core API Documentation and Specifications",
        version="1.0",
        routes=server.routes,
    )
    openapi_schema["info"] = {
        "title": "Wager-Core API Documentation and Specifications",
        "version": "1.0",
        "description": "Wager-Core API Documentation and Specifications",
        "termsOfService": "/",
        "contact": {
            "name": "Get Help with this API",
            "url": "/",
            "email": "stephen.sanwo@icloud.com"
        },
        "license": {
            "name": "Copyrights - Wager",
            "url": ""
        },
    }
    server.openapi_schema = openapi_schema
    return server.openapi_schema

    server.openapi = my_schema
