# AutoGen Weather News Agent

An AI assistant built with AutoGen that takes a city name from the user, retrieves the latest live weather updates using keyless DuckDuckGo search, and summarizes the forecast in exactly three short lines[cite: 1].

---

## Features

- **Tool Calling**: Connects an AutoGen `AssistantAgent` to a custom Python tool function[cite: 1, 2].
- **Keyless Web Search**: Utilizes `ddgs` to pull live weather news without requiring a dedicated search API key[cite: 1].
- **Reflective Tool Output**: Configured with `reflect_on_tool_use=True` to digest search outputs and generate natural responses instead of dumping raw text[cite: 1].
- **Strict Formatting**: Enforces an exact 3-line summary format for every query[cite: 1].

---

## Project Structure

```text
weather-news-agent/
├── .env                  # API keys (excluded from git)
├── .gitignore            # Excludes .env and .venv
├── weather_news.py       # Main application script
├── README.md             # Project documentation
└── requirements.txt      # Project dependencies
