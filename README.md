# Fake News Detector

## Overview

This is a Fake News Detector web application built using Django, NLTK, and machine learning. The application takes the news author name and headline as input and classifies the news as either fake or real.

## Features

- Input fields for news author name and headline
- ML-based classification of news as fake or real
- User-friendly web interface using HTML and CSS
- Built with Django for web development
- Utilizes NLTK for natural language processing

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fake-news-detector.git
    cd fake-news-detector
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to use the Fake News Detector.

## Usage

1. Enter the news author name and headline in the provided input fields.
2. Click the "Detect" button to classify the news as fake or real.

## Screenshots

Include screenshots of the web interface to give users a visual preview of your application.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.


## Acknowledgements

- Thank you to [NLTK](https://www.nltk.org/) for providing powerful tools for natural language processing.
- This project was inspired by the need to combat misinformation and fake news.

## Contact

If you have any questions or suggestions, feel free to reach out to [karshit48@gmail.com](mailto:karshit48@gmail.com).

