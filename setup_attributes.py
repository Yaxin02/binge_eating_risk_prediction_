import os
from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()
client.set_endpoint('https://nyc.cloud.appwrite.io/v1')
client.set_project('69d8f483003b02a74713')
client.set_key('standard_43cb9ed0354adc2682adf564ba9ae9c46d7b3fecdd701429568cddcce9a7ffd33a581ce09807ab7b5eda90e53fa6ae0b39181aed2ab58a4811b8cf7c0c617c7d07d73995d77604eb4a5107a1bd69c4ce912f6ab715056c7ed9b6f1e85131b9b75cbdfcfec0f4755f0ea1bfe343703eafa2a4138d0c1bb4e0acad058a30509aff')

databases = Databases(client)

db_id = 'binge_db'
col_id = 'patients'

try:
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
        
    print("Setup Complete")
except Exception as e:
    print(e)
