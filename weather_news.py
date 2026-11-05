import asyncio
from dotenv import load_dotenv
from ddgs import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

# Load the OPENAI_API_KEY from .env
load_dotenv()


def search_weather_news(city: str) -> str:
    """Search the web for today's weather news and forecasts for a specified city.

    Args:
        city: The name of the city to get weather news for.
    """
    results = DDGS().news(query=f"{city} weather today", max_results=5)
    return str(results)


# Ask the user for a city
city = input("Which city? ")

# Initialize the OpenAI model client
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")

# Configure the AssistantAgent with the tool and strict formatting instructions
agent = AssistantAgent(
    name="weather_news",
    model_client=model_client,
    tools=[search_weather_news],
    system_message=(
        "You are a weather news assistant. Use the search_weather_news tool to find "
        "the latest weather updates for the requested city. Always reply in exactly 3 short lines."
    ),
    reflect_on_tool_use=True,
)


async def main():
    # Run the agent stream and print output to console
    await Console(
        agent.run_stream(task=f"Find today's weather news for {city} and summarize it in exactly 3 short lines.")
    )
    # Close the model client session
    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())