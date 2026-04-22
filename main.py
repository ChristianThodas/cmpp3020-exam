import json

from Classes.Route import Route
from Classes.TransitStop import TransitStop


def load_data(filepath):
    with open("Data/data.json", "r") as f:
        data = json.load(f)

    stops = {}
    routes= []
    for s in data["stops"]:
        stops[s["id"]] = TransitStop(s["id"], s["name"])

    # Load routes
    for r in data["routes"]:
        routes.append(
            Route(
                stops[r["from"]],
                stops[r["to"]],
                r["time"]
            )
        )
    return stops, routes

stops,routes = load_data("Data/data.json")