import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Olympics Medal Analysis')
    parser.add_argument('file', type=str, help='File with data')
    parser.add_argument('-medals', type=str, help='Country code and year of Olympic games')
    parser.add_argument('-total', type=int, help='Year to see country`s medals')
    parser.add_argument('-output', type=str, help='File to output results')
    return parser.parse_args()

def read_data(file):
    data = []
    with open(file, 'r') as f:
        table_headlines = f.readline()
        for line in f:
            row = line.strip().split('\t')
            data.append({
                'ID': row[0],
                'Name': row[1],
                'Sex': row[2],
                'Age': row[3],
                'Height': row[4],
                'Weight': row[5],
                'Team': row[6],
                'NOC': row[7],
                'Games': row[8],
                'Year': row[9],
                'Season': row[10],
                'City': row[11],
                'Sport': row[12],
                'Event': row[13],
                'Medal': row[14]
            })
    return data