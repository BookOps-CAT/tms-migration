from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Objects(Base):
    __tablename__ = "Objects"
    ObjectID: Mapped[int] = mapped_column(primary_key=True)
    ObjectNumber: Mapped[str] = mapped_column(String(30))
    ObjectCount: Mapped[int]
    DepartmentID: Mapped[int] = mapped_column(ForeignKey("Departments.DepartmentID"))

    def __repr__(self) -> str:
        return f"Object(ObjectID={self.ObjectID!r}, ObjectNumber={self.ObjectNumber!r}, ObjectCount={self.ObjectCount!r}, DepartmentID={self.DepartmentID!r})"


class Departments(Base):
    __tablename__ = "Departments"
    DepartmentID: Mapped[int] = mapped_column(primary_key=True)
    Department: Mapped[str] = mapped_column(String(30))
    Mnemonic: Mapped[str] = mapped_column(String(30))
    Objects: Mapped[list["Objects"]] = relationship()

    def __repr__(self) -> str:
        return f"Department(DepartmentID={self.DepartmentID!r}, Department={self.Department!r}, Mnemonic={self.Mnemonic!r}, Objects={self.Objects!r})"


class Roles(Base):
    __tablename__ = "Roles"
    RoleID: Mapped[int] = mapped_column(primary_key=True)
    RoleTypeID: Mapped[int] = mapped_column(ForeignKey("RoleTypes.RoleTypeID"))
    Role: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Role(RoleID={self.RoleID!r}, RoleTypeID={self.RoleTypeID!r}, Role={self.Role!r})"


class RolesTypes(Base):
    __tablename__ = "RolesTypes"
    RoleTypeID: Mapped[int] = mapped_column(primary_key=True)
    RoleType: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"RolesType(RoleTypeID={self.RoleTypeID!r}, RoleType={self.RoleType!r})"
