# all the data is copied from https://github.com/pnxenopoulos/awpy

import json

import matplotlib.pyplot as plt

import numpy as np

IMAGE_SIZE = 1024

NADE_COLOR_MAP = {
    "incendiary_grenade": "red",
    "molotov": "red",
    "smoke": "gray",
    "he_grenade": "green",
    "flashbang": "blue",
    "decoy": "black",
}

with open('data/map/map_data.json') as f:
    MAP_DATA = json.load(f)


def plot_map(map_name):
    map_data = MAP_DATA[map_name]
    img = plt.imread(f'data/map/{map_name}.png')
    if 'z_cutoff' in map_data:
        img_lower = plt.imread(f'data/map/{map_name}_lower.png')
        img = np.concatenate((img, img_lower), axis=0)
    plt.set_cmap('hot')
    fig, ax = plt.subplots()
    ax.set_axis_off()
    ax.imshow(img)
    return fig, ax


def flatten_positions(map_name, positions):
    map_data = MAP_DATA[map_name]
    start_x = map_data['pos_x']
    end_y = map_data['pos_y']
    scale = map_data['scale']
    positions = positions.copy()
    positions['X'] = (positions['X'] - start_x) / scale
    positions['Y'] = (end_y - positions['Y']) / scale
    if 'z_cutoff' in map_data and 'Z' in positions:
        positions['Y'] = np.where(
            positions['Z'] > map_data['z_cutoff'], positions['Y'], positions['Y'] + IMAGE_SIZE)
    if 'Z' in positions:
        positions.drop(columns=['Z'], inplace=True)
    return positions


def plot_positions(ax, positions, color='b', label=None):
    ax.plot(positions['X'], positions['Y'], color=color, label=label)


def plot_grenades(map_name, grenades):
    fig, ax = plot_map(map_name)

    grenades = grenades.copy()
    grenades_first = grenades[['first_X', 'first_Y', 'first_Z']].copy()
    grenades_first.columns = ['X', 'Y', 'Z']
    grenades_first = flatten_positions(map_name, grenades_first)
    grenades.loc[:, 'first_X'] = grenades_first['X']
    grenades.loc[:, 'first_Y'] = grenades_first['Y']

    grenades_last = grenades[['last_X', 'last_Y', 'last_Z']].copy()
    grenades_last.columns = ['X', 'Y', 'Z']
    grenades_last = flatten_positions(map_name, grenades_last)
    grenades.loc[:, 'last_X'] = grenades_last['X']
    grenades.loc[:, 'last_Y'] = grenades_last['Y']

    for _, grenade in grenades.iterrows():
        ax.plot(
            [grenade['first_X'], grenade['last_X']],
            [grenade['first_Y'], grenade['last_Y']],
            color=NADE_COLOR_MAP[grenade['grenade_type']],
            label=grenade['grenade_type']
        )
        ax.scatter(
            grenade['first_X'],
            grenade['first_Y'],
            color=NADE_COLOR_MAP[grenade['grenade_type']],
            marker='o'
        )
        ax.scatter(
            grenade['last_X'],
            grenade['last_Y'],
            color=NADE_COLOR_MAP[grenade['grenade_type']],
            marker='x'
        )

    return fig, ax