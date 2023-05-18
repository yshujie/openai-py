from enum import Enum

import openai

class ApiType(Enum):
    AZURE = 1
    OPEN_AI = 2
    AZURE_AD = 3

    @staticmethod
    def from_str(label):
        if label.lower() == 'azure':
            return ApiType.AZURE
        elif label.lower() in ("azure_ad", "azuread"):
            return ApiType.AZURE_AD
        elif label.lower() in ("open_ai", "openai"):
            return ApiType.OPEN_AI
        else:
            raise openai.error.InvalidAPIType(
                "The API type provided in invalid"
            )