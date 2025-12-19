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

db.add(
    Category(name="undefined")
)

for category in categories:
    # print(f'Adding {category}')
    db.add(
        Category(name="undefined")
    )
    db.add(
        Category(name=category)
    )


for index, row in df.iterrows():
    db.add(
        Entreprise(
            name=row['name'],
            category_id=db.query(Category.id).filter(Category.name == row['category']).first()[0],
            address=row['address'],
            phone=row['tel'],
            description=row['description']

        )
    )

db.commit()
db.close()


