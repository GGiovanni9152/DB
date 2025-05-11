import redis
import json
import pandas as pd
import pickle
import jwt_utils

redis_client = redis.Redis(host = 'localhost', port = 6379, db = 0, decode_responses = True)

def save_games_table(user_id: int, df: pd.DataFrame):
    redis_client.set(f"session:{user_id}:games_table", df.to_json(), ex = 3600)

def load_games_table(user_id: int) -> pd.DataFrame | None:
    data = redis_client.get(f"session:{user_id}:games_table")

    if data:
        try:
            df = pd.read_json(data)
            return df
        except Exception as e:
            print(f"Reddis error: {e}")
            return None
    return None

def clear_games_table(user_id: int):
    redis_client.delete(f"session:{user_id}:games_table")

def save_user_library(user_id: int, df: pd.DataFrame):
    redis_client.set(f"user_library:{user_id}", df.to_json(), ex = 3600)

def load_user_library(user_id: int) -> pd.DataFrame | None:
    data = redis_client.get(f"user_library:{user_id}")

    if data is not None:
        df = pd.read_json(data)
        return df
    return None

def clear_user_library(user_id: int):
    redis_client.delete(f"user_library:{user_id}")

def save_current_user(user: pd.DataFrame):
    redis_client.set("current_user", user.to_json(), ex = 3600)

def load_current_user():
    data = redis_client.get("current_user")

    if data is not None:
        df = pd.read_json(data)
        return df
    return None

def clear_current_user():
    redis_client.delete("current_user") 

def clear_users():
    redis_client.delete("users:list")

def clear_games():
    redis_client.delete("games:list")

def clear_admins():
    redis_client.delete('admins')

def save_token(user_id, token):
    redis_client.setex(f"jwt:{user_id}", jwt_utils.JWT_TTL_SECONDS, token)

def load_token(user_id):
    return redis_client.get(f"jwt:{user_id}")

def clear_token(user_id):
    redis_client.delete(f"jwt:{user_id}")

def publish_event(channel, message):
    redis_client.publish(channel, message)

def subscribe_to_channel(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub