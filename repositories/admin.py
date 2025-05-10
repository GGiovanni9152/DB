import psycopg2
import psycopg2.extras
from settings import DB_CONFIG
from redis_client import redis_client
import json

def get_all_admins(): #-> list[dict]:
    cache_key = "admins"
    #cached_admins = redis_client.get(cache_key)
    if redis_client.exists(cache_key):
        return [int(admin_id) for admin_id in redis_client.smembers(cache_key)]
    #if cached_admins:
    #    return json.loads(cached_admins)

    query = "SELECT user_id FROM admins;"
    
    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:#(cursor_factory = psycopg2.extras.RealDictCursor) as cur:
            cur.execute(query)
            admins = cur.fetchall()
            adm = []
            for elem in admins:
                adm.append(elem[0])
            redis_client.sadd(cache_key, *adm)
            redis_client.expire(cache_key, 3600)
            #redis_client.set(cache_key, json.dumps(adm), ex=3600)
            return adm

def get_admins(admin_id) -> bool:
    if redis_client.exists("admins"):
        return redis_client.sismember("admins", str(admin_id))
    
    admins = get_all_admins()

    return admin_id in admins
    
    #query = """SELECT user_id FROM admins WHERE user_id = %(admin_id)s"""
    
    #with psycopg2.connect(**DB_CONFIG) as conn:
    #    with conn.cursor() as cur:
    #        cur.execute(query, {"admin_id" : admin_id})
    #       return (cur.fetchone() != None)