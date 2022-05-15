from fastapi import APIRouter, Request
import asyncio
import aiohttp
from . import utils
from . import schema


router = APIRouter()


@router.get("/scrape")
async def scrape(request: Request, url: str):
    headers = {}
    params = {}
    payload = {}

    async with aiohttp.ClientSession() as session:
        print(url)
        html = await utils.request(url, session, headers, params, payload, request_id="fdf", request_type="GET")

        # print(html)

    return html


@router.post("/scrape")
async def scrape(request: Request, url: str, payload: schema.RequestModel):
    headers = {}
    params = {}
    payload = {'key1': 'value1', 'key2': 'value2'}

    async with aiohttp.ClientSession() as session:
        print(url)
        html = await utils.request(url, session, headers, params, payload, request_id="fdf", request_type="POST")

        # print(html)

    return None
