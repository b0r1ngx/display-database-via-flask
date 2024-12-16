from database.db_session import Session
from database.tables.users import User
from database.tables.deals_history import DealHistory


def get_all_users() -> list[User]:
    with Session() as s:
        users = s.query(User).all()

    return users


def get_all_deals() -> list[DealHistory]:
    with Session() as s:
        deals = s.query(DealHistory).all()

    return deals
