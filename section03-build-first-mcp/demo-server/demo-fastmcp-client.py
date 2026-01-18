import asyncio
from fastmcp import Client


async def main():
    async with Client('http://localhost:8000/mcp') as client:
        if client.is_connected:
            print("MCP client is connected")

        tools = await client.list_tools()
        print("Available tools: ")
        for tool in tools:
            print(f"{tool.name}: {tool.description}")


if __name__ == "__main__":
    asyncio.run(main())