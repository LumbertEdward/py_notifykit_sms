class ProviderError(Exception):
    """Base exception for provider errors."""


class ConfigurationError(ProviderError):
    """Invalid or missing configuration."""


class AuthenticationError(ProviderError):
    """Invalid or missing API key."""


class ValidationError(ProviderError):
    """Invalid request payload."""


class RateLimitError(ProviderError):
    """Provider rate limit exceeded."""


class SendError(ProviderError):
    """Failed to send email."""
