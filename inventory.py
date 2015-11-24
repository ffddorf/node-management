#!/usr/bin/env python2.7

import urllib
import json
import ipaddress
import argparse


def output_list_inventory(json_output):
    '''
    Output the --list data structure as JSON
    '''
    print(json.dumps(json_output))


def find_host(search_host, inventory):
    '''
    Find the given variables for the given host and output them as JSON
    '''
    host_attribs = inventory.get(search_host, {})
    print(json.dumps(host_attribs))


def get_nodes():
    json_url = "http://map.freifunk-duesseldorf.de/nodes.json"
    response = urllib.urlopen(json_url)
    nodes = json.loads(response.read().decode("utf-8"))['nodes']
    return nodes


def build_inventory():
    hosts = []

    for i, node in get_nodes().items():
        ip = get_ips_from_node(node)
        if ip is not False:
            hosts.append(ip)

    return {
        "nodes": {
            "hosts": hosts,
            "vars": {}
        }
    }


def get_global_ip(ip_adresses):
    ip = None
    for address in ip_adresses:
        if ipaddress.ip_address(address).is_global:
            ip = address
    if ip is None:
        return False
    return ip


def get_ips_from_node(node):
    if 'addresses' not in node['nodeinfo']['network']:
        return False
    return get_global_ip(node['nodeinfo']['network']['addresses'])


def main():
    '''
    Ansible dynamic inventory experimentation
    Output dynamic inventory as JSON from statically defined data structures
    '''

    # Argument parsing
    parser = argparse.ArgumentParser(description="Ansible dynamic inventory")
    parser.add_argument("--list",
                        help="Ansible inventory of all of the groups",
                        action="store_true", dest="list_inventory")
    parser.add_argument("--host",
                        help="Ansible inventory of a particular host",
                        action="store",
                        dest="ansible_host", type=str)

    cli_args = parser.parse_args()
    list_inventory = cli_args.list_inventory
    ansible_host = cli_args.ansible_host

    if list_inventory:
        ANSIBLE_INV = build_inventory()
        output_list_inventory(ANSIBLE_INV)

    if ansible_host:
        print("{}")


if __name__ == "__main__":
    main()
