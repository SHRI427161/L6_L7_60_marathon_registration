def format_bib_name(name):
    """
    Upper-cases a runner's name and cuts it to 12 characters for the bib.
    Handles non-string and edge-case inputs gracefully without crashing.
    """
    try:
        if not isinstance(name, str):
            return ""
        return name.strip().upper()[:12]
    except Exception:
        return ""

def parse_finish_time(text):
    """
    Converts a finish time written as H:MM:SS into seconds.
    Handles malformed or non-string inputs gracefully without crashing.
    Returns total seconds as an integer, or None if invalid.
    """
    try:
        if not isinstance(text, str):
            return None
        parts = text.strip().split(':')
        if len(parts) != 3:
            return None
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = int(parts[2])
        if hours < 0 or minutes < 0 or seconds < 0:
            return None
        return hours * 3600 + minutes * 60 + seconds
    except Exception:
        return None

def average_split(text):
    """
    Averages split times given in minutes, separated by spaces.
    Handles malformed or non-string inputs gracefully without crashing.
    Returns average split as a float, or None if invalid.
    """
    try:
        if not isinstance(text, str):
            return None
        tokens = text.strip().split()
        if not tokens:
            return None
        splits = [int(s) for s in tokens]
        if any(s < 0 for s in splits):
            return None
        return sum(splits) / len(splits)
    except Exception:
        return None

def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    print("Finish time in seconds:", parse_finish_time(value))

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    print("Average split (minutes):", average_split(value))

if __name__ == "__main__":
    main()
