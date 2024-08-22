from sqlalchemy import create_engine


def get_engine(fh: str):
    engine = create_engine(f"sqlite:///{fh}")
    return engine
