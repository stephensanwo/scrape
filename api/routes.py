from fastapi import APIRouter, Request, Depends, Header
import asyncio
import aiohttp
from . import schema
from typing import Union
from starlette.datastructures import MutableHeaders

router = APIRouter()


# @route   GET /scrape
# @desc    Get HTML of provided url, this will handle when the user sends a GET request to the /scrape endpoint
# @access  Public

@router.get("/scrape")
async def scrape(request: schema.RequestModel = Depends()):
    """
    Description: 
        Get HTML of provided url, this will handle when the user sends a GET request to the /scrape endpoint
    Args:
        request (Request): Request Object
            - url: parameter (url) for GET request
    Returns:
        HTML
    """
    # If the user sends a GET request, there shouldnt be a request body, the POST request function will handle the request body.

    # Using async request, send a post request to the endpoint pfovided by the user, passing all the parameters to the session.post method if they exist

    async with aiohttp.ClientSession() as session:
        async with session.get(request.url) as response:
            # await the response, and return the html
            html = await response.text()
    return html


# @route   POST /scrape
# @desc    Get HTML of provided url, this will handle when the user sends a POST request to the /scrape endpoint
# @access  Public

@router.post("/scrape")
async def scrape(request: schema.ScrapeModel):
    """
    Description:
        API route to scrape a url, based on the information provided by the user
    Args:
        request (schema.ScrapeModel): Request Object
            - url: User required data
            - headers : User optional data
    Returns:
        HTML
    """

    headers = request.headers
    cookies = request.cookies
    payload = request.payload

    # check if cookies exist in the request object, then assign it to the custom cookies
    if request.cookies:
        cookies = request.cookies

    print(cookies)

    # Using async request, send a post request to the endpoint pfovided by the user, passing all the parameters to the session.post method if they exist
    async with aiohttp.ClientSession() as session:
        async with session.post(request.url, headers=headers, cookies=cookies, json=payload) as response:
            # await the response, and return the html
            html = await response.text()

            print(html)

    return html
