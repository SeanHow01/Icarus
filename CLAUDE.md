# Icarus — Jarvis-like AI Assistant Project

## Project Overview
Building a suite of AI agents and a voice interface powered by Claude, inspired by Jarvis from Iron Man.

## Structure
- `/agent` — Autonomous Claude agent (Python, Anthropic SDK)
- `/voice-frontend` — Browser-based voice + text interface with Flask backend
- `setup-mcp-servers.sh` — Script to configure MCP servers for Claude Code

## Key Rules
- Never commit .env files (API keys)
- Financial system agents should be INPUT ONLY — no approval/submission permissions
- All agent actions should be logged for audit purposes

## Tech Stack
- Python 3.10+
- Anthropic Python SDK
- Flask (voice backend)
- Web Speech API (browser voice)
