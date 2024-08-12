import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',  
        database='techzone',  
        user='root',  
        password=''  
    )

    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

        cursor = connection.cursor()

        insert_query = """
        INSERT INTO Devices (device_name, brand_id, type_id, price, release_date, warranty_period)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, ('MacBook Pro', 1, 2, 2399.99, '2023-06-15', 12))
        connection.commit()
        print("Nuevo dispositivo insertado")

        select_query = "SELECT * FROM Devices"
        cursor.execute(select_query)
        devices = cursor.fetchall()
        print("Dispositivos actuales:")
        for device in devices:
            print(device)

        update_query = "UPDATE Devices SET price = %s WHERE device_id = %s"
        cursor.execute(update_query, (2199.99, 1))
        connection.commit()
        print("Precio del dispositivo actualizado")


        cursor.execute(select_query)
        devices = cursor.fetchall()
        print("Dispositivos después de la actualización:")
        for device in devices:
            print(device)

        delete_query = "DELETE FROM Devices WHERE device_id = %s"
        cursor.execute(delete_query, (1,))
        connection.commit()
        print("Dispositivo eliminado")

        cursor.execute(select_query)
        devices = cursor.fetchall()
        print("Dispositivos después de la eliminación:")
        for device in devices:
            print(device)

except Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a la base de datos cerrada")
