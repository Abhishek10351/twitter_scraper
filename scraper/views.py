import random
import datetime as dt
import json

# from . import utils
from . import db as database
from django.shortcuts import render


def scrape_twitter(request):
    if request.method == "POST":
        try:
            # trends = utils.get_trending_topics()
            trends = list(range(1, 6))
            random.shuffle(trends)
            datetime = dt.datetime.now()
            time = datetime.time().strftime("%I:%M %p")
            date = datetime.date().strftime("%d-%m-%Y")

            data = {"date": date, "time": time, "trends": trends[0:5]}
            inserted = database.db.insert(data)

            find_data = database.db.find_one({"_id": inserted.inserted_id})
            final_data = {
                "date": date,
                "time": time,
                "trends": trends[0:5],
                "inserted_data": find_data,
            }

            return render(request, "results.html", final_data)
        except Exception as e:
            print(e)
            return render(request, "error.html")

    return render(request, "index.html")
