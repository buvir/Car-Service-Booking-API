# create_database.py
import psycopg2
from psycopg2 import sql
import sys

def create_database():
    try:
        # Connect to PostgreSQL default database
        print("Connecting to PostgreSQL...")
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='sample12',
            host='localhost',
            port='5432'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Check if database already exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='car_service_db'")
        exists = cursor.fetchone()
        
        if exists:
            print("✅ Database 'car_service_db' already exists")
        else:
            # Create database
            cursor.execute(sql.SQL("CREATE DATABASE car_service_db"))
            print("✅ Database 'car_service_db' created successfully!")
        
        # List all databases
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        databases = cursor.fetchall()
        print("\n📋 Available databases:")
        for db in databases:
            print(f"  - {db[0]}")
        
        cursor.close()
        conn.close()
        
    except psycopg2.OperationalError as e:
        print(f"❌ Connection failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Is PostgreSQL running?")
        print("2. Is password correct?")
        print("3. Try default password if you didn't set one")
        print("   Common defaults: 'postgres', 'password', or empty ''")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    create_database()