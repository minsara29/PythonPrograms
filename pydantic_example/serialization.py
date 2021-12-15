import datetime
from typing import List
import humps
from pydantic import BaseModel, ValidationError


class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    element: List[str]

    class Config:
        alias_generator = humps.camelize
        allow_population_by_field_name = True


if __name__ == "__main__":
    order1 = Order(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        element=["10 wines", "3 whisky"]
    )

    print(f"this is proper {order1}")

    print(order1.json(by_alias=True))

    order2 = Order(
        orderId=2,
        country="India",
        orderAt=datetime.datetime.now(),
        description="its a proper order",
        element=["10 wines", "3 whisky"]
    )

    print(f"this is proper {order2}")

    external_body = {
        "order_id": 3,
        "country": "USA",
         "order_at": datetime.datetime.now(),
         "description": "its a proper order",
        "element": ["10 wines", "3 whisky"]
    }

    external_order = Order(**external_body) # same as above

    print(external_order)

    external_body1 = {
        "orderId": 4,
        "country": "USA",
         "orderAt": datetime.datetime.now(),
         "description": "its a proper order",
        "element": ["10 wines", "3 whisky"]
    }

    external_order1 = Order.parse_obj(external_body1)

    print(external_order1)
