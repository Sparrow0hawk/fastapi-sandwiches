# FastAPI Sandwich Shop

Exploring FastAPI for Python web stuff.

## Setup

To use this repository you will need:
- Python 3.12

1. Create a virtual environment
    ```bash
   python3 -m venv .venv 
   ```
2. Activate the virtual environment
    ```bash
   . .venv/bin/activate
   ```
3. Install dependencies into the virtual environment
    ```bash
   pip install .
   ```
4. Run the app
    ```bash
   uvicorn --port 8000 fastapi_sandwiches.main:app
   ```
5. View the app at http://127.0.0.1:8000

