# Getting Started — Complete Beginner Guide

This guide assumes you have very little coding experience. Every step is explained.

---

## What Are We Building?

We're building two things:

1. **A Jarvis Agent** — A Python script you run from your terminal. You give it a task
   in plain English and it figures out what tools to use to complete it.

2. **A Voice Interface** — A web page you open in your browser. You click a glowing
   circle, speak to it, and it talks back — like Jarvis from Iron Man.

Both of these talk to Claude (the AI) using an API key you'll set up.

---

## PART 1: Setting Up Your Computer

### Step 1: Check if Python is installed

**What this does:** Python is the programming language our code is written in.
Your computer might already have it.

Open your terminal:
- **Mac:** Press Cmd + Space, type "Terminal", press Enter
- **Windows:** Press the Windows key, type "Command Prompt" or "PowerShell", press Enter

Then type:

```bash
python3 --version
```

You should see something like `Python 3.12.1`. Any version 3.10 or higher is fine.

**If you don't have Python:**
- **Mac:** Go to https://www.python.org/downloads/ and download the latest version
- **Windows:** Same link. During install, CHECK THE BOX that says "Add Python to PATH"
  (this is important — without it, your terminal won't find Python)

After installing, close and reopen your terminal, then try `python3 --version` again.

---

### Step 2: Check if pip is installed

**What this does:** pip is Python's package manager — it lets you install libraries
(pre-built code that other people wrote, so you don't have to write everything
from scratch).

```bash
pip3 --version
```

You should see something like `pip 23.2.1`. If not, run:

```bash
python3 -m ensurepip --upgrade
```

---

### Step 3: Navigate to your project folder

**What this does:** Your terminal starts in a default location (usually your home
folder). You need to tell it where your project files are.

```bash
cd ~/Icarus
```

**What `cd` means:** "change directory" — it moves you into a folder.
The `~` symbol means "my home folder".

To check you're in the right place:

```bash
ls
```

**What `ls` means:** "list" — it shows all files and folders in your current location.

You should see: `agent/`, `voice-frontend/`, `README.md`, etc.

---

### Step 4: Install the required libraries

**What this does:** Downloads and installs the Python libraries our code needs.

```bash
pip3 install anthropic python-dotenv flask flask-cors
```

**What each library does:**
- `anthropic` — Lets your code talk to Claude's AI
- `python-dotenv` — Reads your API key from a file so you don't hardcode it
- `flask` — A lightweight web server (handles the voice interface backend)
- `flask-cors` — Lets your browser talk to your Flask server (browsers block this
  by default for security)

You'll see a bunch of download progress. Wait until it says "Successfully installed".

---

## PART 2: Getting Your API Key

### Step 5: Create an Anthropic account

**What this does:** The API key is like a password that lets your code access Claude.
This is separate from your Claude Pro subscription.

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. You may need to add payment info (API usage is pay-as-you-go, separate from Pro)

---

### Step 6: Create an API key

1. In the Anthropic console, click "API Keys" in the left sidebar
2. Click "Create Key"
3. Give it a name like "Icarus Jarvis"
4. Copy the key — it starts with `sk-ant-`
5. IMPORTANT: Save this somewhere safe. You won't be able to see it again.

---

### Step 7: Save your API key in the project

**What this does:** Creates a `.env` file that stores your API key. The code reads
from this file, so your key never appears in the actual code.

```bash
cd ~/Icarus/agent
cp .env.example .env
```

**What `cp` means:** "copy" — it makes a copy of the example file.

Now open the `.env` file in a text editor:

- **Mac:** `open -a TextEdit .env`
- **Windows:** `notepad .env`
- **Or:** Open it in any text editor you like

Replace the placeholder with your actual key:

```
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

Save and close the file.

**Why a .env file?** If you ever share your code (on GitHub, etc.), the `.gitignore`
file we set up will prevent your `.env` from being uploaded. This keeps your key
private.

---

## PART 3: Running the Jarvis Agent

### Step 8: Test the agent

**What this does:** Runs the Jarvis agent with a simple task. The agent will use
Claude to figure out what to do, use tools (like reading files), and give you
an answer.

```bash
cd ~/Icarus
python3 agent/jarvis_agent.py "What files are in this project?"
```

**What you should see:**
```
==================================================
  JARVIS — Task: What files are in this project?
==================================================

  [Using tool: list_files]
Jarvis: Here are the files in your project: README.md, agent/, voice-frontend/ ...

==================================================
```

**How it works behind the scenes:**
1. Your code sends your question to Claude via the API
2. Claude decides it needs to list files, so it asks to use the `list_files` tool
3. Your code runs that tool and sends the results back to Claude
4. Claude reads the results and writes a human-friendly answer
5. This loop continues until Claude has enough info to answer

Try some more:

```bash
python3 agent/jarvis_agent.py "Read the README and summarise it"
python3 agent/jarvis_agent.py "What time is it?"
```

---

## PART 4: Running the Voice Interface

### Step 9: Copy your API key to the voice frontend folder

```bash
cp ~/Icarus/agent/.env ~/Icarus/voice-frontend/.env
```

This gives the voice backend access to the same API key.

---

### Step 10: Start the backend server

**What this does:** Starts a small web server on your computer. Your browser will
send voice/text messages to this server, which forwards them to Claude and sends
back the reply.

Open a terminal and run:

```bash
cd ~/Icarus/voice-frontend
python3 server.py
```

You should see:

```
Jarvis voice backend running on http://localhost:5000
```

**IMPORTANT:** Leave this terminal running. Don't close it. The server needs to
stay running while you use the voice interface.

**What "localhost:5000" means:** "localhost" means "this computer" and "5000" is
the port number (like a door number). Your browser will knock on this door to
talk to the server.

---

### Step 11: Open the voice interface in your browser

**Option A — Double click:**
Find the file `Icarus/voice-frontend/jarvis.html` in your file browser and
double-click it. It will open in your default web browser.

**Option B — From a second terminal:**

```bash
# Mac
open ~/Icarus/voice-frontend/jarvis.html

# Windows
start ~/Icarus/voice-frontend/jarvis.html

# Linux
xdg-open ~/Icarus/voice-frontend/jarvis.html
```

---

### Step 12: Talk to Jarvis

You should see a dark screen with a glowing blue circle that says "Tap to speak".

**To use voice:**
1. Click the glowing orb
2. It turns green and says "Listening..."
3. Speak your question (e.g. "What can you help me with?")
4. It turns yellow ("Thinking...") while Claude processes
5. It turns blue ("Speaking...") and reads the answer out loud

**To use text:**
Just type in the text box at the bottom and press Enter or click Send.

**If voice doesn't work:**
- Your browser may ask for microphone permission — click "Allow"
- Some browsers (especially on Windows) have limited speech support
- Chrome works best for voice features
- The text input always works as a fallback

---

## PART 5: MCP Servers (Optional, For Claude Code Users)

### Step 13: Connect MCP servers

**What this does:** MCP servers are plugins that give Claude Code (the tool you're
in right now) access to external services like GitHub, your file system, etc.

**IMPORTANT:** Run this in a regular terminal, NOT inside Claude Code.

```bash
cd ~/Icarus
./setup-mcp-servers.sh
```

If you get a "permission denied" error:

```bash
chmod +x setup-mcp-servers.sh
./setup-mcp-servers.sh
```

**What `chmod +x` means:** It marks the file as "executable" — telling your
computer "yes, you're allowed to run this as a program".

After running, open Claude Code and type `/mcp` to see your connected servers
and authenticate with GitHub.

---

## Troubleshooting

### "command not found: python3"
Python isn't installed or isn't in your PATH. Reinstall from python.org and make
sure to check "Add to PATH" during installation.

### "ModuleNotFoundError: No module named 'anthropic'"
You haven't installed the libraries yet. Run:
`pip3 install anthropic python-dotenv flask flask-cors`

### "Error: Could not resolve authentication"
Your API key is wrong or missing. Check your `.env` file — make sure there are
no extra spaces or quotes around the key.

### "I cannot reach the backend. Is server.py running?"
The Flask server isn't running. Open a terminal and run:
`cd ~/Icarus/voice-frontend && python3 server.py`

### The voice interface doesn't hear me
- Use Chrome (best browser for voice)
- Check that you allowed microphone access when prompted
- Make sure your microphone is working (test it in your system settings)

### The voice sounds robotic
That's your browser's built-in text-to-speech. Quality varies by operating system.
macOS generally sounds best. You could upgrade this later with a dedicated
text-to-speech service.

---

## What's Next?

Now that you have this working, some things you could build next:

- Add more tools to the agent (web search, email, calendar)
- Connect it to your financial system (start with read-only first!)
- Add conversation memory so Jarvis remembers previous chats
- Run the agent on a schedule to monitor things automatically

Ask Claude Code to help you with any of these — that's what it's here for.
