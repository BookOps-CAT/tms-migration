from sqlalchemy import select, func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from tms.tms_db_conn import get_tms_engine, get_manipulation_engine
from tms.tms_models import Objects, ObjTitles, Departments, Roles, RolesTypes
from tms.tms_values import TitleTypes


def temp(engine):
    with Session(engine) as session:
        rows = session.execute(
            select(Roles.Role, Roles.RoleID).where(Roles.RoleTypeID == 1)
        ).all()
        for r in rows:
            print(f"{r.Role} = {r.RoleID}")


def object_by_dept_count(engine, dept_id: int):
    with Session(engine) as session:
        row_count = session.scalar(
            select(func.count())
            .select_from(Objects)
            .filter(Objects.DepartmentID == dept_id)
        )
        dept = session.execute(
            select(Departments).where(Departments.DepartmentID == dept_id)
        ).one()
        if row_count > 0:
            print(f"'{dept[0].Department}' ({dept_id}) has {row_count} objects.")


def title_types_in_ObjTitles_tbl(engine):
    with Session(engine) as session:
        for title, titletype_id in TitleTypes.__members__.items():
            row_count = session.scalar(
                select(func.count())
                .select_from(ObjTitles)
                .filter(ObjTitles.TitleTypeID == titletype_id)
            )

            # if row_count > 0:
            print(f"{title} has {row_count} entries.")


if __name__ == "__main__":
    engine = get_tms_engine()
    title_types_in_ObjectTitles_tbl(engine)
