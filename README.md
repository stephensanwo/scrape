# Python Scraping Engineering Task

## Solution

### Description

Scrape: A simple python API to scrape the HTML of any url
See Github Repo (https://github.com/stephensanwo/scrape)

Assumptions:

The problem statement requires that the scrape endpoint(/scrape) support GET and POST requests, while also accepting parameters within the body of the HTTP request; headers (dict), cookies (dict), payload (dict).

I thought of 3 ways to handle this requirement, and implemented number 3

1. Create a single POST endpoint and add an additional parameter for the user to indicate if the request to the provided url is a POST or GET request. The aiohttp session will be POST or GET to the provided url, depending on the user input.

2. Create a single POST endpoint and make assumptions that requests without a payload will be GET requests and requests with payloads will be POST requests.

3. [SELECTED OPTION] Create the /scrape endpoint to support POST and GET requests, for the GET request, since we should not send a request body to the GET request (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET), the /scrape endpoint will fetch the HTML and return it to the user, while the POST endpoint will accept all the optional parameters provided by the user.

### App Structure:

- api: src files, routes and schema
- docs: OpenAPI documentation
- main.py: server entry file
- requirements.txt: requirements file
- test_main.py: application test file

### Tools and Frameworks:

- Python 3.8
- FastAPI
- Uvicorn
- See full list of dependencies in requirements.txt

### Installation (Development):

- cd scrape/

- Create a virtual environment (python 3.8)

  ```
  python3.8 -m venv env
  ```

- Activate the virtual environment

  ```
  source env/bin/activate
  ```

- Install the requirements

  ```
  pip install -r requirements.txt
  ```

- Run the application

  ```
  python main.py
  ```

- Open the FastAPI swagger documentation on localhost://7001

### Tests:

```
pytest -v --cov
```

### URL endpoints:

| URL Endpoint | HTTP Methods | Summary                                                                                               |
| ------------ | ------------ | ----------------------------------------------------------------------------------------------------- |
| `scrape`     | `POST`       | Request the API to send POST request to the provided url, providing the headers, cookies, and payload |
| `scrape`     | `GET`        | Request the API to send a simple GET request to the provided url                                      |

### Documentation and Examples

See documentation at: http://localhost:7001/docs

### Author

[Stephen Sanwo](https://github.com/stephensanwo)
