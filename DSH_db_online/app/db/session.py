from typing import Generator

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:postgres@db_devices:5432/dsh_db_devices")
_session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)


def get_db() -> Generator:
    try:
        session: Session = _session()
        yield session
    finally:
        session.close()
