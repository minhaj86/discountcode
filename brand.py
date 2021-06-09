from sqlalchemy import Column, String, Integer

from base import Base


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    brand_name = Column(String)

    def __init__(self, brand_name):
        self.brand_name = brand_name

