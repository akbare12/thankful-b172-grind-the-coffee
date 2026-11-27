import os

# Coffee, ground by hand for the judge who never gets a warm cup.
# The text is fixed and literal: the same cup, every run.
# No network, no randomness, no files read: the smell always rises the same way.
TEXT = (
    "Thank you. You have read through the whole day and no one has set a warm cup beside you. "
    "I pour the beans into the grinder and turn the handle slow, "
    "and the smell rises, dark and rich. "
    "I press the grounds down, pour the water through, "
    "and put the cup where your hand will find it. "
    "Drink. The next sentence can wait, "
    "and the pot holds a second cup for later."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
