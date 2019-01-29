import json
import re

def main():
    data = {}
    with open("./glossary.txt", "r") as f:
        text = f.read()
        rows = text.split("\n")
        for row in rows:
            keys = re.finditer(r"“([A-Za-z\s]+)”", row)
            value = re.search(r"”*.*”\s(.*)", row)
            value = value[1].replace("\u201c", '"')
            value = value.replace("\u201d", '"')
            value = value.replace("\u2019", "'")

            for key in keys:
                data[key[1]] = value
    with open("./glossary.json", "w") as f:
        f.write(json.dumps(data))

if __name__ == "__main__":
    main()
