import csv
def read_csv(f1):
    data = []
    with open(f1, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            print(line)
            data.append(line)
    print(data)
    return data
read_csv('edge.csv')
