from fastapi import FastAPI
from api.helpers import mail_checker

app = FastAPI()


@app.get('/verify_email/')
def verify_email(emails: str):
    result = mail_checker(emails)
    return result
