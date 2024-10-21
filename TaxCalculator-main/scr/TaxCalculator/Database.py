import sys
import os
from psycopg import connect, OperationalError, DatabaseError
# Agregar la carpeta raíz del proyecto a la ruta de búsqueda
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from psycopg import connect
from SecretConfig import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME

def connect_db():
    """Establece conexión a la base de datos NeonTech."""
    try:
        conn = connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME
        )
        return conn
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables():
    """Crea las tablas necesarias para almacenar usuarios, ingresos, deducciones y el historial."""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS calculations (
            calculation_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            gross_income NUMERIC NOT NULL,
            deductions NUMERIC NOT NULL,
            tax_credits NUMERIC NOT NULL,
            tax_paid NUMERIC NOT NULL,
            calculation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
        )
        """
    )

    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
            conn.commit()
            print("Tables created successfully.")
        except DatabaseError as e:
            print(f"Error creating tables: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

def insert_user(username, email):
    """Inserta un nuevo usuario en la base de datos y devuelve el ID del usuario."""
    sql_command = """
    INSERT INTO users (username, email) VALUES (%s, %s) RETURNING user_id;
    """
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (username, email))
                user_id = cur.fetchone()[0]
            conn.commit()
            return user_id
        except DatabaseError as e:
            print(f"Error inserting user: {e}")
            return None
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")
        return None

def insert_calculation(user_id, gross_income, deductions, tax_credits, tax_paid):
    """Inserta un cálculo de impuestos en la base de datos."""
    sql_command = """
    INSERT INTO calculations (user_id, gross_income, deductions, tax_credits, tax_paid)
    VALUES (%s, %s, %s, %s, %s);
    """
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (user_id, gross_income, deductions, tax_credits, tax_paid))
            conn.commit()
            print("Calculation inserted successfully.")
        except DatabaseError as e:
            print(f"Error inserting calculation: {e}")
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")

def get_user_calculations(user_id):
    """Obtiene el historial de cálculos de un usuario por su ID."""
    sql_command = """
    SELECT calculation_id, gross_income, deductions, tax_credits, tax_paid, calculation_date 
    FROM calculations 
    WHERE user_id = %s;
    """
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (user_id,))
                calculations = cur.fetchall()
            return calculations
        except DatabaseError as e:
            print(f"Error retrieving user calculations: {e}")
            return None
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")
        return None
    
def get_user_by_id(user_id):
    """Obtiene los detalles de un usuario por su ID."""
    sql_command = """
    SELECT * FROM users WHERE user_id = %s;
    """
    conn = connect_db()
    if conn is not None:
        cur = conn.cursor()
        cur.execute(sql_command, (user_id,))
        user = cur.fetchone()  # Retorna solo un registro
        cur.close()
        conn.close()
        return user
    else:
        print("Error retrieving user by ID.")
        return None

def delete_user(user_id):
    """Elimina un usuario de la base de datos por su ID."""
    sql_command = """
    DELETE FROM users WHERE user_id = %s;
    """
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (user_id,))
            conn.commit()  # Confirmar la eliminación
            print(f"User with ID {user_id} deleted successfully.")
        except DatabaseError as e:
            print(f"Error deleting user: {e}")
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")

def update_user_email(user_id, new_email):
    """Actualiza el correo electrónico de un usuario en la base de datos."""
    sql_command = """
    UPDATE users SET email = %s WHERE user_id = %s;
    """
    conn = connect_db()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (new_email, user_id))
            conn.commit()  # Confirmar los cambios
            print(f"Email updated to {new_email} for user ID {user_id}.")
        except DatabaseError as e:
            print(f"Error updating email: {e}")
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")

def get_user_by_email(email):
    """Obtiene un usuario de la base de datos utilizando su correo electrónico."""
    sql_command = """
    SELECT id, name, email FROM users WHERE email = %s;
    """
    
    conn = connect_db()
    user = None  # Inicializa la variable para almacenar el usuario
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(sql_command, (email,))
                user = cur.fetchone()  # Obtiene el primer resultado
                if user:
                    print(f"User found: ID={user[0]}, Name={user[1]}, Email={user[2]}")
                else:
                    print("No user found with the provided email.")
        except DatabaseError as e:
            print(f"Error retrieving user: {e}")
        finally:
            conn.close()
    else:
        print("Error: Unable to connect to the database.")
    
    return user  # Devuelve el usuario encontrado o None