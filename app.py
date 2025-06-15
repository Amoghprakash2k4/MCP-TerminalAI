import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient  # Corrected import name

async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # MCP config file path (update if needed)
    config_file = "browser_mcp.json"
    print("Initializing chat...")

    # Create MCP client and agent with memory enabled
    client = MCPClient.from_config_file(config_file)

    # Initialize LLM
    llm=ChatGroq(model="llama3-70b-8192")

    # Create the agent
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
    )

    # Start interactive loop
    print("\n===== Interactive MCP Chat =====")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")
    print("=================================\n")

    try:
        while True:
            user_input = input("\nYou: ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("👋 Ending conversation...")
                break

            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("🧹 Conversation history cleared.")
                continue

            print("Assistant is thinking...\n")
            try:
                response = await agent.run(user_input)
                print("Assistant:", response)
            except Exception as e:
                print(f"❌ Error: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
