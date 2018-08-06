from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from knowledge_model import Knowledge

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(student_name, interests):
	interest_object = Knowledge(
		student_name = student_name,
		interests = interests )
	session.add(interest_object)
	session.commit()

add_article("waseem", "tennis")

# def query_all_articles():
	

# def query_article_by_topic():
	

# def delete_article_by_topic():
	

# def delete_all_articles():
	

# def edit_article_rating():
	
