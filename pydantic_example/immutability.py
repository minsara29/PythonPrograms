import datetime
from typing import List
from pydantic import BaseModel, ValidationError


class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    element: List[str]

    class Config:
        """
        base model with Immutability
        """
        allow_mutation = False

if __name__ == "__main__":

    order = Order(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        element=["10 wines", "3 whisky"]
    )

    print(order)

    try:
        order.order_id = 2
    except TypeError as e:
        print(e)

    print(order)


    #dataclass is not helping when runtime