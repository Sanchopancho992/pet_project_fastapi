from fastapi import APIRouter, Depends
from .models import StartGame, Game
from ..db.client import MongoDBClient

router = APIRouter(prefix="/game", tags=["Games"])


@router.post("/")
async def start_new_game(player_data: StartGame) -> Game:
    data = {"player1": player_data.player, "player2": player_data.player}
    client = MongoDBClient()
    insert_result = await client.insert(Game, data)
    game_data = await client.get(Game, insert_result.inserted_id)
    result = Game(**game_data)
    return result


def get_current_app():
    import importlib

    module = importlib.import_module("src.main")
    field = "app"
    return getattr(module, field)
