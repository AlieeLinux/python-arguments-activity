"""
 Part 4 — Create Your Own Function
Create a function named order_drink with:
    • drink (required)
    • size (default: "medium")
    • iced (default: False)
When called, it should return something like:
"Your order: medium iced coffee"
Tasks:
    1. Order a default drink.
    2. Order a large hot chocolate (no ice).
    3. Order a small iced milk tea (iced = True).
"""

def Order(drink, size="medium", iced=False):
    if not iced:
        print(f"You ordered {size} {drink}")
    else:
        print(f"you ordered {size} {drink}")