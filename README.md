# 🛒 Wallapop Scrapper

Wallapop scraper using Selenium for Python, which retrieves products based on a query and allows us to store the products in a database, as well as receive updates via a Telegram bot.

## 📋 Requirements

- 🐍 Python 3.x
- 🌐 Selenium
- 🗄️ MySQL
- 🤖 Telebot
- 🛠️ dotenv

## ⚙️ Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/CuB1z/wallapop-scrapper
    cd wallapop-scrapper
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the environment variables:**
    - Copy the `.env.example` file to `.env` and fill in the necessary values.

5. **Create the table in the database by running the SQL script:**
    ```sh
    mysql -u <user> -p <database_name> < wallapop/wallapopTableCreator.sql
    ```

## 🚀 Usage

Run the main script:
```sh
python main.py
```

## 📂 Project Structure

- **main.py:** Main script that runs the scraper, stores products in the database, and sends updates to Telegram.
- **db:** Contains the configuration and connection to the MySQL database.
- **telegram:** Contains the Telegram client for sending messages.
- **wallapop:** Contains the scraper and utilities for interacting with Wallapop.

## 👥 Developers

| Name            | GitHub                                      |
|-----------------|---------------------------------------------|
| Daniel Santos   | [@danisntoss](https://github.com/danisntoss)|
| Diego Sánchez   | [@cub1z](https://github.com/cub1z)          |

## 📜 License

This project is licensed under the CC License.
