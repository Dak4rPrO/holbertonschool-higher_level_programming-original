#!/usr/bin/python3
""" python file that contains the class definition of a
    State and an instance Base = declarative_base() """

import MySQLdb
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

if __name__ == "__main__":


    class State(Base):
        """Instatiation of class"""

        __tablename__ = 'states'
        
        id = Column(Integer, primary_key=True, unique=True,
                   autoincrement=True, nullable=False)

        name = Column(String(128), nullable=False)
        
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        cur = db.cursor()

        cur.execute("""SELECT * FROM states 
                    ORDER BY states.id ASC""")

        objets = cur.fetchall()
        
        Session = sessionmaker(bind=create_engine)
        session = Session()
        
        result = session.query(State).all()
        
        for obj in result:
            print(obj)

        cur.close()
        db.close()
