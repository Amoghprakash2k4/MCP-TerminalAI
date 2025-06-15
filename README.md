# MCP-TerminalAI

**MCP-TerminalAI** is a cutting-edge, terminal-based conversational AI platform that orchestrates multiple automation and data services through natural language. Powered by advanced LLMs and the Multi-Command Protocol (MCP), it enables seamless integration with web automation, search, and third-party APIs—all from your terminal.

---

## Features

- **Conversational AI Chatbot**: Interact with your automation stack using natural language in the terminal.
- **Multi-Service Orchestration**: Connects to Airbnb, DuckDuckGo, Playwright, and more via MCP servers.
- **Contextual Memory**: Maintains conversation history for smarter, multi-step interactions.
- **Extensible Architecture**: Easily add new MCP services and tools.
- **Modern Tech Stack**: Python, LangChain, Groq LLM, MCP-Use, and more.

---

## Quickstart

### 1. Clone the Repository

```sh
git clone https://github.com/YOUR_USERNAME/mcp-terminalai.git
cd mcp-terminalai/Mcpone
```

### 2. Install Python Dependencies

```sh
pip install -r requirements.txt
# or use poetry/pipenv as per your workflow
```

### 3. Configure MCP Servers

Edit `browser_mcp.json` to define your MCP services. Example:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": ["-y", "duckduckgo-mcp-server"]
    }
  }
}
```

### 4. Run the Chatbot

```sh
python app.py
```

You'll see:
```
===== Interactive MCP Chat =====
Type 'exit' or 'quit' to end the conversation
Type 'clear' to clear conversation history
=================================
```

### 5. Example Commands

- `List me airbnb in newyork`
- `Search for best pizza places in Brooklyn`
- `Automate browser to open google.com`

---

## Project Structure

```
Mcpone/
├── app.py                # Main chatbot entry point
├── browser_mcp.json      # MCP server configuration
├── airbnb_test.py        # Example/test for Airbnb tool
├── main.py               # Simple hello-world entry
├── pyproject.toml        # Python project metadata
├── README.md             # This file
└── ...
```

---

## Requirements

- Python 3.13+
- Node.js (for MCP servers via npx)
- MCP servers (see `browser_mcp.json`)

---

## Extending

- Add new MCP services by editing `browser_mcp.json`.
- Implement new tools or agents in Python for custom workflows.

---

## License

MIT License

---

## Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq LLM](https://groq.com/)
- [MCP-Use](https://pypi.org/project/mcp-use/)
- [Playwright](https://playwright.dev/)
- [OpenBNB MCP Server](https://github.com/openbnb/mcp-server-airbnb)

---

Elevate your terminal. Automate with intelligence.  
**MCP-TerminalAI**
