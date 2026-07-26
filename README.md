# Express API Python SDK

[![PyPI](https://img.shields.io/badge/pypi-gptapi-blue)](https://pypi.org/project/gptapi/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Python SDK for **[Express API](https://gptapi.net.cn)** — access **34 Chinese LLMs** from 9 providers through a single OpenAI-compatible API. **Cheaper than OpenRouter, with exclusive models.**

## Why Express API?

| | Express API | OpenRouter |
|---|---|---|
| **Pricing** | 10-20% cheaper | Baseline |
| **Doubao (豆包)** | ✅ Exclusive | ❌ |
| **ERNIE (文心)** | ✅ Exclusive | ❌ |
| **Hunyuan (混元)** | ✅ Exclusive | ❌ |
| **Payment** | Stripe ($0 min) | Stripe/Crypto |
| **API Format** | OpenAI-compatible | OpenAI-compatible |

## Quick Start

### 1. Install

```bash
pip install gptapi
```

### 2. Get an API Key

Register at **[gptapi.net.cn](https://gptapi.net.cn)** → get your API key from the dashboard. **$1 free credit** to start.

### 3. Use it (30 seconds)

```python
from gptapi import GPTAPI

client = GPTAPI(api_key="your-api-key")

# Simple chat
response = client.chat("Explain quantum computing in one sentence")
print(response)

# Use a specific model
response = client.chat("写一首关于春天的诗", model="qwen-max")

# Streaming
for chunk in client.chat_stream("Tell me a story about AI"):
    print(chunk, end="")

# List all available models
print(client.models())
```

### 4. Drop-in OpenAI Replacement

Already using OpenAI's Python SDK? Just change 2 lines:

```python
# Before: OpenAI
from openai import OpenAI
client = OpenAI(api_key="...")

# After: Express API (keep the same code!)
from openai import OpenAI
client = OpenAI(
    api_key="your-gptapi-key",
    base_url="https://gptapi.net.cn/v1"
)
```

## Available Models (34 total)

| Provider | Models |
|----------|--------|
| **DeepSeek** | deepseek-v3, deepseek-v3.1, deepseek-r1, deepseek-v4-flash |
| **Kimi/Moonshot** | kimi-k2.5, kimi-k2.6, kimi-k2.7-code, kimi-k3 |
| **Qwen/Alibaba** | qwen-max, qwen-plus, qwen-turbo, qwen3-max, qwen3.7-max |
| **Doubao/ByteDance** ⭐ | doubao-1.5-pro-32k, doubao-1.5-pro-256k |
| **GLM/Zhipu** | glm-4.7, glm-5, glm-5.1, glm-5.2 |
| **ERNIE/Baidu** ⭐ | ernie-4.0-turbo, ernie-4.5 |
| **MiniMax** | minimax-m2.1, minimax-m2.5, minimax-m3 |
| **MiMo/Xiaomi** | mimo-v2.5-pro |
| **Hunyuan/Tencent** ⭐ | hunyuan-turbo, hunyuan-pro |

⭐ = Exclusive to Express API (not on OpenRouter)

## Pricing

Full pricing at **[gptapi.net.cn/docs](https://gptapi.net.cn/docs)**. All prices in USD, Stripe checkout. $1 minimum to start.

## License

MIT
