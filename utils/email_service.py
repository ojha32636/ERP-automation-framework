

import os
import re
import json

import mailslurp_client
from dotenv import load_dotenv

load_dotenv()


class EmailService:
    def __init__(self):
        api_key = os.getenv("MAILSLURP_API_KEY")

        if not api_key:
            raise RuntimeError(
                "MAILSLURP_API_KEY is missing from .env"
            )

        configuration = mailslurp_client.Configuration()
        configuration.api_key["x-api-key"] = api_key

        self.client = mailslurp_client.ApiClient(configuration)
        self.wait_api = mailslurp_client.WaitForControllerApi(
            self.client
        )

    
  
    def wait_for_reset_email(self, recipient, timeout=60_000):
        import json
        import time

        inbox_api = mailslurp_client.InboxControllerApi(self.client)

        # Read inboxes as raw JSON to bypass the SDK enum issue.
        response = inbox_api.get_all_inboxes(
            _preload_content=False
        )

        data = json.loads(response.data.decode("utf-8"))
        inboxes = data.get("content", [])

        inbox = next(
            (
            item for item in inboxes
            if item.get("emailAddress", "").lower()
            == recipient.lower()
            ),
            None,
        )

        if inbox is None:
            raise ValueError(
                f"No MailSlurp inbox found for: {recipient}"
            )

        print(f"Waiting for reset email in: {recipient}")

        # Poll for the latest email without deserializing inbox models.
        deadline = time.monotonic() + timeout / 1000

        while time.monotonic() < deadline:
            email_response = inbox_api.get_emails(
            inbox_id=inbox["id"],
            _preload_content=False,
        )

        email_data = json.loads(
            email_response.data.decode("utf-8")
        )

        emails = (
            email_data.get("content", [])
            if isinstance(email_data, dict)
            else email_data
        )

        for item in emails:
            subject = item.get("subject") or ""
            if "reset" in subject.lower() or "password" in subject.lower():
                email_id = item.get("id")

                # Fetch the email content using its ID.
                email_api = mailslurp_client.EmailControllerApi(
                    self.client
                )
                raw_email = email_api.get_email(
                    email_id=email_id,
                    _preload_content=False,
                )

                return json.loads(
                    raw_email.data.decode("utf-8")
                )

        time.sleep(2)

        raise TimeoutError(
        f"No password-reset email received by {recipient} "
        f"within {timeout // 1000} seconds."
    )





    
    def extract_reset_url(self, email):
        import re

        content = (
        email.get("body", "")
        or email.get("bodyExcerpt", "")
        or ""
        )

        urls = re.findall(r'https?://[^\s<>"\']+', content)

        for url in urls:
            url = url.rstrip(".,);]")

        if "reset" in url.lower() or "password" in url.lower():
            return url

        raise ValueError(
        "No password-reset URL found in the email body."
        )



    def close(self):
        self.client.close()

