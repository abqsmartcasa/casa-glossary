import json
import re

def main():
    data = []
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
                term = {}
                term['term'] = key[1]
                term['definition'] = value
                data.append(term)

    with open("./glossary.json", "w") as f:
        f.write(json.dumps(data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
