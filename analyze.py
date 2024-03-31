import os
import argparse
from data import DemoAnalyzer, plot_grenades
import matplotlib.pyplot as plt

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='CS2 Demo Analyzer')
    arg_parser.add_argument('demo_file', type=str, help='CS2 demo file')
    args = arg_parser.parse_args()

    parser = DemoAnalyzer(args.demo_file)
    print(f'MAP: {parser.map_name}')
    print(f'PLAYERS: {parser.player_info}')
    os.makedirs('results', exist_ok=True)
    parser.grenades.to_csv('results/grenades.csv', index=False)
    for round in parser.grenades['round'].unique():
        fig, ax = plot_grenades(
            parser.map_name, parser.grenades[parser.grenades['round'] == round])
        fig.savefig(f'results/grenades_{round}.png', bbox_inches='tight')
        plt.close()
