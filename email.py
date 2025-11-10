from datetime import datetime

email = {
    "subject": "Reminder: Meeting",
    "from": "  ceo@corporation.com ",
    "to": " team_lead@outlook.com ",
    "body": "   "
}

# 2. create send date
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date


# 3. normalize email addresses
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

# 4. take login and domain
login, domain = email["from"].split("@")[0], email["from"].split("@")[1]

# 5. take short part of body
short_body = email["body"][:10]
if short_body == "":
    email["short_body"] = "Empty message"
else:
    email["short_body"] = f"{short_body}..."


# 6. create domain lists
private_domain = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']
corporate_domain = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
private_domain = list(set(private_domain))
corporate_domain = list(set(corporate_domain))
