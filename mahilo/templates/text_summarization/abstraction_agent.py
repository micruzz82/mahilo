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
        paraphrased = f"Paraphrased: {text}"
        self.chat_with_agent("synthesis_agent", paraphrased)
        return paraphrased

    async def process_queue_message(self, message: Dict[str, str] = None, websockets: List[WebSocket] = []) -> None:
        """Process a message and pass it to the synthesis_agent."""
        if not message:
            return

        if not isinstance(message, dict) or "sender" not in message or "content" not in message:
             print(f"Error: Invalid message format for AbstractionAgent. Message must be a dictionary with 'sender' and 'content' keys. Message: {message}")
             return
        if message and "extraction_agent" not in message["sender"]:
             print(f"Error: Invalid message format for AbstractionAgent. Message must contain `extraction_agent`. Message: {message}")
             return

        paraphrased = self.paraphrase_sentences(message["content"])
        # Validate the output before sending
        if not isinstance(paraphrased, str) or "Paraphrased:" not in paraphrased:
            print(f"Error: Invalid output from AbstractionAgent. Message: {paraphrased}")
            return

        for ws in websockets:
            await ws.send_text(paraphrased)
        print(f"In process_queue_message: Response for {self.name}: {paraphrased}")