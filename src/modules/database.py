import firebirdsql
import os
from dotenv import load_dotenv

load_dotenv()
conn = firebirdsql.connect(
    host=os.getenv("HOST"),
    database=os.getenv("DATABASE"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
)

cursor = conn.cursor()
