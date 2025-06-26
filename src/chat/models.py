from sqlalchemy import Column, Integer, String
from src.auth.connection import Base
class Messages(Base):
    __tablename__ = "messages"  # Указываем имя таблицы

    id = Column(Integer, primary_key=True)
    message = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}