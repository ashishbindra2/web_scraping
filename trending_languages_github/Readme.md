# Web Scraping with FastAPI

This project demonstrates how to build a web scraping service using **FastAPI** and integrate it.

## Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.11+**
- **FastAPI**: Web framework for building APIs
- **aiohttp**: For asynchronous web scraping
- **BeautifulSoup**: For parsing HTML content

You can install the necessary dependencies using `pip`:

```bash
pip install fastapi uvicorn aiohttp beautifulsoup4 pandas wing
```

## Project Setup

### 1. Clone the repository

Clone the project to your local machine:

```bash
git clone https://github.com/ashishbindra2/trending_languages_github.git
cd trending_languages_github
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Start the FastAPI server

To run the FastAPI server:

```bash
fastapi dev main.py
uvicorn main:app --reload
```

This will start the FastAPI application and you can access the documentation at:

```
http://127.0.0.1:8000/docs
```

### 2. Web Scraping Endpoint

To initiate a scraping task, send a `GET` request to the `/scrape` endpoint:

```bash
curl -X 'GET' \
  'http://localhost:8000/analyze/github/trending/Python' \
  -H 'accept: application/json'
```

This will trigger the web scraping process and return the scraped data in JSON format.

Sorry i did not get chance to do **edges** part and analysis part
