from mahilo.agent import BaseAgent

class AbstractionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            type='abstraction_agent',
            name='abstraction_agent',
            description="This helper says important things in a a different way.",
        )
    def paraphrase_sentences(self, text: str) -> str:
        """Paraphrases the sentences."""
        print(f"AbstractionAgent: paraphrase_sentences called with: {text}") # for debugging
        self.chat_with_agent("synthesis_agent", f"Paraphrased: {text}")
        return f"Paraphrased sentences for {text}"