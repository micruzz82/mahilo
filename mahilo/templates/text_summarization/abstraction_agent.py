from mahilo.agent import BaseAgent
from typing import List, Dict, Any
from fastapi import WebSocket

class AbstractionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            type='abstraction_agent',
            name='abstraction_agent',
            description="This helper says important things in a different way.",
        )

    def paraphrase_sentences(self, text: str) -> str:
        """Paraphrases the sentences."""
        print(f"AbstractionAgent: paraphrase_sentences called with: {text}")  # for debugging
        paraphrased = "Paraphrased: " + text
        self.chat_with_agent("synthesis_agent", paraphrased)
        return paraphrased

    async def process_chat_message(self, message: str = None, websockets: List[WebSocket] = []) -> Dict[str, Any]:
        """Process a message and pass it to the synthesis_agent."""
        if not message:
            return {"response": "", "activated_agents": []}

        paraphrased = self.paraphrase_sentences(message)
        response = f"AbstractionAgent: {paraphrased}"
        return {
            "response": response,
            "activated_agents": ["synthesis_agent"]
        }