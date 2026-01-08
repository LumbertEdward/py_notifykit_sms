import base64
import requests
from typing import List, Dict

from py_notifykit_sms.core import SMSProvider
from py_notifykit_sms.exceptions import ConfigurationError, SendError


class SMSLeopardSMSProvider(SMSProvider):
    BASE_URL = "https://api.smsleopard.com/v1/sms/send"

    def __init__(
        self,
        api_key: str,
        api_secret: str,
        sender_id: str,
        timeout: int = 10,
    ):
        if not api_key or not api_secret:
            raise ConfigurationError("SMS Leopard API key and secret are required")

        if not sender_id:
            raise ConfigurationError("SMS Leopard sender_id is required")

        credentials = f"{api_key}:{api_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        self.headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json",
        }
        self.sender_id = sender_id
        self.timeout = timeout

    @staticmethod
    def _normalize_phone_number(phone: str) -> str:
        """
        Normalize phone numbers to international format.
        Mirrors the JS implementation.
        """
        phone = phone.replace(" ", "")

        if phone.startswith("0"):
            return f"254{phone[1:]}"
        if phone.startswith("2"):
            return f"{phone}"
        if phone.startswith("+"):
            return phone[1:]
        return phone

    def send(self, recipients: List[str], message: str):
        if not recipients:
            raise SendError("At least one recipient is required")

        try:
            destinations = [
                {"number": self._normalize_phone_number(phone)} for phone in recipients
            ]

            payload = {
                "message": message,
                "source": self.sender_id,
                "destination": destinations,
            }

            response = requests.post(
                self.BASE_URL,
                json=payload,
                headers=self.headers,
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json()

        except requests.RequestException as exc:
            raise SendError("Failed to send SMS via SMS Leopard") from exc

    def send_bulk(self, messages: List[Dict]) -> List[Dict]:
        responses = []

        for msg in messages:
            try:
                response = self.send(
                    recipients=[msg["recipient"]],
                    message=msg["message"],
                )
                responses.append(response)
            except Exception as exc:
                responses.append(
                    {
                        "recipient": msg.get("recipient"),
                        "error": str(exc),
                    }
                )

        return responses
