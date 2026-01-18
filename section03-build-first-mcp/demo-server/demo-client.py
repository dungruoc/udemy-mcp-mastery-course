import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    server_url = 'http://localhost:8000/mcp'

    async with streamablehttp_client(server_url) as (read, write, get_session_id):
        async with ClientSession(read, write) as session:
            print("Start: ",get_session_id())
            
            await session.initialize()
            sid = get_session_id()
            print("Session ID: ", sid)

            result = await session.call_tool("add", {'a': 1, 'b': 2})
            print("session result: ", result)


if __name__ == "__main__":
    asyncio.run(main())