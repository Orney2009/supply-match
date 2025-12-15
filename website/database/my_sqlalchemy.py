from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database



def get_engine(rdms, user, password, host, port, db):
    url = f"{rdms}://{user}:{password}@{host}/{db}"
    try:
        if not database_exists(url):
            # print('Creating database')
            create_database(url)

        engine = create_engine(url, pool_size=50, echo=False)
        return engine

    except Exception as e:
        print(f'Error when getting engine: {e}')



def get_session(engine):
    session = sessionmaker(bind=engine)
    return session