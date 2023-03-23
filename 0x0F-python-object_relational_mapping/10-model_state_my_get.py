#!/usr/bin/python3
""" Get a state """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """prints the State object with the
    name passed as argument from the database hbtn_0e_6_usa
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
    @localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == f'{sys.argv[4]}')
    if len(list(query)) == 0:
        print("Not found")
    else:
        for state in query:
            print(f"{state.id}")
