import sys
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Hello from udemy-mcp-mastery-building-ai-apps-mcp-ollama!")
    print("Python version:", sys.version, sys.version_info)
    print("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
