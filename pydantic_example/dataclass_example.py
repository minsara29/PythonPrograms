import datetime
from typing import List
from dataclasses import dataclass

@dataclass
class Order:
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    element: List[str]


if __name__ == "__main__":
    order1 = Order(
        1,
        "USA",
        datetime.datetime.now(),
        "its a proper order",
        ["10 wines", "3 whisky"]
    )

    print(f"this is proper {order1}")

    order2 = Order(
        2.2,
        "USA",
        datetime.datetime.now(),
        "its a NOT proper order",
        ["10 wines", "3 whisky"]
    )

    print(f"this orderId is float : {order2}")

    order3 = Order(
        [3],
        "USA",
        datetime.datetime.now(),
        "its a NOT proper order",
        ["10 wines", "3 whisky"]
    )

    print(f"this orderId is list : {order3}")


    #dataclass is not helping when runtime 