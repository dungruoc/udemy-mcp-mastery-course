from fastmcp import FastMCP

import asyncio
import httpx

mcp = FastMCP("Weather Server")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get current weather condition for a location

    :param location: input location
    :type location: str
    :return: current weather condition with temperature
    :rtype: str
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{location}?format=j1")
        data = response.json()

        current = data['current_condition'][0]
        area = data['nearest_area'][0]['areaName'][0]['value']

        return f"Weather in {area}: {current['temp_C']} CelciusDeg, {current['weatherDesc'][0]['value']}"
    
@mcp.tool()
async def get_forecast(location: str) -> str:
    """
    Get 3-day weather forecast for a location
    
    :param location: input location
    :type location: str
    :return: 3-day forecast of weather condition  with temperature
    :rtype: str
    """

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{location}?format=j1")
        data = response.json()

        result = [f"{day['date']}: {day['mintempC']}-{day['maxtempC']} CelciusDeg" for day in data['weather'][:3]]
        result = [f"3-day forecast for {location}"] + result

        return '\n'.join(result)
    
if __name__ == '__main__':
    mcp.run(transport='streamable-http')