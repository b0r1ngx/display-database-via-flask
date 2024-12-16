from database.db_session import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger


class DealHistory(Base):
    __tablename__ = 'deals_history'

    id = Column(Integer, primary_key=True, autoincrement=True)

    deal_id = Column(Integer, unique=True)
    chat_id = Column(BigInteger)

    type = Column(String)
    currency = Column(String)
    value = Column(Float)
    wallet = Column(String)
    payed_by = Column(String)
    to_pay = Column(Integer)
    referred_by = Column(String)
    bonuses_used = Column(Integer)

    # buy parameter
    transaction_link = Column(String)

    # sell parameters
    user_requisites = Column(String)
    transaction_hash = Column(String)
    document_id = Column(String)

    created_at = Column(DateTime)

    def __str__(self):
        return f"<Deal - deal_id: {self.deal_id}, chat_id: {self.chat_id}, to_pay: {self.to_pay}>"

    def __repr__(self):
        return self.__str__()
