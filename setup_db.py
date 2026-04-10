import os
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.permission import Permission
from appwrite.role import Role

client = Client()
client.set_endpoint('https://nyc.cloud.appwrite.io/v1')
client.set_project('69d8f483003b02a74713')
client.set_key('standard_43cb9ed0354adc2682adf564ba9ae9c46d7b3fecdd701429568cddcce9a7ffd33a581ce09807ab7b5eda90e53fa6ae0b39181aed2ab58a4811b8cf7c0c617c7d07d73995d77604eb4a5107a1bd69c4ce912f6ab715056c7ed9b6f1e85131b9b75cbdfcfec0f4755f0ea1bfe343703eafa2a4138d0c1bb4e0acad058a30509aff')

databases = Databases(client)

try:
    # Create DB
    db = databases.create("binge_db", "Binge Prediction Database")
    db_id = db['$id'] if isinstance(db, dict) else db.id
    print(f"Created Database: {db_id}")

    # Create Collection with open permissions
    perms = [
        Permission.read(Role.any()),
        Permission.create(Role.any()),
        Permission.update(Role.any()),
        Permission.delete(Role.any()),
    ]
    
    collection = databases.create_collection(
        database_id=db_id,
        collection_id="patients",
        name="Patients Records",
        permissions=perms
    )
    col_id = collection['$id'] if isinstance(collection, dict) else collection.id
    print(f"Created Collection: {col_id}")

    # Create Attributes
    print("Creating attributes...")
    
    # Strings
    databases.create_string_attribute(db_id, col_id, "created_at", 100, True)
    
    # Integers
    int_attrs = ["gender", "education", "alcohol", "t2d", "sleep_apnea_syndrome", "gastroesophageal_reflux_disease", "prediction"]
    for attr in int_attrs:
        databases.create_integer_attribute(db_id, col_id, attr, True)

    # Floats
    float_attrs = ["age", "bmi", "weight_kg", "waist_cm", "ede_q_per_operation", "probability"]
    for attr in float_attrs:
        databases.create_float_attribute(db_id, col_id, attr, True)
        
    print(f"\nSETUP COMPLETE!")
    print(f"DB_ID={db_id}")
    print(f"COL_ID={col_id}")
    
except Exception as e:
    print(f"Error: {e}")
