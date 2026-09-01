# Bulk Email Sender

A simple Python automation project that reads email addresses from an Excel file and sends a common email message to multiple recipients using Gmail's SMTP server.

## Features

* **Read Email Addresses:** Reads recipient email addresses from an Excel file.
* **Excel Integration:** Uses Pandas to load and process the Excel data.
* **Bulk Email Sending:** Sends the same email message to multiple recipients automatically.
* **Gmail SMTP:** Uses Gmail SMTP with TLS for secure email communication.
* **Configurable Email:** Email credentials are loaded from a separate JSON configuration file.
* **Automatic Processing:** Loops through all email addresses and sends the message without manually composing each email.

## Technologies Used

* Python 3.x
* Pandas
* JSON
* SMTP
* Gmail SMTP

## Requirements

Install the required Python package:

```bash
pip install pandas openpyxl
```

## Project Structure

```text
.
├── email_sender.py       # Main Python script
├── email.xlsx            # Excel file containing recipient email addresses
├── config.json            # Email configuration (DO NOT upload to GitHub)
├── config.example.json    # Example configuration file
└── README.md              # Project documentation
```

## Excel File Format

The `email.xlsx` file should contain a column named:

```text
Emails
```

Example:

| Emails                                          |
| ----------------------------------------------- |
| [example1@gmail.com](mailto:example1@gmail.com) |
| [example2@gmail.com](mailto:example2@gmail.com) |
| [example3@gmail.com](mailto:example3@gmail.com) |

## Configuration

Create a `config.json` file containing your email credentials:

```json
{
  "params": {
    "email": "your_email@gmail.com",
    "password": "your_app_password"
  }
}
```

**Security:** Never upload your real `config.json` or email password to GitHub.

Create a safe `config.example.json` instead:

```json
{
  "params": {
    "email": "your_email@gmail.com",
    "password": "your_app_password"
  }
}
```

## How to Run

1. Clone or download the repository.

2. Open the project folder in VS Code.

3. Install the required packages:

```bash
pip install pandas openpyxl
```

4. Add your recipient email addresses to `email.xlsx`.

5. Create your own `config.json` with your email credentials.

6. Run the Python program:

```bash
python email_sender.py
```

## How It Works

1. The program imports the required Python modules.
2. It reads the email credentials from `config.json`.
3. It loads the recipient list from `email.xlsx`.
4. It connects to Gmail's SMTP server.
5. It starts a secure TLS connection.
6. It logs into the configured email account.
7. It creates the email subject and message.
8. It loops through all email addresses in the Excel file.
9. It sends the email to each recipient.
10. Finally, it closes the SMTP connection.

## Main Python Modules

* **JSON:** Used to read email configuration details.
* **Pandas:** Used to read and process the Excel file.
* **SMTP:** Used to connect to Gmail's email server and send emails.

## Security Note

Never share your email password, API keys, or other sensitive credentials in a public GitHub repository.

Add the following to `.gitignore`:

```text
config.json
*.pyc
__pycache__/
```


LinkedIn URL:https://www.linkedin.com/posts/josna-johnson-894a29392_python-softwaredevelopment-emailautomation-activity-7491850336836710400-T3Kf?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGCdu7AB3McqJazzcJ3w2cmEvw-1JU5jJNc
