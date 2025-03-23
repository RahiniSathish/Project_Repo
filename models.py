from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    conversations = relationship("Conversation", back_populates="user")

class Conversation(Base):
    __tablename__ = 'conversations'

    id = Column(Integer, primary_key=True)
    conversation_id = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    user = relationship("User", back_populates="conversations")
