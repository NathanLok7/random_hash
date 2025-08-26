# random_hash.py
import uuid
import sys

def main():
    for attempt in range(1, 1001):  # 1000 attempts
        candidate = uuid.uuid4().hex  # 32-char random hex string
        if candidate.startswith("00"):
            print(f"PASS: Found hash after {attempt} attempts:\n{candidate}")
            sys.exit(0)
    print("FAIL: No matching hash found in 1000 attempts.")
    sys.exit(1)

if __name__ == "__main__":
    main()
