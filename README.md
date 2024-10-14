# URL Shortener

A simple web application that converts long URLs into shorter, more manageable links. Built with Python and Flask, this project allows users to create custom short URLs, track the number of clicks on each link, and manage URL redirection.

## Features

- **URL Shortening**: Generates unique shortened URLs for any long URL.
- **Custom Short URLs**: Allows users to create custom short links.
- **Click Tracking**: Tracks the number of times each short URL has been accessed.
- **User-Friendly Interface**: A simple HTML form with a CSS-styled interface for inputting and displaying shortened URLs.
- **Persistent Storage**: Stores URL mappings in a JSON file, allowing for easy management and data persistence.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: JSON (for URL storage)

## Getting Started

Follow these instructions to set up and run the project on your local machine.

**Prerequisites:**
Python (3.x recommended)
Flask (Install using pip)

**Usage**
1. Open the application in your browser: http://127.0.0.1:5000/.
2. Enter the long URL you want to shorten in the provided form.
3. Optionally, specify a custom short URL.
4. Click Shorten to generate your short URL.
5. The shortened URL will appear, and you can use it to redirect to the original URL.
6. To view the click statistics, go to http://127.0.0.1:5000/stats/<short_url>.
