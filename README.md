# Project 1 - FastAPI
The goal of this exercise is to create both a synchronous and an asynchronous route for querying exchange rates. 

## Dependecies ##
- poetry => 1.8.2 

## Goals ##
- Create an asynchronous route to query the exchange rate.
- Create a synchronous route to query the exchange rate.
- Access an external API to receive the exchange value.

## Runing the Application

1 - Execute the command for create a virtual environment:
```bash
poetry install
```

2 - Execute the application command:
```bash
uvicorn main:app --reload
```

## Access the Application ##

You can access the application in the browser by the following url :
```bash
 http://127.0.0.1:8000    
```

## References ##

- https://fastapi.tiangolo.com/
- https://www.python.org
- https://python-poetry.org/
- https://docs.pydantic.dev/latest/
- https://www.alphavantage.co/
