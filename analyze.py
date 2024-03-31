import argparse
from data import DemoAnalyzer

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='CS2 Demo Analyzer')
    arg_parser.add_argument('demo_file', type=str, help='CS2 demo file')
    args = arg_parser.parse_args()

    parser = DemoAnalyzer(args.demo_file)
    print(f'MAP: {parser.map_name}')
    print(f'PLAYERS: {parser.player_info}')
    parser.grenades.to_csv('results/grenades.csv', index=False)
    print('Grenades saved to results/grenades.csv')
