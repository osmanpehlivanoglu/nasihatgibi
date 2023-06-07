# nasihatgibi Readme

This project is a Python script that retrieves data from a Google Sheets spreadsheet, adds the data to a MongoDB database, selects a random entry from the database, and sends it to a Telegram channel using a Telegram bot. The script is configured to run automatically using GitHub Actions twice a day.

## Setup

To set up and run this project, follow the instructions below:

### Prerequisites

1. Python 3.x should be installed on your system.
2. Create a virtual environment (optional but recommended) to keep the project dependencies isolated.

### Installation

1. Clone this repository to your local machine or download the project files.
2. Open a terminal or command prompt and navigate to the project directory.
3. If you're using a virtual environment, activate it now.

   ```shell
   source <path_to_virtual_env>/bin/activate  # for Unix/Linux
   <path_to_virtual_env>\Scripts\activate    # for Windows

4. Install the required Python packages by running the following command:
   ```bash
   $ pip install -r requirements.txt
   
# Configuration

## Google Sheets API:
- Follow the steps mentioned in the [Google Sheets API Python Quickstart Guide](https://developers.google.com/sheets/api/quickstart/python) to enable the API for your Google account and obtain the `credentials.json` file.
- Add `CREDENTIALS` environment variable in `.env` file with the one line formatted `credentials.json` value.
- Update the `SHEET_URL` environment variable in `.env` file with the URL of your Google Sheets spreadsheet.

## MongoDB:
- Create a [MongoDB](https://cloud.mongodb.com) database and note down the connection details (URI). 
- Update the `URI` environment variable in a `.env` file with your MongoDB connection URI.

## Telegram Bot:
- Create a new Telegram bot using the [BotFather](https://core.telegram.org/bots#botfather) and obtain the bot token.
- Add the bot to the desired Telegram channel and make it an administrator.
- Update the `BOT_TOKEN` and `CHAT_ID` environment variables in a `.env` file with your bot token and channel ID respectively.

## GitHub Actions:
- Push your changes to the repository. The script will run automatically using the provided GitHub Actions workflow configuration twice a day.
- Do not push your `.env` file to the repository, you need to add your environment variables to GitHub secrets.

# Usage

To run the script manually, execute the following command in the project directory:

To test if the GitHub Actions workflow is set up correctly, push your changes to the repository. The script will run automatically according to the configured schedule.

## Project Structure

The project directory contains the following files:

- `main.py`: The main Python script that retrieves data from a Google Sheets spreadsheet, adds it to a MongoDB database, selects a random entry, and sends it to a Telegram channel.
- `.env`: Environment variables file for configuration (not included in the repository).
- `requirements.txt`: List of Python dependencies required by the project.
- `.github/workflows/main.yml`: GitHub Actions workflow configuration file.

# License

This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.