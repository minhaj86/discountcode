from sqlalchemy import Column, String, Integer, ForeignKey
from enum import Enum
from base import Base


class DiscountCodeState(Enum):
    UNUSED = 0
    DISTRIBUTED = 1
    USED = 1


class DiscountCode(Base):
    __tablename__ = 'discount_code'

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    code = Column(String)
    state = Column(Integer)

    def __init__(self, brand_id, code, state=DiscountCodeState.UNUSED):
        self.brand_id = brand_id
        self.code = code
        self.state = state
