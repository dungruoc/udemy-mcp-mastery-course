import asyncio
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient

import os

async def main():
    # Configure MCP server
    client = MCPClient.from_config_file(os.path.join(os.path.dirname(__file__), "mcp_configs.json"))


    llm = ChatOllama(model="qwen3:latest", url="http://localhost:8000")
    agent = MCPAgent(llm=llm, client=client, max_steps=20)

    # result = await agent.run("What is the weather like in Hanoi tomorrow?")
    # result = await agent.run("My son have 3 coins, I give him 2 more coins. Then he offers his mother 5 coins. How many coins does he have now? Use directly the result from tools, do not try to invent it from thinking.")
    # print(result)

    # result = await agent.run("What is the weather like in Hanoi the next 3 days?")
    # print(result)

    # result = await agent.run("What is the production of 34 and 11? What is the weather like the next 3 days in New York?")
    # print(result)

    result = await agent.run("What is the minimal temperator of the weather the next 3 days in New York?")
    print(result)

asyncio.run(main())