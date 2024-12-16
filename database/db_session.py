import logging

from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as S, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()
Session: S = sessionmaker()

# todo: set link to your database
path = 'database/cryptobot.db'
sqlite_file_path = 'sqlite:///' + path + '?check_same_thread=False'


def init_database_session() -> None:
    engine = create_engine(url=sqlite_file_path, echo=False)

    logging.info('Подключение к базе данных')
    Session.configure(bind=engine)

    if not database_exists(engine.url):
        logging.info('Создание базы данных')
        create_database(engine.url)

    logging.info('Инициализация таблиц')
    Base.metadata.create_all(engine)

    logging.info('Объект Session, для доступа к базе данных, доступен')
