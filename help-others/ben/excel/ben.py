import csv

data_path = "ben.csv"
results = "results.txt"


def get_time_seeds(path: str):
    with open(path, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        return [row for row in csv_reader]


def extract_header(data):
    return data[0]


def trim_header(data):
    return [h.split("/") for h in data[3:]]


def get_timer_seed_column(data, col: int):
    return [[row[2], int(row[col], 16) if row[col] else None] for row in data]


def prune_data(data):
    return [row for row in data if row[1] is not None]


def append_settings(data, header, index: int):
    for row in data:
        if row[1] is not None:
            row.extend([header[index][1], header[index][0], "Start", "LG", "English"])
    return data


def main():
    data = get_time_seeds(data_path)
    header = trim_header(extract_header(data))
    data.pop(0)

    seed_start = 3
    result = []

    for col in range(6):
        filtered = get_timer_seed_column(data, seed_start)
        settings = append_settings(filtered, header, col)
        prune = prune_data(settings)
        seed_start += 1

        for row in prune:
            result.append(row)

    with open(results, "w") as file:
        for row in result:
            file.write(",".join(map(str, row)) + "\n")

    print(len(result))


if __name__ == "__main__":
    main()
