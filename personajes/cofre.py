import mysql.connector, objeto, random, pygame,os
conexion=mysql.connector.connect(
    host="3306",
    user="root",
    password="LuMITY_BV1",
)

cursor=conexion.cursor()

class cofre(objeto):
    def __init__(self,id_cofre):
        self.imgage=imgane=pygame.image.load(os.path.join(os.path.dirname(__file__),"Image","cofre.jpg"))
    def interactuar(id_cofre):
        abierto=cursor.execute("select abierto from cofre where id_cofre=?",id_cofre)
        if not abierto:
            num_al=random.randint(0,300)
            objeo=cursor.execute("select * from objetos where id_obj=?",num_al)
            abierto=True
            cursor.execute("UPDATE cofre set abierto=? where id_cofre=?",{abierto, id_cofre})
            return objeo
