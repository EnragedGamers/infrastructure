# A little data building tool for Source servers
# Author : Gabriel Santamaria <gabyfle@enragedgamers.net>
# Python 2.6.6

import json

class Server:
    id = ''
    status = 0
    address = ''
    info = {}
    ping = 0
    players = []

    def __init__(self, serv):
        self.status = serv['status']
        self.address = serv['address']
        self.id = serv['server']

        if self.status == 0: return

        self.info = serv['info']
        self.ping = serv['info']['ping']
        self.players = serv['players']

    def playerCount():
        return len(players)

    def getInfo(info):
        if self.status == 0: return ''
        if not info in self.info: raise LookupError

        return self.info[info]

class Data:
    # Server data
    servers = []

    # Data that can be accessed by an user throught web
    client = []

    def __init__(self, servers, client):
        for server in servers:
            servers.append(Server(server))

        self.client = client

    def clientJson():
        """Build the data accessible by users throught web"""
        data = {}
        for server in self.servers:
            srv_data = {}
            srv_data['address'] = server.address
            srv_data['status'] = server.status

            srv_data['infos'] = {}
            for info in self.client:
                srv_data['infos'][info] = server.getInfo(info)

            srv_data['info']['nb_players'] = servers.playerCount()

            data[server.id] = srv_data

        return json.dumps(data)
