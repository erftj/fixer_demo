import json

from fixer.handler import get_rates


def archive(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


if __name__ == "__main__":
    res = get_rates()
    archive(res['timestamp'], res['rates'])
