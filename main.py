import asyncio
import ollama
from ollama import ChatResponse

from src.functions import available_functions, all_tools
from src.funcs_description import system_prompt

model = 'llama3.2:1b'


messages = [
    {'role': 'user', 'content': 'Calculate total: 3 plus 1, 5 minus 2, 7 times 3, and eight divided by two'}
]



async def main():
    client = ollama.AsyncClient()

    response: ChatResponse = await client.chat(
        model,
        messages=messages,
        tools=list(available_functions.values()),
    )

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            func_name = tool_call.function.name
            args = tool_call.function.arguments

            if func := available_functions.get(func_name):
                print(f"Calling function: {func_name} with args: {args}")
                output = func(**args)
                print(f"Function output: {output}")
                messages.append({'role': 'tool', 'content': str(output), 'tool_name': func_name})
            else:
                print(f"Function {func_name} not found")

        final_response = await client.chat(model, messages=messages)
        print("Final response:", final_response.message.content)

    else:
        print("No tool calls returned from model")

if __name__ == '__main__':
    asyncio.run(main())
