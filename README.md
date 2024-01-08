# Beer Fridge Backend

## Overview

This repository contains the backend code for the Beer Fridge application, a Flask-based API service for managing beer collections. It interacts with a Postgres database using SQLAlchemy and is configured to work with ElephantSQL's hosted database solution.

## Features

- **Flask API**: Provides RESTful endpoints for managing beer collection data.
- **Postgres Database**: Utilizes PostgreSQL for storing and querying data.
- **SQLAlchemy ORM**: Leverages SQLAlchemy for database interactions.
- **ElephantSQL Integration**: Configured to connect with a Postgres database hosted on ElephantSQL.

## Installation

1. Clone the repository:
   `git clone https://github.com/AZBL/beer-backend`

2. Navigate to the project directory:
   `cd beer-backend`

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate # On Windows use venv\Scripts\activate
   ```
4. Install dependencies:
   `pip install requirements.txt`

## Configuration

Set up your local environment variables to match those expected by the Flask application, including database connection details to your ElephantSQL instance.

## Usage

To start the Flask server locally:
`flask run`

This will start the server on [http://localhost:5000](http://localhost:5000) by default.

## Database Setup

Ensure you have an ElephantSQL instance set up and the connection details correctly specified in your environment variables or configuration files.

## Contributing

Contributions are welcome. Feel free to submit issues, pull requests, or suggestions to improve the codebase.
