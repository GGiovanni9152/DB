from redis_client import subscribe_to_channel
import json
import time
import threading

def handle_message(msg):
    if msg["type"] == "message":
        data = json.loads(msg["data"])
        if data["type"] == "new_game_added":
            print(f"[Message] Users: {data['user_id']} added games: {data['game_id']}")

def start_list():
    def listen():
        pubsub = subscribe_to_channel("game_updates")
        print("Success subscribe")

        for message in pubsub.listen():
            handle_message(message)
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
