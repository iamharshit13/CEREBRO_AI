import os
import requests

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

class LLMAdapter:
    def __init__(self, provider: str = 'openai'):
        self.provider = provider

    def call(self, prompt: str, max_tokens: int = 512, temperature: float = 0.2):
        # If OPENAI_API_KEY not set, return a mocked response to help dev flow
        if not OPENAI_API_KEY:
            return "(mocked response) This is a placeholder. Set OPENAI_API_KEY to call real API."

        url = 'https://api.openai.com/v1/chat/completions'
        headers = {'Authorization': f'Bearer {OPENAI_API_KEY}'}
        payload = {
            'model': 'gpt-4o-mini',
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': prompt}
            ],
            'max_tokens': max_tokens,
            'temperature': temperature
        }
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()
        # minimal defensive parsing
        return data.get('choices', [])[0].get('message', {}).get('content', '')
