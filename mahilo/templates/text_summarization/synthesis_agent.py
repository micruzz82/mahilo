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
        summary = "Summary: " + text
        return summary

    async def process_chat_message(self, message: str = None, websockets: List[WebSocket] = []) -> Dict[str, Any]:
        """Process a message and generate a summary."""
        if not message:
            return {"response": "", "activated_agents": []}

        summary = self.generate_summary(message)
        response = f"SynthesisAgent: {summary}"
        return {
            "response": response,
            "activated_agents": []
        }