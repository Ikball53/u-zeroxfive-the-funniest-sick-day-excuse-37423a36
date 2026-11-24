import os

# One concrete detail, deadpan: a real injury caused by the snooze button itself.
ENTRY = "I pulled a muscle reaching for the snooze button, so I'm staying home to recover from my own alarm clock today."

def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()
