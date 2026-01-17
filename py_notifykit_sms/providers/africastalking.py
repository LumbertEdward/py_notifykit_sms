import africastalking
from py_notifykit_sms.core import SMSProvider
from py_notifykit_sms.exceptions import ConfigurationError, SendError


class AfricaTalkingSMSProvider(SMSProvider):

    def __init__(self, username: str, api_key: str, sender_id: str | None = None):
        if not username or not api_key:
            raise ConfigurationError("Africa's Talking credentials are required")

        africastalking.initialize(username=username, api_key=api_key)
        self.sms = africastalking.SMS
        self.sender_id = sender_id

    def send(self, recipients: list[str], message: str):
        try:
            return self.sms.send(message, recipients, self.sender_id)
        except Exception as exc:
            raise SendError("Failed to send SMS via Africa's Talking") from exc

    def send_bulk(self, messages: list[dict]) -> list[dict]:
        responses = []
        for msg in messages:
            try:
                response = self.sms.send(
                    msg["message"], [msg["recipient"]], self.sender_id
                )
                responses.append(response)
            except Exception as exc:
                responses.append({"recipient": msg["recipient"], "error": str(exc)})
        return responses
