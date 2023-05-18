import os
from openai.error import APIError, InvalidRequestError, OpenAIError


organization = os.environ.get("OPENAI_ORGANIZATION")
api_base = os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1")
api_type = os.environ.get("OPENAI_API_TYPE", "open_ai")
api_version = os.environ.get(
    "OPENAI_API_VERSION",
    ("2023-03-15-preview" if api_type in ("azure", "azure_ad", "azuread") else None),
)