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
		interests = interests)
		# rating = rating)
	session.add(interest_object)
	session.commit()

# add_article("waseem", "tennis")
# add_article("Mousa", "GYM")

def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge
print(query_all_articles())
	

def query_article_by_topic(name):
	knowledge = session.query(Knowledge).filter_by(student_name=name).all()
	return knowledge
# print(query_article_by_topic("waseem"))	

def delete_article_by_topic(name):
	knowledge = session.query(Knowledge).filter_by(student_name=name).delete()
	session.commit()
# delete_article_by_topic("Mousa")
# print(query_all_articles())
	

# def delete_all_articles():
# 	knowledge = session.query(Knowledge).delete()
# 	session.commit()
# print(delete_all_articles())
	
def edit_article_rating(name1,interests):
	interest_object = session.query(Knowledge).filter_by(student_name=name1).first()
	interest_object.interests = interests
	session.commit()

edit_article_rating("waseem","soccer")
edit_article_rating("Mousa","violin")
print(query_all_articles())
	
