# notifykit 📲

**notifykit** is a provider-agnostic Python notification toolkit that enables developers to send SMS (and other notifications) through a unified, extensible API.

It abstracts away provider-specific SDKs and APIs, making it easy to switch providers or add new notification channels without rewriting application logic.

> **One interface. Multiple notification providers.**

---

## Features

- 🔌 Pluggable notification providers
- 📩 SMS support (Africa’s Talking)
- 🧩 Clean, provider-agnostic API
- 🔁 Easy provider switching
- ⚙️ Framework-friendly (FastAPI, Django, Flask)
- 🚀 Designed for future channels (Email, WhatsApp, Push)

---

## Installation

```bash
pip install notifykit
```

---

## Usage

## Initialize an SMS provider

---

```bash
from notifykit.providers.africastalking import AfricaTalkingSMSProvider

sms = AfricaTalkingSMSProvider(
    username="your_username",
    api_key="your_api_key",
    sender_id="SENDER_ID"
)
```

---

## Sending an SMS

---

```bash
response = sms.send(
    recipients=["+254712345678"],
    message="Hello! This message was sent using notifykit."
)
```

---

## Sending to multiple recipients

---

```bash
response = sms.send_bulk([
        {
            message="Bulk SMS via notifykit 🚀",
            recepient="+254712345678"
        }
    ]
)
```

---

## Provider Response

notifykit returns the raw provider response to allow flexibility, while standardizing error handling.

---

```bash
{
    "SMSMessageData": {
        "Recipients": [
            {
                "statusCode": 101,
                "number": "+254712345678",
                "status": "Success",
                "messageId": "ATXid_123",
                "cost": "KES 0.80"
            }
        ]
    }
}
```

---

## Error Handling

Provider-specific errors are translated into notifykit exceptions.

---

```bash

from notifykit.exceptions import AuthenticationError, SendError

try:
    sms.send(...)
except AuthenticationError:
    # Invalid API key or credentials
    pass
except SendError as exc:
    # Failed to send SMS
    pass

```

---

## Supported Providers

---

✅ Africa’s Talking
