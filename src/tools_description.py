from src.functions import (
    add_two_numbers,
    subtract_two_numbers,
    multiply_two_numbers,
    divide_two_numbers,
    total
)

add_tool = {
    "name": "add_two_numbers",
    "description": "Add two numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer", "description": "The first number"},
            "b": {"type": "integer", "description": "The second number"},
        },
        "required": ["a", "b"],
    },
}

subtract_tool = {
    "name": "subtract_two_numbers",
    "description": "Subtract two numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "integer"},
        },
        "required": ["a", "b"],
    },
}

multiply_tool = {
    "name": "multiply_two_numbers",
    "description": "Multiply two numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "integer"},
            "b": {"type": "integer"},
        },
        "required": ["a", "b"],
    },
}

divide_tool = {
    "name": "divide_two_numbers",
    "description": "Divide two numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"},
        },
        "required": ["a", "b"],
    },
}

total_tool = {
    "name": "total",
    "description": "Calculate total of several numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "nums": {
                "type": "array",
                "items": {"type": "integer"},
                "description": "List of numbers to sum",
            },
        },
        "required": ["nums"],
    },
}

all_tools = [
    add_tool,
    subtract_tool,
    multiply_tool,
    divide_tool,
    total_tool,
]
