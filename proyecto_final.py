import mysql.connector

class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
    
    def __str__(self):
        return f"Usuario (id={self.id}, nombre='{self.nombre}', email='{self.email}')"

class Materia:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
    def __str__(self):
        return f"Materia(id={self.id}, nombre='{self.nombre}')"
    
class BaseDatos:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()
        
    def crear_usuario(self, usuario):
        query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        self.cursor.execute(query,  (usuario.nombre, usuario.email))
        self.conexion.commit()
        
    def leer_usuarios(self):
        query = "SELECT * FROM usuarios"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        usuarios = []
        for row in results:
            usuarios.append(Usuario(*row))
        return usuarios
    
    def actualizar_usuario(self, usuario):
        query = "UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s"
        self.cursor.execute(query, (usuario.nombre, usuario.email, usuario.id))
        self.conexion.commit()
        
    def eliminar_usuario(self, id):
        query = "DELETE FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (id,))
        self.conexion.commit()
        
    def crear_materia(self, materia):
        query = "INSERT INTO materias (nombre) VALUES (%s)"
        self.cursor.execute(query, (materia.nombre,))
        self.conexion.commit()
        
    def leer_materias(self):
        query = "SELECT * FROM materias"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        materias = []
        for row in results:
            materias.append(Materia(*row))
        return materias
    
    def unir_usuario_a_materia(self, usuario_id, materia_id):
        query = "INSERT INTO usuarios_materias (usuario_id, materia_id) VALUES (%s, %s)"
        self.cursor.execute(query, (usuario_id, materia_id))
        self.conexion.commit()
        
    def leer_usuarios_de_materia(self, materia_id):
        query = "SELECT u.* FROM usuarios u JOIN usuarios_materias um ON u.id = um.usuario_id WHERE um.materia_id = %s"
        self.cursor.execute(query, (materia_id,))
        results = self.cursor.fetchall()
        usuarios = []
        for row in results:
            usuarios.append(Usuario(*row))
        return usuarios
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
        
#Base de Datos
username = 'root'
password = ''
host = 'localhost'
database = 'control'

db = BaseDatos(host, username, password, database)

#Menu
def menu():
    while True:
        print("1. Crear Usuario")
        print("2. Leer Usuario")
        print("3. Actualizar Usuario")
        print("4. Eliminar Usuario")
        print("5. Crear Materia")
        print("6. Leer Materia")
        print("7. Unir Usuario a Materia")
        print("8. Leer Usuario de Materia")
        print("9. Salir")
        opcion = input("Selecciona una opción. ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del Usuario: ")
            email = input("Ingrese el email del Usuario: ")
            nuevo_usuario = Usuario(None, nombre, email)
            db.crear_usuario(nuevo_usuario)
        elif opcion == '2':
            usuarios = db.leer_usuarios()
            for usuario in usuarios:
                print(usuario)
        elif opcion == '3':
            id = int(input("Ingrese el ID del usuario a actualizar: "))
            nombre = input("Ingrese el nuevo nombre del usuario: ")
            email = input("Ingrese el nuevo email del usuario: ")
            usuario_actualizado = Usuario(id, nombre, email)
            db.actualizar_usuario(usuario_actualizado)
        elif opcion == '4':
            id = int(input("Ingrese el ID del usuario a eliminar: "))
            db.eliminar_usuario(id)
        elif opcion == '5':
            nombre = input("Ingrese el nombre de la Materia: ")
            nueva_materia = Materia(None, nombre)
            db.crear_materia(nueva_materia)
        elif opcion == '6':
            materias = db.leer_materias()
            for materia in materias:
                print(materia)
        elif opcion == '7':
            usuario_id = int(input("Ingrese el ID del ususario: "))
            materia_id = int(input("Ingrese el ID de la materia: "))
            db.unir_usuario_a_materia(usuario_id, materia_id)
        elif opcion == '8':
            materia_id = int(input("Ingrese el ID de la materia: "))
            usuarios = db.leer_usuarios_de_materia(materia_id)
            for usuario in usuarios:
                print(usuario)
        elif opcion == '9':
            db.cerrar_conexion()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
            
menu()