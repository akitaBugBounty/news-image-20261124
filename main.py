import hashlib
import os


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        data = f.read()
    digest = hashlib.sha256(data).hexdigest()
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        check = hashlib.sha256(f.read()).hexdigest()
    if check != digest:
        raise SystemExit("sha256 mismatch")
    print(digest)


if __name__ == "__main__":
    main()
