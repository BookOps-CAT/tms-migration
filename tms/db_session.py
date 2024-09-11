import json
import os

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from tms.tms_models import Roles


def get_manipulation_engine(fh: str):
    engine = create_engine(f"sqlite:///data/private/manipulated_tms_data.db")
    return engine


def get_creds() -> dict:
    with open(
        os.path.join(os.environ["USERPROFILE"], ".cred/.tms/tms-tomasz.json"), "r"
    ) as f:
        creds = json.load(f)
        return creds


def get_tms_engine():
    creds = get_creds()
    url = f"mssql+pyodbc://{creds['USER']}:{creds['PASSWORD']}@{creds['HOST']}:{creds['PORT']}/{creds['DB']}?driver=ODBC+Driver+13+for+SQL+Server"
    engine = create_engine(url)
    return engine


def get_session(engine):
    with Session(engine) as sess:
        return sess


def engine_connection_test(engine):
    """Throws an exception if the connection fails"""
    engine.connect()
    print("Connection successful")
