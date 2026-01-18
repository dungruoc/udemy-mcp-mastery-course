from fastmcp import FastMCP

mcp = FastMCP("Maths Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two integer numbers"""
    return a + b

@mcp.tool
def mul(a: int, b: int) -> int:
    """multiply two integer numbers"""
    return a * b

@mcp.tool
def sub(a: int, b: int) -> int:
    """make the substraction of two integer numbers"""
    return a * b

@mcp.tool
def max(a: int, b: int) -> int:
    """the greatest value of two integer numbers"""
    return a if a > b else b

@mcp.tool
def min(a: int, b: int) -> int:
    """the smallest value of two integer numbers"""
    return b if a > b else a

if __name__ == "__main__":
    mcp.run(transport="stdio")