# 🛒 Wallapop Scrapper

Wallapop scraper using Selenium for Python, which retrieves products based on a query and allows us to store the products in a database, as well as receive updates via a Telegram bot.

## 📋 Requirements

| Requirement  | Description                                          |
| ------------ | ---------------------------------------------------- |
| 🐍 Python   | Python 3.x is required to run the scripts.            |
| 🌐 Selenium | Selenium is used for web scraping.                    |
| 🗄️ MySQL    | MySQL is the database used to store the scraped data. |
| 🤖 Telebot  | Telebot is used to send updates via a Telegram bot.   |
| 🛠️ dotenv   | dotenv is used to manage environment variables.       |


## 🤖 How can I set up my Telegram bot?

1. **🔍 Create a new bot on Telegram**
    - Open Telegram and search for the `BotFather`.
    - Send the `/newbot` command to create a new bot.
    - Follow the instructions to set up your bot.

2. **🔑 Get the bot token**
    - Once the bot is created, you will receive a token.
    - Copy the token and save it for later.

3. **💬 Create a new group chat**
    - Create a new group chat where you want to receive the updates.
    - Add the bot to the group chat.

4. **🆔 Get the chat ID**
    - Open the following URL in your browser, replacing `<bot_token>` with your bot token:
      ```
      https://api.telegram.org/bot<bot_token>/getUpdates
      ```
    - Send a message to the group chat.
    - Refresh the page and look for the `chat` object.
    - Copy the `id` value and save it for later.

5. **➡️ Continue with the installation steps**
    

## ⚙️ Installation

### 🪟 Windows

1. **📥 Clone the repository**
    ```sh
    git clone https://github.com/CuB1z/wallapop-scrapper
    cd wallapop-scrapper
    ```

2. **🐍 Create and activate a virtual environment**
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. **📦 Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **🔧 Configure the environment variables**
    - Copy the `.env.example` file to `.env`:
      ```sh
      copy .env.example .env
      ```
    - Open the `.env` file and fill in the necessary values:
      ```properties
      TELEGRAM_BOT_TOKEN=your_telegram_bot_token
      CHAT_ID=your_chat_id
      DB_HOST=your_db_host
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_NAME=your_db_name
      DB_PORT=your_db_port
      ```

5. **🗄️ Create the table in the database by running the SQL script**
    ```sh
    mysql -u <user> -p <database_name> < wallapop/wallapopTableCreator.sql
    ```

### 🐧 MacOS and Linux

1. **📥 Clone the repository**
    ```sh
    git clone https://github.com/CuB1z/wallapop-scrapper
    cd wallapop-scrapper
    ```

2. **🐍 Create and activate a virtual environment**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **📦 Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **🔧 Configure the environment variables**
    - Copy the `.env.example` file to `.env`:
      ```sh
      cp .env.example .env
      ```
    - Open the `.env` file and fill in the necessary values:
      ```properties
      TELEGRAM_BOT_TOKEN=your_telegram_bot_token
      CHAT_ID=your_chat_id
      DB_HOST=your_db_host
      DB_USER=your_db_user
      DB_PASSWORD=your_db_password
      DB_NAME=your_db_name
      DB_PORT=your_db_port
      ```

5. **🗄️ Create the table in the database by running the SQL script**
    ```sh
    mysql -u <user> -p <database_name> < wallapop/wallapopTableCreator.sql
    ```


## 🚀 Usage

1. **🛠️ Configure the query params and keywords in the `wallapop/wallapopConfig.json` file**
    ```json
    {
        "params": {
            "category_ids": 100,
            "filters_source": "search_box",
            "latitude": 40.41956,
            "longitude": -3.69196,
            "max_sale_price": 3000,
            "min_km": 1000,
            "max_km": 250000,
            "min_year": 2000,
            "max_year": 2008,
            "min_horse_power": 100,
            "time_filter": "today",
            "order_by": "newest",
            "... add your own params": "..."
        },
        "keywords": ["bmw", "audi a3", "... add your own keywords"]
    }
    ```

2. **📝 Feel free to modify the `main.py` params present at the top of the file**
    ```python
    # Database table where the products will be stored
    PRODUCTS_TABLE = "products"

    # Configuration file path
    CONFIG_FILE = "./wallapop/wallapopConfig.json"

    # Interval in minutes to check for new products
    INTERVAL = 20
    ```

3. **▶️ Once everything is set up, run the script**
    ```sh
    python main.py
    ```


## 👨‍💻 Developers

| Name            | Linkedin                                                 | GitHub                                       |
| --------------- | -------------------------------------------------------- | -------------------------------------------- |
| Daniel Santos   | [Daniel Santos](https://www.linkedin.com/in/danisntoss/) | [@danisntoss](https://github.com/danisntoss) |
| Diego Sánchez   | [Diego Sánchez](https://www.linkedin.com/in/cub1z/)      | [@cub1z](https://github.com/cub1z)           |


## 📜 License

This project is licensed under the CC License.

---