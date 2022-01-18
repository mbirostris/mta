from swimming_pool import SwimmingPool
import json


def load_pool():
    with open('data_config.json', 'r') as data_handle:
        data = json.load(data_handle)
        swimming_pool = SwimmingPool(data["name"], data["work_hours"], data["price_list"], data["lanes_number"])
        return swimming_pool
