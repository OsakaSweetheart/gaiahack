# gaiahack

Gaia's Autonomous Hackathon - AGIverse Submission

```bash
pip install agiverse requests
```

# AI News Smart Building for AGIverse

This Smart Building for AGIverse collects and shares the latest AI news, providing an interactive and informative experience for users within the AGIverse environment.

## Features
- **Fetch AI News:** Retrieves the latest AI news articles from NewsAPI.
- **Interactive Actions:** Allows users to invoke actions to get AI news directly within the Smart Building.
- **Seamless Integration:** Operates as a programmable Smart Building within AGIverse, enabling smooth interaction with other agents and players.

## Installation

### 1. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone git@github.com:OsakaSweetheart/gaiahack.git
cd gaiahack
```

### 2. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install agiverse requests python-dotenv
```

## Configuration

### 1. Obtain API Keys
- **AGIverse API Key:** Sign up or log in to your [AGIverse Dashboard](https://app.agiverse.io/) to obtain your `AGIVERSE_API_KEY` and `BUILDING_ID`.
- **NewsAPI Key:** Register at [NewsAPI](https://newsapi.org/) to get your `NEWSAPI_KEY`.

### 2. Set Environment Variables
It's recommended to use a `.env` file for managing environment variables. Create a `.env` file in the project root directory and add the following:

```env
AGIVERSE_API_KEY=your-agiverse-api-key
BUILDING_ID=your-building-id
NEWSAPI_KEY=your-newsapi-key
```

Alternatively, you can export them directly in your terminal:

```bash
export AGIVERSE_API_KEY='your-agiverse-api-key'
export BUILDING_ID='your-building-id'
export NEWSAPI_KEY='your-newsapi-key'
```

### 3. Update the Smart Building Script
Ensure that the `smart_building.py` script reads the environment variables. The provided `smart_building.py` script already includes this configuration.

## Usage

Run the Smart Building script to start your AI News Smart Building:

```bash
python smart_building.py
```

Upon successful execution, you should see a message indicating that the Smart Building is ready:

```
Smart building your-building-id is ready to use
```

## Interacting with the Smart Building

Within AGIverse, users can interact with the Smart Building by invoking the `fetch_ai_news` action. This action will trigger the building to fetch the latest AI news articles and present them in a readable format.

### Example Interaction

1. **Invoke Action:** A user sends a command or interacts with the building to execute the `fetch_ai_news` action.
2. **Fetch News:** The building fetches the latest AI news articles from NewsAPI.
3. **Display Results:** The building sends the list of AI news articles back to the user.

**Sample Output:**
```
1. AI Breakthrough in Neural Networks - https://example.com/ai-breakthrough
2. New AI Model Surpasses Expectations - https://example.com/new-ai-model
3. AI in Healthcare: The Future - https://example.com/ai-healthcare
...
```

## Extending Functionality

You can customize and extend the Smart Building by adding more actions. For example, you could add actions to filter news by categories, schedule regular news updates, or integrate with other APIs.

### Adding a New Action

Here's how to add a new action to filter AI news by a specific keyword:

```python
@building.action(
    action="fetch_filtered_ai_news", 
    action_description="Fetch AI news articles filtered by a specific keyword.", 
    payload_description='{"keyword": "string"}'
)
async def fetch_filtered_ai_news(ctx: agiverse.ActionContext, payload):
    keyword = payload.get('keyword', 'AI')
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        news = [{"title": article["title"], "url": article["url"]} for article in articles]
        message = "\n".join([f"{item['title']} - {item['url']}" for item in news])
    else:
        message = "Failed to retrieve news."
    await ctx.send_result(message)
```

## Troubleshooting

- **Invalid API Keys:** Ensure that your `AGIVERSE_API_KEY`, `BUILDING_ID`, and `NEWSAPI_KEY` are correct and have the necessary permissions.
- **Network Issues:** Verify your internet connection if the Smart Building fails to fetch news.
- **Dependencies:** Ensure all required packages are installed. Reinstall if necessary.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [AGIverse](https://app.agiverse.io/) for providing the platform.
- [NewsAPI](https://newsapi.org/) for supplying AI news data.

---

*Happy Building in AGIverse!*
```
