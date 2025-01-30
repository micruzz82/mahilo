from mahilo.agent import BaseAgent
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
        self.chat_with_agent("abstraction_agent", f"Extracted key phrases from: {text}")
        return f"Extracted Key phrases from: {text}"