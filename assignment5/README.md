# IN3110 strømpris

This project fetches and visualizes daily energy prices from the hvakosterstrommen.no API.
It provides a view of energy prices over time for various locations in Norway (Oslo, Bergen, Kristiansan, Tromsø, Trondheim).

### Dependencies

The project requires the following Python packages:

altair==4
altair-viewer
beautifulsoup4
fastapi[all]
pandas
pytest
requests
requests-cache
uvicorn

### Installation

Install the required packages

    - pip install -e .

### Run code

Now that you have the dependencies installed you can run the program

    - python3 strompris.py
