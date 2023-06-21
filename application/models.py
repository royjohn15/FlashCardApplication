from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Deck(Base):
    __tablename__ = 'decks'

    deck_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    total_score = Column(Integer)
    last_reviewed = Column(String)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    user = relationship("User", backref="decks")


class Card(Base):
    __tablename__ = 'cards'

    card_id = Column(Integer, primary_key=True, autoincrement=True)
    front = Column(Text, nullable=False)
    back = Column(Text, nullable=False)
    score = Column(Integer)
    deck_id = Column(Integer, ForeignKey('decks.deck_id'))

    deck = relationship("Deck", backref="cards")
