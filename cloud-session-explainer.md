# What Is a Claude Code Cloud Session?

## The Simple Version

Think of it like **hiring a remote worker to code for you while you sleep.**

Normally, Claude Code runs *on your machine* — your laptop has to be open and running. A **cloud session** removes that requirement. You give Claude a task, it works on Anthropic's secure servers, and when it's done it opens a pull request on GitHub — all without your laptop needing to be on.

---

## Can It Connect Your Laptop, Phone, and iPad?

Yes, but not in the "Dropbox/iCloud" sense. Here's what it actually does:

| What you want                            | Does it work?                                  |
|------------------------------------------|------------------------------------------------|
| Start a coding task on your laptop       | Yes                                            |
| Check progress from your phone           | Yes — via claude.ai or the Claude mobile app   |
| Steer or give feedback from your iPad    | Yes                                            |
| Resume the session on your laptop        | Yes — use `/teleport` to pull it back locally  |
| Sync local files between devices         | No — that's not what this is for               |

You kick off work on one device and monitor/interact with it from any other device, because the work lives in the cloud — not tied to any one machine.

---

## How It Works (Step by Step)

1. You give Claude a task (from your terminal, claude.ai, or the mobile app)
2. Anthropic spins up a secure virtual machine
3. Your GitHub repo is cloned into it
4. Claude analyzes the code, makes changes, and runs tests
5. Results are pushed to a branch, ready for you to review and merge
6. You can check in at any time from any device

---

## What Can You Build / Use It For?

- **Parallel tasks** — run 5 independent bug fixes at the same time
- **Async workflows** — start a task before bed, wake up to a PR
- **Remote repos** — work on code you don't have checked out locally
- **Well-defined jobs** — "fix this failing test", "update the API docs", "refactor this module"

### Preinstalled in the cloud environment
- Languages: Python, Node.js, Ruby, Go, Rust, Java, PHP, C++
- Databases: PostgreSQL 16, Redis 7.0
- Package managers: npm, pip, cargo, bundler, maven, etc.

---

## How to Start a Cloud Session

**From your terminal:**
```bash
claude --remote "Fix the authentication bug in src/auth/login.ts"
```

**From the web:**
Go to [claude.ai/code](https://claude.ai/code), connect your GitHub account, and submit a task.

**From the mobile app:**
Use the Claude iOS or Android app to kick off or monitor tasks on the go.

---

## Key Limits to Know

- **GitHub only** — works with GitHub repos (not GitLab or Bitbucket yet)
- **Not a file sync tool** — it doesn't sync local files across your devices
- **Research preview** — features are still evolving
- Requires a Pro, Max, Team, or Enterprise Claude plan

---

## The Bottom Line

Cloud sessions are best thought of as **autonomous, cloud-based coding runs** you can start from anywhere and check on from any device. They're great for parallelizing work, running tasks overnight, and freeing you from keeping your laptop open.
