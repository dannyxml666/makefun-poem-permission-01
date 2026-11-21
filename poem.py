import os

poem = """I type the prompt and ask:
may we open this?
You test the weight,
lift the latch,
and nod.
For one bright second
neither of us holds
the heavy door alone."""

os.makedirs('/output', exist_ok=True)
with open('/output/entry.txt', 'w', encoding='utf-8') as f:
    f.write(poem)
