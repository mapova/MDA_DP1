from db_connection import *
import random
import time

time.sleep(60)

# OBTENEMOS LOS IDs DE LOS USUARIOS PARA CREAR LAS RESERVAS
sql_id_usuarios = "SELECT id FROM users"
id_usuarios_consulta = None
while id_usuarios_consulta == None:
    id_usuarios_consulta = sql_request_select(sql_id_usuarios)
id_usuarios = []
for id in id_usuarios_consulta:
    id_usuarios.append(id[0])
# OBTENEMOS LOS IDs DE LOS HOTELES PARA CREAR LAS RESERVAS
sql_id_hoteles = "SELECT id FROM hotels"
id_hoteles_consulta = sql_request_select(sql_id_hoteles)
id_hoteles = []
for id in id_hoteles_consulta:
    id_hoteles.append(id[0])
reservas = []
for id in id_usuarios:
    id_hoteles = random.sample(id_hoteles, 5)
    for id_hotel in id_hoteles:
        reservas.append(f"({id}, {id_hotel})")
        
sql_query = "INSERT INTO bookings (user_id, hotel_id) VALUES "
sql_query += ",\n".join(reservas) + ";"
sql_request(sql_query)