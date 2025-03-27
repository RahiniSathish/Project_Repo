
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
API_KEY = os.getenv("API_KEY")
API_VERSION = os.getenv("API_VERSION")
DEPLOYMENT_ID = os.getenv("DEPLOYMENT_ID")
