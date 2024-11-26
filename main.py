import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Olympics Medal Analysis')
    parser.add_argument('file', type=str, help='File with data')
    parser.add_argument('-medals', type=str, help='Country code and year of Olympic games')
    parser.add_argument('-total', type=int, help='Year to see country`s medals')
    parser.add_argument('-output', type=str, help='File to output results')
    return parser.parse_args()
