from modelos import Base
from datos.conexion import motor_db

def main():
    Base.metadata.create_all(bind=motor_db)
    print("Creación de tablas finalizada (si no existían).")

if __name__ == "__main__":
    main()
