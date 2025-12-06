# create_db.py
import psycopg2
from psycopg2 import sql

def create_database():
    try:
        print("Step 1: Connecting to PostgreSQL...")
        
        # First connect to the default 'postgres' database
        conn = psycopg2.connect(
            dbname='postgres',  # Connect to default database
            user='postgres',
            password='sample12',  # Your password
            host='localhost',
            port='5432'
        )
        conn.autocommit = True  # Important for creating databases
        cursor = conn.cursor()
        
        print("Step 2: Checking if database already exists...")
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='car_service_db'")
        exists = cursor.fetchone()
        
        if exists:
            print("✅ Database 'car_service_db' already exists!")
        else:
            print("Step 3: Creating database 'car_service_db'...")
            cursor.execute(sql.SQL("CREATE DATABASE car_service_db"))
            print("✅ Database 'car_service_db' created successfully!")
        
        # List all databases
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false ORDER BY datname;")
        databases = cursor.fetchall()
        
        print("\n📋 All databases on your system:")
        for db in databases:
            print(f"  - {db[0]}")
        
        cursor.close()
        conn.close()
        
    except psycopg2.OperationalError as e:
        print(f"\n❌ CONNECTION ERROR: {e}")
        print("\n🔧 Possible solutions:")
        print("1. Is PostgreSQL running? Check services")
        print("2. Is the password 'sample12' correct?")
        print("3. Try connecting with pgAdmin GUI")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = create_database()
    if success:
        print("\n🎉 Database setup complete! You can now run alembic.")