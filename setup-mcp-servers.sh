#!/bin/bash
# ============================================
# MCP Server Setup Script for Claude Code
# Run this in your terminal (NOT inside Claude Code)
# ============================================

echo "=== Setting up MCP Servers for Claude Code ==="
echo ""

# 1. GitHub MCP Server
# Gives Claude access to your GitHub repos, PRs, issues
echo "[1/2] Adding GitHub MCP server..."
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
echo "  ✓ GitHub MCP added. Run /mcp inside Claude Code to authenticate."
echo ""

# 2. Filesystem MCP Server
# Gives Claude broader file access beyond the current project
echo "[2/2] Adding Filesystem MCP server..."
echo "  NOTE: Edit the path below to point to your actual projects folder"
claude mcp add --transport stdio filesystem -- npx -y @modelcontextprotocol/server-filesystem "$HOME/projects"
echo "  ✓ Filesystem MCP added."
echo ""

echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Open Claude Code"
echo "  2. Type /mcp to see your connected servers"
echo "  3. Authenticate with GitHub when prompted"
echo ""
echo "Optional MCP servers you can add later:"
echo "  # Google Calendar"
echo "  claude mcp add --transport stdio gcal -- npx -y @anthropic-ai/google-calendar-mcp"
echo ""
echo "  # Notion"
echo "  claude mcp add --transport stdio notion --env NOTION_API_KEY=your-key -- npx -y @notionhq/notion-mcp-server"
echo ""
echo "  # Home Assistant (smart home)"
echo "  claude mcp add --transport stdio homeassistant --env HA_URL=http://your-ha-ip:8123 --env HA_TOKEN=your-token -- npx -y homeassistant-mcp-server"
