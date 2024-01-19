from fastapi import FastAPI
from helpers import mail_checker

app = FastAPI()


@app.get('/email_verify/')
def email_verify(emails: str):
    result = mail_checker(emails)
    return result
