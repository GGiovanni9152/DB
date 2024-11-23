#Mb Delete
from repositories.library import get_user_games
from pandas import DataFrame

class LibraryService:
    def user_games(self, user_id: int) -> DataFrame:
        items = get_user_games(user_id)
        return items