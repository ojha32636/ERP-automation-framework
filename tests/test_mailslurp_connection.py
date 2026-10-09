

import json
import os

import mailslurp_client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MAILSLURP_API_KEY")

if not api_key:
    raise RuntimeError("MAILSLURP_API_KEY is missing from .env")

configuration = mailslurp_client.Configuration()
configuration.api_key["x-api-key"] = api_key


def test_mailslurp_can_receive_email():
    with mailslurp_client.ApiClient(configuration) as client:
        inbox_api = mailslurp_client.InboxControllerApi(client)
        wait_api = mailslurp_client.WaitForControllerApi(client)

        # Create an inbox and receive the raw HTTP response.
        # This avoids the outdated account_region enum validation.
        response = inbox_api.create_inbox_with_defaults(
            _preload_content=False
        )

        inbox_data = json.loads(response.data.decode("utf-8"))

        inbox_id = inbox_data["id"]
        inbox_email = inbox_data["emailAddress"]

        print(f"Test inbox: {inbox_email}")

        # Send a test email to the new inbox.
        inbox_api.send_email_and_confirm(
            inbox_id=inbox_id,
            send_email_options=mailslurp_client.SendEmailOptions(
                to=[inbox_email],
                subject="MailSlurp connection test",
                body="Email testing is working!",
            ),
        )

        # Wait for the email to arrive.
        email = wait_api.wait_for_latest_email(
            inbox_id=inbox_id,
            timeout=60_000,
            unread_only=True,
        )

        assert "MailSlurp connection test" in email.subject
        assert "Email testing is working!" in email.body