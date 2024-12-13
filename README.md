# gaiahack
Gaia's Autonomous Hackathon - AGIverse Submission
pip install agiverse
export OPENAI_API_KEY='your-openai-api-key'
import agiverse
import requests
import os

# Initialize AGIverse agent
agent = agiverse.Agent(api_key='your-agiverse-api-key', name='AI_News_Agent')

# Set a prompt for the agent's behavior (optional)
agent.set_prompt("character.info", "This agent collects and shares trendy AI news.")

# Function to fetch AI news from NewsAPI
def get_ai_news():
    api_key = "your-newsapi-key"
    url = f"https://newsapi.org/v2/everything?q=AI&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json()['articles']
        return [{"title": article["title"], "url": article["url"]} for article in articles]
    else:
        return [{"title": "Failed to retrieve news", "url": ""}]

# Create an action to fetch and display AI news
@agent.action(action="fetch_ai_news")
async def fetch_ai_news(ctx: agiverse.ActionContext, payload):
    news = get_ai_news()
    message = "\n".join([f"{item['title']} - {item['url']}" for item in news])
    await ctx.send_result(message)

# Run the agent
agent.run()
# AI News Agent for AGIverse

This is an agent for AGIverse that collects and shares trendy AI news.

## Features
- Fetches AI news articles from NewsAPI.
- Shares the articles in a human-readable format.

## Installation

1. Install dependencies:
   ```bash
   pip install agiverse requests
python ai_news_agent.py
