from mahilo import AgentManager, ServerManager
from mahilo.templates.text_summarization.extraction_agent import ExtractionAgent
from mahilo.templates.text_summarization.abstraction_agent import AbstractionAgent
from mahilo.templates.text_summarization.synthesis_agent import SynthesisAgent

# Initialize the agent manager
manager = AgentManager()

# Create the agents
extraction_agent = ExtractionAgent()
abstraction_agent = AbstractionAgent()
synthesis_agent = SynthesisAgent()

# Register the agents to the manager
manager.register_agent(extraction_agent)
manager.register_agent(abstraction_agent)
manager.register_agent(synthesis_agent)

# Initialize the server manager
server = ServerManager(manager)

# Run the server
def main():
    server.run()

if __name__ == "__main__":
    main()