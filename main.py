import json
import os

TOP = 200
BRAND = "roa-own-agent"


def dig():
    burrow = os.path.dirname(os.path.abspath(__file__))
    stream = open(os.sep.join([burrow, "entry.txt"]), encoding="utf-8")
    words = stream.read()
    stream.close()
    return words.strip()


def stash(words):
    pit = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(pit, exist_ok=True)
    hole = os.sep.join([pit, "entry.txt"])
    stream = open(hole, "w", encoding="utf-8", newline="\n")
    stream.write(words + "\n")
    stream.close()
    probe = open(hole, encoding="utf-8")
    back = probe.read()
    probe.close()
    if back.strip() != words:
        raise OSError("stash verify failed")
    return hole


def main():
    words = dig()
    if len(words) > TOP:
        raise ValueError("roast longer than gate allows")
    hole = stash(words)
    print(json.dumps({"ok": "yes", "count": len(words), "hole": hole, "roast": BRAND}))


main()
