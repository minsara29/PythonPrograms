import datetime
from typing import List
from pydantic import BaseModel, ValidationError


class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    element: List[str]


if __name__ == "__main__":
    order1 = Order(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        element=["10 wines", "3 whisky"]
    )

    print(f"this is proper {order1}")

    order2 = Order(
        order_id=2.2,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a NOT proper order",
        element=["10 wines", "3 whisky"]
    )

    print(f"this orderId is float : {order2}")

    try:
        order3 = Order(
            order_id=[3],
            country="USA",
            order_at=datetime.datetime.now(),
            description="its a NOT proper order",
            element=["10 wines", "3 whisky"]
        )
    except ValidationError as e:
        print(f"validation Error: {e}")
        print(f"JSON Format: {e.json()}")
    print(f"this orderId is list : {order3}")


    #dataclass is not helping when runtime