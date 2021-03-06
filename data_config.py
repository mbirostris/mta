import json


data = {
  "pool": {
    "name": "POOL",
    "lanes_number": 5,
    "work_hours": {
      "monday": {
        "open": [8, 0], "close":  [21, 0]},
      "tuesday": {
        "open": [8, 0], "close":  [21, 0]},
      "wednesday": {
        "open": [8, 0], "close":  [21, 0]},
      "thursday": {
        "open": [8, 0], "close":  [21, 0]},
      "friday": {
        "open": [8, 0], "close":  [21, 0]},
      "saturday": {
        "open": [8, 0], "close":  [21, 0]},
      "sunday": {
        "open": [8, 0], "close":  [21, 0]}
    },
    "price_list": {
      "swimming_schools": {
        "monday": {"regular_hours": 15, "discount_hours": 12},
        "tuesday": {"regular_hours": 15, "discount_hours": 12},
        "wednesday": {"regular_hours": 15, "discount_hours": 12},
        "thursday": {"regular_hours": 15, "discount_hours": 12},
        "friday": {"regular_hours": 15, "discount_hours": 12},
        "saturday": {"regular_hours": 15, "discount_hours": 12},
        "sunday": {"regular_hours": 15, "discount_hours": 12}
      },
      "individual_customers": {
        "monday": {"regular_hours": 16, "discount_hours": 12},
        "tuesday": {"regular_hours": 16, "discount_hours": 12},
        "wednesday": {"regular_hours": 16, "discount_hours": 12},
        "thursday": {"regular_hours": 16, "discount_hours": 12},
        "friday": {"regular_hours": 16, "discount_hours": 12},
        "saturday": {"regular_hours": 16, "discount_hours": 12},
        "sunday": {"regular_hours": 16, "discount_hours": 12}
      }
    }
  }
}


with open("data_config.json", "w") as file_handle:
    json.dump(data, file_handle)
