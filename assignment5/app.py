"""
strompris fastapi app entrypoint
"""
import datetime
import os
from typing import List, Optional

import altair as alt
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import uvicorn

from strompris import (
    ACTIVITIES,
    LOCATION_CODES,
    fetch_day_prices,
    fetch_prices,
    plot_activity_prices,
    plot_daily_prices,
    plot_prices,
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# `GET /` should render the `strompris.html` template
# with inputs:
# - request
# - location_codes: location code dict
# - today: current date
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "strompris.html",
        {
            "request": request,
            "location_codes": LOCATION_CODES,
            "today": datetime.date.today(),
        },
    )


# GET /plot_prices.json should take inputs:
# - locations (list from Query)
# - end (date)
# - days (int, default=7)
# all inputs should be optional
# return should be a vega-lite JSON chart (alt.Chart.to_dict())
# produced by `plot_prices`
# (task 5.6: return chart stacked with plot_daily_prices)


@app.get("/plot_prices.json")
async def plot_prices_json(
    locations: Optional[List[str]] = Query(None),
    end: Optional[datetime.date] = None,
    days: int = 7,
):
    if locations is None:
        locations = list(LOCATION_CODES.keys())
    df = fetch_prices(end_date=end, days=days, locations=locations)
    chart = plot_prices(df)
    return alt.Chart.to_dict(chart)


# Task 5.6 (bonus):
# `GET /activity` should render the `activity.html` template
# activity.html template must be adapted from `strompris.html`
# with inputs:
# - request
# - location_codes: location code dict
# - activities: activity energy dict
# - today: current date


...

# Task 5.6:
# `GET /plot_activity.json` should return vega-lite chart JSON (alt.Chart.to_dict())
# from `plot_activity_prices`
# with inputs:
# - location (single, default=NO1)
# - activity (str, default=shower)
# - minutes (int, default=10)


...


# mount your docs directory as static files at `/help`


def main():
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)


if __name__ == "__main__":
    main()
