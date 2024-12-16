from database.db_session import Base
from sqlalchemy import Column, Integer, BigInteger, DateTime, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)

    chat_id = Column(BigInteger, unique=True)
    username = Column(String)
    referred_by = Column(String)
    created_at = Column(DateTime)

    def __str__(self):
        return f"<User chat_id: {self.chat_id}, @{self.username}, referred_by: {self.referred_by}>"

    def __repr__(self):
        return self.__str__()
