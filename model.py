from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
	__tablename__= 'message'
	id = Column (Integer, primary_key= True)
	firstName = Column(String)
	lastName = Column(String)
	email = Column(String)
	story = Column(String)





