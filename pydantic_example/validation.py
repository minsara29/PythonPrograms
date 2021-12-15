import datetime
from typing import List
from pydantic import BaseModel, ValidationError, validator


class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    elements: List[str]

    @validator('elements')
    def validate_element(cls, v, values, **kwargs):
        if any([el for el in v if 'gun' in el]):
            raise Exception(
                f"the customer {values.get('description')} is trying to buy a 'GUN'"
            )


if __name__ == "__main__":
    order1 = Order(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        elements=["10 wines", "3 whisky"]
    )

    print(f"this is proper {order1}")

    try:
        order2 = Order(
            order_id=2,
            country="USA",
            order_at=datetime.datetime.now(),
            description="Kannan",
            elements=["10 winesgun", "3 whisky"]
        )
    except Exception as e:
        print(e)
    print(f"this orderId is float : {order2}")




    #dataclass is not helping when runtime