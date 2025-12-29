from pathlib import Path
import requests
import os
# Permet de charger les secret depuis un fichier .env
from dotenv import load_dotenv

current_dir = Path(__file__).parent
root_dir = current_dir.parent
env_path = root_dir / '.env'

# Charge les secrets depuis le fichier .env
load_dotenv(dotenv_path=env_path)

class wargamingclient():
    def __init__(self):
        self.api_key = os.getenv("WARGAMING_APP_ID")

        if not self.api_key:
            raise ValueError("ERREUR: la clé API est manquante dans le fichier .env")
        
        self.region = "eu"
        self.base_url = f"https://api.worldoftanks.{self.region}/wot/"

    def get_player_id(self, nickname: str) -> int:
        """Pour chercher un jouer par son pseudo et retourne son account_id."""
        endpoint= f"{self.base_url}/account/list/"
        params = {
            "application_id": self.api_key,
            "search": nickname,
            "limit": 1  # On ne conserve que le premier résultat exacte
        }

        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()

            if data["status"] != "ok" or not data["data"]

        
API_KEY = os.getenv("WARGAMING_APP_ID")
REGION = "eu"
BASE_URL = f"https://api.worldoftanks.{REGION}/wot/"

def fetch_player_id(nickname: str):
    """Pour chercher un jouer par son pseudo et retourne son account_id."""
    if not API_KEY:
        raise ValueError("ERREUR: la clé API est vide ou introuvable dans le .env.")
    
    endpoint = f"{BASE_URL}/account/list/"
    params = {
        "application_id" = API_KEY,
        "search" : nickname,
        "limit" : 1 # On ne conserve que le premier résultat exacte
    }

    try:
        response = requests.get(endpoint, params=params)
        re