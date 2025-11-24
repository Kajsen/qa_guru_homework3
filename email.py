from datetime import datetime

email = {
    "subject": "   ",
    "from": "   alex@business.net ",
    "to": "   hr@company.ru ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!",
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
private_domain = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate_domain = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]
private_domain = list(set(private_domain))
corporate_domain = list(set(corporate_domain))

# 7. check domains crossing
for i in private_domain:
    if i in corporate_domain:
        print(i)

# 8. check if domain is corporate
is_corporate = False
if domain in corporate_domain:
    is_corporate = True

# 9. clean text
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")

# 10. sent letter
email["subject"] = email["subject"].strip()
email["sent_text"] = (
    f"From: {email["from"]}\nTo: {email["to"]}\nSubject:"
    f" {email["subject"]}\nData: {send_date}\n"
    f"{email["clean_body"]}"
)

# 11. page count
pages = (len(email["sent_text"]) + 499) // 500

# 12. empty subject and body
is_subject_empty = not email["subject"]
is_body_empty = not email["body"]

# 13. email masked form
email["masked_from"] = f"{login[:2]}***@{domain}"

# 14. delete personal domain
private_domain.remove("list.ru")
private_domain.remove("bk.ru")


print("Resulting email")
for key in email.keys():
    print(key + ": " + email.get(key))

print("=" * 100)
print("Private domains: " + ", ".join(private_domain))
print("Corporate domain: " + ", ".join(corporate_domain))
print(f"Pages: {pages}")
