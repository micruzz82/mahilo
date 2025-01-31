from mahilo.agent import BaseAgent
from typing import List, Dict, Any
from fastapi import WebSocket

class SynthesisAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            type='synthesis_agent',
            name='synthesis_agent',
            description="This helper makes a short story from all the words.",
        )

    def generate_summary(self, text: str) -> str:
        """Generates a summary."""
        print(f"SynthesisAgent: generate_summary called with: {text}")  # for debugging
        summary = f"Summary: {text}"
        return summary

    async def process_queue_message(self, message: Dict[str, str] = None, websockets: List[WebSocket] = []) -> None:
        """Process a message and generate a summary."""
        if not message:
            return
        
        if not isinstance(message, dict) or "sender" not in message or "content" not in message:
             print(f"Error: Invalid message format for SynthesisAgent. Message must be a dictionary with 'sender' and 'content' keys. Message: {message}")
             return
        
        if message and "abstraction_agent" not in message["sender"]:
             print(f"Error: Invalid message format for SynthesisAgent. Message must contain `abstraction_agent`. Message: {message}")
             return
        
        summary = self.generate_summary(message["content"])

        # Validate the output before sending
        if not isinstance(summary, str) or "Summary:" not in summary:
            print(f"Error: Invalid output from SynthesisAgent. Message: {summary}")
            return
        
        for ws in websockets:
            await ws.send_text(summary)
        print(f"In process_queue_message: Response for {self.name}: {summary}")