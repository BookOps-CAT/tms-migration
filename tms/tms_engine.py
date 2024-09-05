from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def get_engine(fh: str):
    engine = create_engine(f"sqlite:///{fh}")
    return engine


def get_session(engine):
    with Session(engine) as sess:
        return sess
