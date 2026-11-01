
from pathlib import Path
import sys

uploads = Path("uploads")
source = uploads / "source.svg"

# Get amount from GitHub Actions
amount = int(sys.argv[1])

if amount < 1 or amount > 5000:
    raise ValueError("Choose between 1 and 5000 copies.")

if not source.exists():
    raise FileNotFoundError("uploads/source.svg is missing!")

original = source.read_bytes()
links = []

for i in range(1, amount + 1):
    filename = f"copy-{i}.svg"
    (uploads / filename).write_bytes(original)

    url = (
        f"https://cdn.jsdelivr.net/gh/"
        f"bananas1234567/media@main/uploads/{filename}"
    )
    links.append(url)

Path("links.txt").write_text("\n".join(links) + "\n")

print(f"Successfully created {amount} SVG copies!")
print("Links saved to links.txt")
