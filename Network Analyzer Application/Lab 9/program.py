# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:15:05 2020

@author: Rylie Horrall, Wyatt Haak
"""

from NetworkAnalyzer import NetworkAnalyzer


def main():
    filename = input('Enter in the PCAP filename: ')
    network_analyzer = NetworkAnalyzer(filename)

    search_opt = int(input('Choose analysis option:\n'
                           '(0) IPs by Connection\n'
                           '(1) IPs by Bytes\n'
                           '(2) Protocols by Connections\n'
                           '(3) Protocols by Bytes\n'
                           '(4) Connections by Connections\n'
                           '(5) Connections by Bytes\n'
                           '(6) Quit\n'))

    while search_opt != 6:
        if search_opt == 0:  # ips by connection
            result = network_analyzer.ips_by_connection()
            for i, item in enumerate(result):
                print(i, item)

        elif search_opt == 1:  # ips by bytes
            result = network_analyzer.ips_by_bytes()
            for i, item in enumerate(result):
                print(i, item)

        elif search_opt == 2:  # protocols by connections
            result = network_analyzer.protocols_by_connections()
            for i, item in enumerate(result):
                print(i, item)

        elif search_opt == 3:  # protocols by bytes
            result = network_analyzer.protocols_by_bytes()
            for i, item in enumerate(result):
                print(i, item)

        elif search_opt == 4:  # connections by connections
            result = network_analyzer.connections_by_connections()
            for i, item in enumerate(result):
                print(i, item)

        elif search_opt == 5:  # connections by connections
            result = network_analyzer.connections_by_bytes()
            for i, item in enumerate(result):
                print(i, item)

        print()
        search_opt = int(input('Choose analysis option:\n'
                               '(0) IPs by Connection\n'
                               '(1) IPs by Bytes\n'
                               '(2) Protocols by Connections\n'
                               '(3) Protocols by Bytes\n'
                               '(4) Connections by Connections\n'
                               '(5) Connections by Bytes\n'
                               '(6) Quit\n'))


if __name__ == '__main__':
    main()
