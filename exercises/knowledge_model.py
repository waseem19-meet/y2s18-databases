from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	__tablename__= 'knowledge'
	student_id = Column(Integer, primary_key=True)
	student_name = Column(String)
	interests = Column(String)
	def __repr__(self):
		return("student name: {}\n"
				"student's interests: {}\n").format(
				self.student_name,
				self.interests)
x = Knowledge(student_name="shir" , interests="playing on the three guitars she owns, but one is broken so she only use the other two")
print(x)

# y = Knowledge(student_name="waseem" , interests="playing tennis ")
# print(y)

# z = Knowledge(student_name="or" , interests="the royal Britain family")
# print(z)


