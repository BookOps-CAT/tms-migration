from sqlalchemy import Table
from sqlalchemy import MetaData

from db_session import get_tms_engine

metadata_obj = MetaData()


def get_objects_tbl(engine, tbl: str) -> Table:
    tbl = Table(tbl, metadata_obj, autoload_with=engine)
    return tbl


def get_tbl_columns(tbl: Table) -> list[str]:
    return tbl.columns.keys()


def get_tbl_constraints(tbl: Table):
    return tbl.constraints


if __name__ == "__main__":
    engine = get_tms_engine()
    tbl = get_objects_tbl(engine, "Objects")
    tbl_cols = get_tbl_columns(tbl)
    for t in tbl_cols:
        print(t)

    tbl_cons = get_tbl_constraints(tbl)
    print(tbl_cons, type(tbl_cons))
