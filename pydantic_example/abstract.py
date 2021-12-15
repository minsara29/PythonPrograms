import abc
import datetime
import random
from typing import List, Literal
from pydantic import BaseModel, ValidationError


class Order(BaseModel):
    order_id: int
    country: str
    order_at: datetime.datetime
    description: str
    elements: List[str]

    @abc.abstractmethod
    def allocate_element(self):
        raise NotImplementedError


class HardwareOrder(Order):
    allocation_states: List[Literal["Processing", "Finished", "Failed"]] = []

    def allocate_element(self):
        for element in self.elements:
            self.allocation_states.append(random.choice(["Processing", "Finished", "Failed"]))

if __name__ == "__main__":

    order = HardwareOrder(
        order_id=1,
        country="USA",
        order_at=datetime.datetime.now(),
        description="its a proper order",
        elements=["10 wines", "3 whisky"]
    )

    order.allocate_element()

    for element, state in zip(order.elements, order.allocation_states):
        print(f"the element {element} is in {state}")

    # print(order)




