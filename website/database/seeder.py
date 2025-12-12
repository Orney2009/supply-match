import os
from dotenv import load_dotenv
from my_sqlalchemy import *
from objects import *
import pandas as pd

load_dotenv()


engine = get_engine(os.getenv('DBMS'), os.getenv('DB_USER'), os.getenv('DB_PASSWORD'), os.getenv('DB_HOST'), os.getenv('DB_PORT'), os.getenv('DB_NAME'))
Base.metadata.create_all(bind=engine)
current_session = get_session(engine)

db = current_session()

df = pd.read_csv('artificial_intelligence/data/processed/processed_data.csv')

categories = df['category'].unique()

for category in categories:
    # print(f'Adding {category}')
    db.add(
        Category(name=category)
    )

db.commit()
db.close()

# print(engine.url)


