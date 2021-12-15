import datetime
import random
from typing import List, Literal, Union
from pydantic import BaseModel, ValidationError

class Element(BaseModel):
    name: str
    amount: int

class ExplosiveElement(Element):
    explosivity: Literal["HIGH", "MEDIUM", "LOW"]



class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    elements: List[Union[Element, ExplosiveElement]]



if __name__ == "__main__":

    order = Order(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        elements= [
            Element(name="nail", amount=10),
            Element(name="nail", amount=10),
            ExplosiveElement(name="TNT", amount=10, explosivity="HIGH")
        ]
    )

    print("valid order")
    print(order)

    print("invalid order")
    try:
        order.elements.append(
            ExplosiveElement(name="TNT", amount=10, explosivity="Unknown")
        )
    except ValidationError as e:
        print(e)
        print(e.json())
    print(order)




