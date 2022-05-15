async def request(url: str, session, headers: dict, params: dict, payload: dict, request_id: str, request_type) -> dict:
    print(f"Handling {request_type} request for url: {url}")
    if request_type == "GET":
        async with session.get(url, headers=headers, params=params, json=payload) as response:
            data = await response.text()
            print(data)
            print(f"{request_type} request complete for url: {url}")
        return data

    else:
        async with session.post(url, headers=headers, params=params, json=payload) as response:
            data = await response.text()
            print(data)
            print(f"{request_type} request complete for: {url}")
        return data
