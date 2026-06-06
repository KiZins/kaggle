from abc import ABC, abstractmethod
from openai import OpenAI

class BaseLLM(ABC):
    def __init__(self, model_name: str, temperature: float = 0.2):
        self.model_name = model_name
        self.temperature = temperature

    @abstractmethod
    def generate(self, system_prompt: str, user_prompt: str):
        return None

class NemoLLM(BaseLLM):
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.2):

class OpenAPI(BaseLLM):
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.2):
        super().__init__(model_name, temperature)
        self.client = OpenAI() 

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=self.temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI API Error for {self.model_name}: {e}")
            return f"ERROR: Generation failed."

