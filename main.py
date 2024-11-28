import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Olympics Medal Analysis')
    parser.add_argument('file', type=str, help='File with data')
    parser.add_argument('-medals', nargs=2, type=str, help='Country code and year of Olympic games')
    parser.add_argument('-total', type=int, help='Year to see country`s medals')
    parser.add_argument('-output', type=str, help='File to output results')
    parser.add_argument('-overall', nargs=" ", type=str, help='Best year for country in Olympics')
    return parser.parse_args()

def read_data(file_path):
    data = []
    with open(file_path, 'r') as f:
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

def show_medals(args):
    country = args.medals[0]
    year = int(args.medals[1])
    medals = {"Gold": 0, "Silver": 0, "Bronze": 0}
    country_medals = []

    data = read_data(args.file)

    for row in data:
        if (row['Team'] == country or row['NOC'] == country) and int(row['Year']) == year:
            medal_type = row['Medal']
            if medal_type and medal_type != 'NA':
                country_medals.append(f"{row['Name']} - {row['Event']} - {medal_type}")
                medals[medal_type] += 1

    for medalist in country_medals[:10]:
        print(medalist)

    print(f"Gold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}")

    if args.output:
        with open(args.output, 'w') as output_file:
            for medalist in country_medals[:10]:
                output_file.write(medalist + '\n')
            output_file.write(f"\nGold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}")


def show_total_medals(args):
    year = args.total
    medals_by_country = {}

    data = read_data(args.file)

    for row in data:
        if int(row['Year']) == year:
            country = row['Team']
            medal_type = row['Medal']
            if country not in medals_by_country:
                medals_by_country[country] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            if medal_type != 'NA':
                medals_by_country[country][medal_type] += 1

    for country, medals in medals_by_country.items():
        print(f"{country} - Gold: {medals['Gold']}, Silver: {medals['Silver']}, Bronze: {medals['Bronze']}")

def show_overall(args):
    countries = args.overall.split(' ')
    data = read_data(args.file)

    for country in countries:
        country_summary = {}
        for row in data:
            if row['Team'] == country:
                year = row['Year']
                medal = row['Medal']
                if year not in country_summary:
                    country_summary[year] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                if medal != 'N/A':
                    country_summary[year][medal] += 1

        best_year = min(country_summary)
        for years in country_summary:
             if country_summary[years]['Gold'] > country_summary[best_year]['Gold']:
                best_year = years
             elif country_summary[years]['Gold'] == country_summary[best_year]['Gold'] and country_summary[years]['Silver'] > country_summary[best_year]['Silver']:
                best_year = years
             elif country_summary[years]['Gold'] == country_summary[best_year]['Gold'] and country_summary[years]['Silver'] == country_summary[best_year]['Silver'] and country_summary[years]['Bronze'] > country_summary[best_year]['Bronze']:
                best_year = years

        print(f'{country} best year was {best_year}. They collect {country_summary[best_year]['Gold']} gold medals, {country_summary[best_year]['Silver']} silver medals, {country_summary[best_year]['Bronze']} bronze medals.')

def main():
    args = parse_arguments()
    if args.medals:
        show_medals(args)
    elif args.total:
        show_total_medals(args)
    elif args.overall(args):
        show_overall(args)
    else:
        print("Invalid command or missing arguments.")
if __name__ == '__main__':
    main()