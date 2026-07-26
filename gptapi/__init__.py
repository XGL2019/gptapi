"""
Express API Python SDK — 34 Chinese LLMs via OpenAI-compatible API.

Usage:
    from gptapi import GPTAPI
    
    client = GPTAPI(api_key="your-api-key")
    
    # Chat completion
    response = client.chat("Hello, who are you?")
    print(response)
    
    # With model selection
    response = client.chat("写一首诗", model="deepseek-v3")
    
    # Streaming
    for chunk in client.chat_stream("Tell me a story"):
        print(chunk, end="")
    
    # List available models
    models = client.models()
"""

from openai import OpenAI

BASE_URL = "https://gptapi.net.cn/v1"
DEFAULT_MODEL = "deepseek-v3"

# All available models
MODELS = {
    "deepseek": ["deepseek-v3", "deepseek-v3.1", "deepseek-r1", "deepseek-v4-flash"],
    "kimi": ["kimi-k2.5", "kimi-k2.6", "kimi-k2.7-code", "kimi-k3"],
    "qwen": ["qwen-max", "qwen-plus", "qwen-turbo", "qwen3-max", "qwen3.7-max"],
    "doubao": ["doubao-1.5-pro-32k", "doubao-1.5-pro-256k"],
    "glm": ["glm-4.7", "glm-5", "glm-5.1", "glm-5.2"],
    "ernie": ["ernie-4.0-turbo", "ernie-4.5"],
    "minimax": ["minimax-m2.1", "minimax-m2.5", "minimax-m3"],
    "mimo": ["mimo-v2.5-pro"],
    "hunyuan": ["hunyuan-turbo", "hunyuan-pro"],
}


class GPTAPI:
    """Express API client — drop-in OpenAI-compatible interface for 34 Chinese LLMs."""

    def __init__(
        self,
        api_key: str,
        base_url: str = BASE_URL,
        default_model: str = DEFAULT_MODEL,
    ):
        self.api_key = api_key
        self.default_model = default_model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def chat(
        self,
        prompt: str,
        model: str | None = None,
        system: str | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ) -> str:
        """Send a chat completion and return the response text."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        return response.choices[0].message.content

    def chat_stream(
        self,
        prompt: str,
        model: str | None = None,
        system: str | None = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ):
        """Stream a chat completion, yielding text chunks."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        stream = self.client.chat.completions.create(
            model=model or self.default_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def models(self) -> list[str]:
        """List all available model IDs."""
        all_models = []
        for models in MODELS.values():
            all_models.extend(models)
        return sorted(all_models)

    def models_by_provider(self) -> dict[str, list[str]]:
        """List models grouped by provider."""
        return dict(MODELS)
