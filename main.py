import pendulum

from typing import Union
from fastapi import FastAPI

from utils.dates import period_range

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    today = pendulum.now()
    one_month_ago = today.subtract(months=1)

    date_range = list(period_range(today, one_month_ago, step_type="weeks"))

    return {"total_weeks": len(date_range)}
