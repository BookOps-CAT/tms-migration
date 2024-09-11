from sqlalchemy import ForeignKey, String
from sqalchemy.org improt DeclartiveBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Medium(Base):
    __tablename__ = "Medium"
    MediumID = Mapped[int] = mapped_column(primary_key=True)
    Medium: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Medium(MediumID={self.MediumID!r}, Medium={self.Medium!r})"
