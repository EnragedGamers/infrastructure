#!/usr/bin/python

# See: https://github.com/frostschutz/SourceLib (thanks god it's compatible python 2.6.6)
import SourceQuery
import Data

import json
import os
import sys

ip = 'servers.enragedgamers.net'
servers = { # servers[id] = port
    'csgo_retake': 27015, # csgo retake
    'tf2_deathrun': 27030, # tf2 deathrun
    'tf2_ff2': 27045 # tf2 ff2
}

def query():
    dist = [] # will handle raw servers data

    for server, port in servers.items():
        tmp = { 'server': server, 'status': 1, 'address': ip + port }

        query = SourceQuery.SourceQuery(ip, port)

        try:
            tmp['info'] = query.info()
            tmp['players'] = query.player()
        except:
            tmp['status'] = 0

        dist.append(tmp)

    return dist

# Write client data into "servers.json" at /public_html
def write_client(data, location='public_html/'):
    path = os.path.join(location, 'servers.json')
    if not os.path.exists(path):
        print('There is a problem with the \'servers.json\' file location.')
        return
    with open(path, 'r+') as f:
        f.write(data.clientJson())

def main(args):
    available = {
        'client': write_client
    }

    if not args[0] in available:
        print('[Servers data] The data you\'re trying to gather ({0}) isn\'t supported yet'.format(args[0]))
        return

    data = Data.Data(dist, [
        'map',
        'gamedesc',
        'hostname',
        'maxplayers',
        'numplayers'
    ])

    available[args[0]](data)

if __name__ == '__main__':
   main(sys.argv[1:])
