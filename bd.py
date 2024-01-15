# conexion_bd.py
import mysql.connector

class ConexionBD:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="LuMITY_BV1",
        )
        self.cursor = self.conexion.cursor()

        self.inicializar_base_datos()

    def inicializar_base_datos(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS juego_piolin")
        self.cursor.execute("USE juego_piolin")

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS juego_principal (
                posicion varchar(30) not null,
                fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)

    def ejecutar_query(self, query):
        self.cursor.execute(query)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
