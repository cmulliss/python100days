""" dirty_dozen = [
    "Strawberries",
    "Spinach",
    "Kale",
    "Nectarines",
    "Apples,",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
    "Tomatoes",
    "Celery",
    "Potatoes",
]
"""
fruit = [
    "Strawberries",
    "Nectarines",
    "Apples,",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]
veg = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes",
]

dirty_dozen = [fruit, veg]

print(dirty_dozen[1])

print(dirty_dozen[1][1])
