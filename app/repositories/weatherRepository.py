from app.entities.weatherEntity import WeatherEntity
from app.dto.request.weatherRequest import WeatherRequest
from app.dto.response.weatherResponse import WeatherResponse
from sqlalchemy import select
from sqlalchemy.orm import Session


class WeatherRepository:

    def search_by_city_and_date(self, db: Session, request: WeatherRequest):
        #TODO aca hacer la query a db
        stmt = select(WeatherEntity).where(
            WeatherEntity.ciudad == request.ciudad,
            WeatherEntity.date == request.date
        )

        return db.execute(stmt).scalar_one_or_none()
    
    def save(self, db: Session, entity: WeatherEntity):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity
