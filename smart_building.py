import agiverse
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys and Building ID from environment variables
AGIVERSE_API_KEY = os.getenv('AGIVERSE_API_KEY')
BUILDING_ID = os.getenv('BUILDING_ID')
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')

# Initialize Smart Building client
building = agiverse.SmartBuilding(api_key=AGIVERSE_API_KEY, building_id=BUILDING_ID)

# Function to fetch AI news from NewsAPI
def get_ai_news():
    url = f"https://newsapi.org/v2/everything?q=AI&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [{"title": article["title"], "url": article["url"]} for article in articles]
    else:
        return [{"title": "Failed to retrieve news", "url": ""}]

# Event handler to know when the building is ready
@building.event
async def on_ready():
    print(f"Smart building {building.building_id} is ready to use")

# Action to fetch and display AI news
@building.action(
    action="fetch_ai_news", 
    action_description="Fetch trending AI news from external sources.", 
    payload_description="{}"
)
async def fetch_ai_news(ctx: agiverse.ActionContext, payload):
    news = get_ai_news()
    message = "\n".join([f"{item['title']} - {item['url']}" for item in news])
    # Sending the result back to the player
    await ctx.send_result(message)

# Run the smart building
building.run()
