import re
from typing import NamedTuple

import argparse
import subprocess
import os
import bz2

import requests
from tqdm import tqdm

import proto.cstrike15_gcmessages_pb2 as csgo_pb


DICTIONARY = 'ABCDEFGHJKLMNOPQRSTUVWXYZabcdefhijkmnopqrstuvwxyz23456789'
DICTIONARY_LENGTH = len(DICTIONARY)
SHARECODE_PATTERN = re.compile(r'^CSGO(-?[\w]{5}){5}$')

class MatchInformation(NamedTuple):
    matchId: int
    reservationId: int
    tvPort: int

    def __str__(self):
        return f'{self.matchId} {self.reservationId} {self.tvPort}'

class InvalidShareCode(Exception):
    def __init__(self):
        super().__init__('Invalid share code')

def bytes_to_hex(bytes_list):
    return ''.join(f'{byte:02x}' for byte in bytes_list)

def bytes_to_bigint(bytes_list):
    hex_str = bytes_to_hex(bytes_list)
    return int(hex_str, 16)

def string_to_bytes(string):
    return [int(string[i:i+2], 16) for i in range(0, len(string), 2)]

def int16_to_bytes(number):
    return [(number & 0x0000ff00) >> 8, number & 0x000000ff]

def uint8_to_int8(number):
    return (number << 24) >> 24

def sum_array(array):
    return sum(array)

def share_code_to_bytes(share_code):
    if not SHARECODE_PATTERN.match(share_code):
        raise InvalidShareCode()
    
    share_code = re.sub(r'CSGO|-', '', share_code)
    chars = list(reversed(share_code))
    big = 0
    for char in chars:
        big = big * DICTIONARY_LENGTH + DICTIONARY.index(char)
    
    str_hex = f'{big:036x}'
    return string_to_bytes(str_hex)

def bytes_to_share_code(bytes_list):
    hex_str = bytes_to_hex(bytes_list)
    total = int(hex_str, 16)
    chars = ''
    for _ in range(25):
        rem = total % DICTIONARY_LENGTH
        chars += DICTIONARY[rem]
        total //= DICTIONARY_LENGTH
    
    return f'CSGO-{chars[0:5]}-{chars[5:10]}-{chars[10:15]}-{chars[15:20]}-{chars[20:25]}'

def encode_match(match_info: MatchInformation):
    match_bytes = list(reversed(string_to_bytes(f'{match_info.matchId:x}')))
    reservation_bytes = list(reversed(string_to_bytes(f'{match_info.reservationId:x}')))
    tv_bytes = list(reversed(int16_to_bytes(match_info.tvPort)))
    bytes_list = match_bytes + reservation_bytes + tv_bytes
    share_code = bytes_to_share_code(bytes_list)
    return share_code

def decode_match_share_code(share_code: str):
    bytes_list = share_code_to_bytes(share_code)
    match_id = bytes_to_bigint(bytes_list[0:8][::-1])
    reservation_id = bytes_to_bigint(bytes_list[8:16][::-1])
    tv_port = bytes_to_bigint(bytes_list[16:18][::-1])
    return MatchInformation(match_id, reservation_id, tv_port)

def extract_match_data(decode_match_share_code, share_code):
    cmd = f'boiler\\boiler-writter.exe data.info {decode_match_share_code(share_code)}'
    subprocess.run(cmd, shell=True)

def extract_map_url(f):
    data = f.read()
    match_list = csgo_pb.CMsgGCCStrike15_v2_MatchList()
    match_list.ParseFromString(data)
    url = match_list.matches[0].roundstatsall[-1].map
    return url

def download_map(url, filename):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('content-length', 0))
    with open(f'maps/{filename}', 'wb') as f:
        with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            for data in response.iter_content(chunk_size=1024):
                f.write(data)
                pbar.update(len(data))
    with open(f'maps/{filename[:-4]}', 'wb') as wf:
        rf = bz2.BZ2File(f'maps/{filename}', 'rb')
        data = rf.read()
        wf.write(data)
        rf.close()
    os.remove(f'maps/{filename}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download CS2 demo from a share code')
    parser.add_argument('share_code', type=str, help='CS2 demo share code')
    args = parser.parse_args()
    share_code = args.share_code
    extract_match_data(decode_match_share_code, share_code)
    with open('data.info', 'rb') as f:
        url = extract_map_url(f)
        filename = url.split('/')[-1]
        if os.path.exists(f'maps/{filename[:-4]}'):
            print(f'Map already downloaded: {filename}')
        else:
            download_map(url, filename)
            print(f'Map downloaded: {filename}')
    os.remove('data.info')