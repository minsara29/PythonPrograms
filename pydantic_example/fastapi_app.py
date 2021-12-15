import datetime
from typing import List, Literal, Union
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator
import uvicorn


app = FastAPI()

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


@app.post("/order")
async def process_order(order: Order):
    print(order)
    return "your order has been processed"


if __name__ == "__main__":
    # order1 = Order(
    #     order_id=1,
    #     country="USA",
    #     order_at=datetime.datetime.now(),
    #     description="its a proper order",
    #     elements=["10 wines", "3 whisky"]
    # )

    uvicorn.run(app)

