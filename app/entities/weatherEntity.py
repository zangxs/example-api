from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date
from app.config import Base

class WeatherEntity(Base):
    __tablename__ = "weather_records"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    ciudad: Mapped[str]
    date: Mapped[date]
    temp_cent: Mapped[float]
    temp_far: Mapped[float]