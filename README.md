# Currency Exchange API

The Currency Exchange API allows users to manage currency exchange operations conveniently. It provides endpoints for registering currency exchange requests and retrieving exchange history.

## Installation

1. Clone the repository.
2. Ensure you have Docker and Docker Compose installed on your system.
3. Navigate to the project directory.
4. Run `docker-compose up --build` to build and start the application.
5. Access the API at `http://localhost:8000/docs`.


## Endpoints

### Register Currency Exchange

- **Method:** `POST`
- **URL:** `/{user_id}/currency-exchange/`
- **Description:** Register a currency exchange request for the specified user.
- **Request Body:**
  - `base_currency`: The currency to be exchanged.
  - `dest_currency`: The currency to exchange to.
  - `amount`: The amount of source currency to exchange.
- **Response:**
  - `id`: Unique identifier for the currency exchange request.
  - `user_id`: The user ID.
  - `base_currency`: The currency to be exchanged.
  - `dest_currency`: The currency to exchange to.
  - `origin_amount`: The amount of source currency to be exchanged.
  - `converted_amount`: The amount of currency to exchange to.
  - `exchange_rate`: The exchange rate at the time of exchange.
  - `transaction_time`: The timestamp of the currency exchange request.

### Get Currency Exchanges by User ID

- **Method:** `GET`
- **URL:** `/{user_id}/currency-exchange/`
- **Description:** Retrieve all currency exchange requests for the specified user.
- **Response:** 
  - List of currency exchange objects:
    - `id`: Unique identifier for the currency exchange request.
    - `base_currency`: The currency to be exchanged.
    - `dest_currency`: The currency to exchange to.
    - `origin_amount`: The amount of source currency to be exchanged.
    - `converted_amount`: The amount of currency to exchange to.
    - `exchange_rate`: The exchange rate at the time of exchange.
    - `transaction_time`: The timestamp of the currency exchange request.

## Dependencies

[![FastAPI](https://img.shields.io/badge/FastAPI-0.101.1-blue)](https://github.com/tiangolo/fastapi)
[![Uvicorn](https://img.shields.io/badge/Uvicorn-0.23.2-blue)](https://github.com/encode/uvicorn)
[![Aiohttp](https://img.shields.io/badge/Aiohttp-3.9.5-blue)](https://github.com/aio-libs/aiohttp)
[![Motor](https://img.shields.io/badge/Motor-3.4.0-blue)](https://github.com/mongodb/motor)
[![Python-decouple](https://img.shields.io/badge/Python--decouple-3.8-blue)](https://github.com/henriquebastos/python-decouple)
[![Meeseeks-singleton](https://img.shields.io/badge/Meeseeks--singleton-0.4.4-blue)](https://github.com/thiagofigueiro/meeseeks-singleton)
[![Witch-doctor](https://img.shields.io/badge/Witch--doctor-1.1.0-blue)](https://github.com/GrindrodBank/witch-doctor)
[![Loglifos](https://img.shields.io/badge/Loglifos-0.2.0-blue)](https://github.com/limbo-prime/loglifos)

## Development Dependencies

[![Pyfiglet](https://img.shields.io/badge/Pyfiglet-1.0.2-blue)](https://github.com/pwaller/pyfiglet)
[![PyLint](https://img.shields.io/badge/PyLint-3.1.0-blue)](https://github.com/PyCQA/pylint)
[![Pytest](https://img.shields.io/badge/Pytest-8.1.1-blue)](https://github.com/pytest-dev/pytest)
[![Black](https://img.shields.io/badge/Black-24.4.0-blue)](https://github.com/psf/black)
[![Pytest-asyncio](https://img.shields.io/badge/Pytest--asyncio-0.23.6-blue)](https://github.com/pytest-dev/pytest-asyncio)
[![Pre-commit](https://img.shields.io/badge/Pre--commit-3.7.0-blue)](https://github.com/pre-commit/pre-commit)


## Usage Example

To register a currency exchange request:

```bash 
curl -X POST -H "Content-Type: application/json" -d '{"source_currency": "USD", "dest_currency": "EUR", "amount": 100}' http://localhost:8000/{user_id}/currency-exchange/
```

To retrieve a list of currency exchanges:

```bash
curl -X GET "http://localhost:8000/{user_id}/currency-exchange/" -H "accept: application/json"
```

