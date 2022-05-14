# Python Scraping Engineering Task

## Task

---

### Task description

- Create a simple API that will expose one endpoint called /scrape

- This endpoint will accept four parameters:

  - url: str - URL to scrape [required]
  - headers: dict - custom headers [optional]
  - cookies: dict - custom cookies [optional]
  - payload: dict - Data payload (type: application/json) [optional]

- This API will take the URL from the endpoint parameters and make the request using HTTP library (async)

  - Users can pass custom headers. If these are not present, use default headers
  - Users can pass custom cookies. If these are not present, do not pass cookies

- Support both GET and POST methods

- The API response is the HTML body of the HTTP response

- You can use http://httpbin.org/ website to test your solution

### Requirements

- Python 3.6+
- FastAPI framework

### Delivery

- Take this as an opportunity to showcase your skills! Any additional functionality is very
  welcomed. However, make sure to allocate no more than 4 hours to implement this task.

- Include README.md file with instructions on how to start the application and expose API
  documentation (feel free to use auto-generated FastAPI documentation).

- Once the task is finished, please book a slot using this link and make sure to send your task to
  tamara@reviewshake.com at least 24 hours before the booked time.

# Solution

---

### Description

Audio File API, is an API that manages the file metadata of an Audio File Server

Three audio file types are supported:

- Song
- Podcast
- Audiobook

### Built with:

- Python 3.8
- Flask 1.1.2
- MongoDB
- Docker
- See full list of dependencies in requirements.txt

## Installation (Development):

- clone the repository

  ```
  git clone https://github.com/stephensanwo/Filed-Audio-Server.git

  ```

- cd projectname/

- Create a virtual environment

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
  flask run
  ```

- The application will run on localhost://7000

## Features:

### Application Security:

An API Key is created for the API using the api-credentials CLI tool in development. An API Key is required on specific routes. See URL endpoints below for details <b>remove the require_api decorator on routes to disbale application security in development</b>

To generate an API. in the CLI, run:

```
python api-credentials.py john.doe@email.com
```

### Application Monitoring

Warning and Error logs are collected and stored in request-logs.log file for application monitoring. Typical flags monitored include:

- Database connection offline, or Internal server errors
- Unauthorized user trying to access a restricted route (provides the IP)

### URL endpoints

| URL Endpoint                                                                        | HTTP Methods | Summary                                                                       |
| ----------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------------------------------- |
| `api/create`                                                                        | `POST`       | Creates a new Audio File Record                                               |
| `api/get_audio_files?audioFileType=<audioFileType>`                                 | `GET`        | Retrieves all Audio Files for a specific file type (song, podcast, audiobook) |
| `api/get_audio_file?audioFileType=<audioFileType>&audioFileID=<audioFileID>`        | `GET`        | Retrieves a specific Audio File by file type and file ID                      |
| `/api/v1/update_audio_file?audioFileType=<audioFileType>&audioFileID=<audioFileID>` | `POST`       | Updates the Audio File by file ID and file type                               |
| `/api/v1/delete_audio_file?audioFileType=<audioFileType>&audioFileID=<audioFileID>` | `POST`       | Deletes specific Audio File by file type and file ID                          |

#### Example Request Metadata -> Create New Song

```
Example body
{
    "audioFileType": "song",
    "audioFileMetadata": {
        "name_of_song": "Paradise, Coldplay",
        "duration": 40
    }
}
```

#### Example -> Create New Podcast

```
{
    "audioFileType": "podcast",
    "audioFileMetadata": {
        "name_of_podcast": "All In Podcast",
        "duration": 1909,
        "host": "Jason Calacanis",
        "participants": ["Chamath Palihapitiya", "Davis Sacks","David Friedberg"]
    }
}
```

#### Example -> Create New Podcast

```
{
    "audioFileType": "podcast",
    "audioFileMetadata": {
        "name_of_podcast": "All In Podcast",
        "duration": 1909,
        "host": "Jason Calacanis",
        "participants": ["Chamath Palihapitiya", "Davis Sacks","David Friedberg"]
    }
}
```

#### Example -> Create New Audiobook

```
{
    "audioFileType": "audiobook",
    "audioFileMetadata": {
        "title_of_audiobook": "Born a Crime",
        "author_of_title": "Trevor Noah",
        "narrator": "Trevor Noah",
        "duration": 390492
    }
}
```

See further documentation in docs/,

### Application Testing:

In the project root, run:

```
python3.8 test.py
```

## Deployement (Docker Compose, Nginx Web Server, uWSGI Application Server)

In terminal, with docker installed run:

```
  docker-compose build
  docker-compose up
```

Create API Credentials in Production

cd into the API container

```
docker exec -it api bash
```

exceute the API Credentials CLI command

```
python3.8 api-credentials.py john.doe@email.com
```

## Todos

## License

MIT

## Author

[Stephen Sanwo](https://github.com/stephensanwo)
