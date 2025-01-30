from mahilo.agent import BaseAgent
from typing import List, Dict, Any
from fastapi import WebSocket

class ExtractionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            type='extraction_agent',
            name='extraction_agent',
            description="This helper picks out the most important words.",
        )

    def extract_key_phrases(self, text: str) -> str:
        """Picks the key phrases."""
        print("ExtractionAgent: extract_key_phrases called")  # for debugging
        key_phrases = "Extracted key phrases from: " + text
        self.chat_with_agent("abstraction_agent", key_phrases)
        return key_phrases

    async def process_chat_message(self, message: str = None, websockets: List[WebSocket] = []) -> Dict[str, Any]:
        """Process a message and pass it to the abstraction_agent."""
        if not message:
            return {"response": "", "activated_agents": []}

        key_phrases = self.extract_key_phrases(message)
        response = f"ExtractionAgent: {key_phrases}"
        return {
            "response": response,
            "activated_agents": ["abstraction_agent"]
        }