from os import getenv
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

# Check if the token is loaded properly
print(f"Loaded token: {TOKEN}")  # This will print the token (don't keep this in production!)

dp = Dispatcher(storage=MemoryStorage())
