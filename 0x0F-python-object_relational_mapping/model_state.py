#!/usr/bin/python3

import SQLAlchemy
import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
Base.metadata.create_all(engine)

class State(Base):

