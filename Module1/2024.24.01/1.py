from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv('DATABASE')
secret_key = os.getenv('SECRET_KEY')


print(f'DATABASE: {database}')
print(f'SECRET_KEY: {secret_key}')