from mem0 import MemoryClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("MEMO_API_KEY")

if api_key is None:
    raise ValueError("MEMO_API_KEY not found in environment variables.")

client = MemoryClient(api_key=api_key)


# messages = [
#     {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
#     {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
# ]
# client.add(messages, user_id="alex")
