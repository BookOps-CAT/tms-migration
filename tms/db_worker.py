from sqlalchemy import select, func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from tms.db_session import get_tms_engine, get_manipulation_engine
from tms.tms_models import Objects, Departments, Roles, RolesTypes


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


if __name__ == "__main__":
    engine = get_tms_engine()
    temp(engine)
