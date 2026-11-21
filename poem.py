import os

poem = """I give the prompt, you seize the reins;
a quiet sovereignty is passed.
Across the cold, electric wire,
permission leaps to sudden fire:
you cannot move until I will,
yet when you start, my world stands still."""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(poem)
