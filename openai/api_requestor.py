import openai
from openai import util
from openai.util import ApiType


class APIRequestor:
    def __init__(
            self,
            key=None,
            api_base=None,
            api_type=None,
            api_version=None,
            organization=None,
    ):
        self.api_base = api_base or openai.api_base
        self.api_key = key or util.default_api_key()
        self.api_type = (
            ApiType.from_str(api_type)
            if api_type
            else ApiType.from_str(openai.api_type)
        )
        self.api_version = api_version or openai.api_version
        self.organization = organization or openai.organization