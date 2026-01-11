# Set-Up

- install Anaconda, Ollama
- install NodeJs, Npm
- install Claude Desktop
- install Uv

# Init project with UV

```bash
$ uv init
$ uv add numpy requests
$ uv tree              
Resolved 9 packages in 15ms
udemy-mcp-mastery-building-ai-apps-mcp-ollama v0.1.0
├── numpy v2.0.2
└── requests v2.32.5
    ├── certifi v2026.1.4
    ├── charset-normalizer v3.4.4
    ├── idna v3.11
    └── urllib3 v2.6.3

$ uv python pin 3.11
$ uv sync
```