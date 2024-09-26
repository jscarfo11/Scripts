import csv
from ben import main as t
import time

data_path = "ben.csv"
result_file = "my_results.txt"
ind = 2




def main():
    results = []
    with open(data_path, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")
        header = next(csv_reader)
        types = {i: header[i] for i in range(3,9)}
        results.append(f"{header[2]},base 16 num,Mode")
        for row in csv_reader:
            for i in range(3,9):
                if row[i] != '':
                    results.append(f"{row[ind]},{int(row[i], base=16)},{types[i]}")

    with open(result_file, "w+") as f:
        f.write("\n".join(results))






if __name__ == "__main__":
    ben_start = time.time()
    t()
    ben_end = time.time()
    print(f"Ben's script took {ben_end - ben_start :.6f} seconds.")
    jack_start = time.time()
    main()
    jack_end = time.time()
    print(f"Jack's script took {jack_end - jack_start :.6f} seconds.")
