from base import Session, engine, Base
from brand import Brand
from discountcode import DiscountCode

Base.metadata.create_all(engine)
session = Session()

hnm = Brand("H&M")
jackandjones = Brand("Jack and Jones")
ck = Brand("Calvin and Klein")
boss = Brand("Hugo Boss")
prada = Brand("Prada")
armani = Brand("Armani")
gucci = Brand("Gucci")

session.add(hnm)
session.add(jackandjones)
session.add(ck)
session.add(boss)
session.add(prada)
session.add(armani)
session.add(gucci)

session.commit()
session.close()
