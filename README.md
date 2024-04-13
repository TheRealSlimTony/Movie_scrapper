# Movie Scraper

## Description
Movie Scraper is a real-time movie scraping application that utilizes FastAPI to create a REST API. It allows users to retrieve information about movies currently being shown in various locations.

## Features
- Real-time scraping of movie information in Costa Rica.
- REST API built with FastAPI.
- Detailed information for each movie, including showtimes and formats.

## Technologies Used
- Python
- FastAPI
- requests_html
- asyncio
- re (Regular Expressions)

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/TheRealSlimTony/Movie_scrapper.git
    ```

2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Feel free to make any adjustments to better suit your project's specifics.

## Usage
1. Start the FastAPI server:
    ```
    uvicorn main:app --reload
    ```

2. Access the API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) to explore the available endpoints and interact with the API.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
