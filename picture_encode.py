import base64
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database= "postgres",
    user= "postgres",
    password= 123456
)


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
        return f"data:image/jpeg;base64,{encoded}"
    
query1 = """
        UPDATE game_detail
        SET picture_code = %(image)s
        WHERE game_id = 1
    """

query2 = """
        UPDATE game_detail
        SET picture_code = %(image)s
        WHERE game_id = 2
    """

query3 = """
        UPDATE game_detail
        SET picture_code = %(image)s
        WHERE game_id = 3
    """

try:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(query1, {"image": encode_image_to_base64('pictures/Dota.jpg')})
            cursor.execute(query2, {"image": encode_image_to_base64('pictures/Smyta.jpg')})
            cursor.execute(query3, {"image": encode_image_to_base64('pictures/Heartsofiron.jpg')})
finally:
    conn.close()
