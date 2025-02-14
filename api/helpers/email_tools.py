import asyncio
import time
from typing import Dict
from verify_email import verify_email


def mail_checker(mail: str) -> Dict[str, bool]:
    """
    Check the validity of a list of email addresses.

    :param mail: A comma-separated string of email addresses.
    :return: A dictionary where keys are email addresses, and values are boolean indicating validity.
    """
    out_data: Dict[str, bool] = {}
    mail_list = mail.split(',')
    asyncio.set_event_loop(asyncio.new_event_loop())
    for mail_id in mail_list:
        mail_id = mail_id.strip().lower()
        if mail_id and mail_id not in out_data:
            time.sleep(2)
            out_data.update({mail_id: verify_email(mail_id, timeout=10)})
    return out_data
