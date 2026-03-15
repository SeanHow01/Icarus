"""
Jarvis Agent — Your first autonomous Claude agent.

This agent can:
  - Monitor a folder for new files and summarise them
  - Answer questions about files in your project
  - Run simple system checks (time, disk space, etc.)

Usage:
  1. Copy .env.example to .env and add your API key
  2. pip install -r requirements.txt
  3. python jarvis_agent.py "What files are in my project?"
  4. python jarvis_agent.py "Summarise any .md files you find"
"""

import os
import sys
from datetime import datetime

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

# --- Tool definitions (things Jarvis can do) ---

tools = [
    {
        "name": "list_files",
        "description": "List files in a directory",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Directory path to list (defaults to current directory)",
                }
            },
            "required": [],
        },
    },
    {
        "name": "read_file",
        "description": "Read the contents of a file",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to read",
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "get_system_info",
        "description": "Get current time, date, and basic system information",
        "input_schema": {
            "type": "object",
            "properties": {},
            "required": [],
        },
    },
]


# --- Tool implementations ---


def handle_tool(name: str, input_data: dict) -> str:
    if name == "list_files":
        path = input_data.get("path", ".")
        try:
            entries = os.listdir(path)
            return "\n".join(entries) if entries else "(empty directory)"
        except Exception as e:
            return f"Error: {e}"

    elif name == "read_file":
        try:
            with open(input_data["path"], "r") as f:
                content = f.read(10000)  # Cap at 10k chars for safety
            return content
        except Exception as e:
            return f"Error: {e}"

    elif name == "get_system_info":
        now = datetime.now()
        return f"Date: {now.strftime('%A %d %B %Y')}\nTime: {now.strftime('%H:%M:%S')}"

    return f"Unknown tool: {name}"


# --- Agent loop (think → act → observe → repeat) ---


def run_agent(user_task: str):
    print(f"\n{'='*50}")
    print(f"  JARVIS — Task: {user_task}")
    print(f"{'='*50}\n")

    messages = [{"role": "user", "content": user_task}]

    system_prompt = (
        "You are Jarvis, a helpful AI assistant. You are concise and direct. "
        "Use the tools available to you to complete the user's task. "
        "When you have enough information, give a clear final answer."
    )

    # Agent loop — keeps going until Claude stops calling tools
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        # Check if Claude wants to use tools
        tool_use_blocks = [b for b in response.content if b.type == "tool_use"]

        if not tool_use_blocks:
            # No tools called — Claude is done, print final answer
            for block in response.content:
                if hasattr(block, "text"):
                    print(f"Jarvis: {block.text}")
            break

        # Process each tool call
        tool_results = []
        for tool_block in tool_use_blocks:
            print(f"  [Using tool: {tool_block.name}]")
            result = handle_tool(tool_block.name, tool_block.input)
            tool_results.append(
                {
                    "type": "tool_result",
                    "tool_use_id": tool_block.id,
                    "content": result,
                }
            )

        # Feed results back to Claude and loop
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_results})

    print(f"\n{'='*50}\n")


# --- Entry point ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python jarvis_agent.py \"Your task here\"")
        print("")
        print("Examples:")
        print('  python jarvis_agent.py "What files are in this project?"')
        print('  python jarvis_agent.py "Summarise the README.md file"')
        print('  python jarvis_agent.py "What time is it?"')
        sys.exit(1)

    task = " ".join(sys.argv[1:])
    run_agent(task)
