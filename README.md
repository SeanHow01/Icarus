# Icarus

A Jarvis-inspired AI assistant built with Claude — voice interface, autonomous agents, and MCP integrations.

## Quick Start

### 1. Prerequisites
- Python 3.10+
- Node.js 18+ (for MCP servers)
- An Anthropic API key from [console.anthropic.com](https://console.anthropic.com)

### 2. Set up your API key
```bash
cd agent
cp .env.example .env
# Edit .env and paste your API key
```

### 3. Install dependencies
```bash
pip install anthropic python-dotenv flask flask-cors
```

### 4. Try the agent
```bash
python agent/jarvis_agent.py "What files are in this project?"
python agent/jarvis_agent.py "Summarise the README"
python agent/jarvis_agent.py "What time is it?"
```

### 5. Try the voice interface
```bash
# Terminal 1: Start the backend
cd voice-frontend
cp ../agent/.env .env
python server.py

# Terminal 2: Open the frontend
open voice-frontend/jarvis.html  # macOS
# or just double-click jarvis.html in your file browser
```

Click the glowing orb to speak, or type in the text box below it.

### 6. Set up MCP servers (optional)
```bash
# Run this in your regular terminal, NOT inside Claude Code
./setup-mcp-servers.sh
```

## Project Structure
```
Icarus/
├── agent/
│   ├── jarvis_agent.py      # Autonomous agent with tool use
│   ├── requirements.txt
│   └── .env.example
├── voice-frontend/
│   ├── server.py             # Flask backend (keeps API key safe)
│   └── jarvis.html           # Browser UI with voice + text
├── setup-mcp-servers.sh      # MCP server configuration
├── CLAUDE.md                 # Context file for Claude Code sessions
└── .gitignore
```
