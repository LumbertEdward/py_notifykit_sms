from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class SMSProvider(ABC):

    @abstractmethod
    def send(self, recipients: List[str], message: str) -> Dict:
        pass

    @abstractmethod
    def send_bulk(self, messages: List[Dict[str, str]]) -> List[Dict]:
        pass
