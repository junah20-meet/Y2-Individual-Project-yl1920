from model import Base, Message

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

def add_story(firstname, lastname, email, story):
	story_obj = Message(
		firstName = firstname,
		lastName = lastname,
		email = email,
		story = story)
	session.add(story_obj)
	session.commit()

def querry_all():
	Messages = session.query(Message).all()
	return Messages