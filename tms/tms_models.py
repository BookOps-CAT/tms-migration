from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Objects(Base):
    __tablename__ = "Objects"
    ObjectID: Mapped[int] = mapped_column(primary_key=True)
    ObjectNumber: Mapped[str] = mapped_column(String(30))
    ObjectCount: Mapped[int]
    DepartmentID: Mapped[int] = mapped_column(ForeignKey("Departments.DepartmentID"))

    def __repr__(self) -> str:
        return (
            f"Object(ObjectID={self.ObjectID!r}, ObjectNumber={self.ObjectNumber!r}, "
            f"ObjectCount={self.ObjectCount!r}, DepartmentID={self.DepartmentID!r})"
        )


class ObjTitles(Base):
    __tablename__ = "ObjTitles"
    TitleID: Mapped[int] = mapped_column(primary_key=True)
    ObjectID: Mapped[int] = mapped_column(ForeignKey("Objects.ObjectID"))
    TitleTypeID: Mapped[int] = mapped_column(ForeignKey("TitleTypes.TitleTypeID"))
    Title: Mapped[str] = mapped_column(String(850), nullable=False)
    DisplayOrder: Mapped[int] = mapped_column(nullable=False)
    Displayed: Mapped[int] = mapped_column(nullable=False)
    LanguageID: Mapped[int] = mapped_column(ForeignKey("Languages.LanguageID"))

    def __repr__(self) -> str:
        return (
            f"ObjectTitle(TitleID={self.TitleID!r}, ObjectID={self.ObjectID!r}, "
            f"TitleTypeID={self.TitleTypeID!r}, Title={self.Title!r}, "
            f"DisplayOrder={self.DisplayOrder!r}, Displayed={self.Displayed!r}, "
            f"LanguageID={self.LanguageID!r})"
        )


class Departments(Base):
    __tablename__ = "Departments"
    DepartmentID: Mapped[int] = mapped_column(primary_key=True)
    Department: Mapped[str] = mapped_column(String(30))
    Mnemonic: Mapped[str] = mapped_column(String(30))
    Objects: Mapped[list["Objects"]] = relationship()

    def __repr__(self) -> str:
        return (
            f"Department(DepartmentID={self.DepartmentID!r}, "
            f"Department={self.Department!r}, Mnemonic={self.Mnemonic!r}, "
            f"Objects={self.Objects!r})"
        )


class Roles(Base):
    __tablename__ = "Roles"
    RoleID: Mapped[int] = mapped_column(primary_key=True)
    RoleTypeID: Mapped[int] = mapped_column(ForeignKey("RoleTypes.RoleTypeID"))
    Role: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return (
            f"Role(RoleID={self.RoleID!r}, RoleTypeID={self.RoleTypeID!r}, "
            f"Role={self.Role!r})"
        )


class RolesTypes(Base):
    __tablename__ = "RolesTypes"
    RoleTypeID: Mapped[int] = mapped_column(primary_key=True)
    RoleType: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"RolesType(RoleTypeID={self.RoleTypeID!r}, RoleType={self.RoleType!r})"


class TitleTypes(Base):
    __tablename__ = "TitleTypes"
    TitleTypeID: Mapped[int] = mapped_column(primary_key=True)
    TitleType: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return (
            f"TitleType(TitleTypeID={self.TitleTypeID!r}, "
            f"TitleType={self.TitleType!r})"
        )
