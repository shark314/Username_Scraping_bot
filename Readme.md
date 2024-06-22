```markdown
# Telegram Message Extractor

This Python script retrieves messages and participant information from specified Telegram group IDs.

## Prerequisites

Before running the script, ensure you have the following:

1. Python 3.12.3 installed on your system.
2. You already know the drill: `pip install -r requirements.txt` to install the necessary requirements, then just hop on a server and do:
3. A Telegram API ID and API hash. You can obtain these by creating a Telegram app on the [Telegram API website](https://my.telegram.org/apps).
4. A Telegram phone number associated with your Telegram account.
5. A `group_id.txt` file containing the Telegram group IDs you want to extract messages from, with each group ID on a new line.

## Usage

1. Clone the repository or download the script.
2. Create a `.env` file in the same directory as the script and add the following variables:
   ```
   api_id=<your_api_id>
   api_hash=<your_api_hash>
   phone_number=<your_phone_number>
   ```
3. Run the script using the following command:
   ```
   python script.py
   ```
4. If you haven't authorized the script to access your Telegram account, you'll be prompted to enter the code sent to your phone number.
5. The script will retrieve the messages and participant information from the specified Telegram groups and save them to two JSON files:
   - `unique_participants.json`: Contains a list of unique participants with their user IDs, usernames, and first names.
   - `unique_message_authors.json`: Contains a list of unique message authors with their user IDs, usernames, and first names.

## Command-Line Options

The script supports the following command-line options:

- `-t` or `--token`: Specify a Telegram bot token to control the script's behavior.
- `--help`: Display the help message.

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```
