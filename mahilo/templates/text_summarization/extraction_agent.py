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
        key_phrases = f"Extracted key phrases from: {text}"
        self.chat_with_agent("abstraction_agent", key_phrases)
        return key_phrases

    async def process_queue_message(self, message: str = None, websockets: List[WebSocket] = []) -> None:
        """Process a message and pass it to the abstraction_agent."""
        if not message:
            return
        
        if not isinstance(message, str):
             print(f"Error: Invalid message format for ExtractionAgent. Message must be a string. Message: {message}")
             return
        
        if message and "extraction_agent" not in message:
            print(f"Error: Invalid message format for ExtractionAgent. Message must contain `extraction_agent`. Message: {message}")
            return

        key_phrases = self.extract_key_phrases(message)
        # Validate the output before sending
        if not isinstance(key_phrases, str) or "Extracted key phrases from:" not in key_phrases:
            print(f"Error: Invalid output from ExtractionAgent. Message: {key_phrases}")
            return

        for ws in websockets:
            await ws.send_text(key_phrases)
        print(f"In process_queue_message: Response for {self.name}: {key_phrases}")