#!/usr/bin/python3.6

READ_ME = '''
=== PREREQUISITES ===
Run in Python 3.6+

Install the requests & Meraki Python modules:
pip[3] install --upgrade requests
pip[3] install --upgrade meraki

Have input CSV file with network name, second octet, and third octet specified.
Bind those networks to template that has VLANs configured.

=== DESCRIPTION ===
This script iterates through a dashboard org's MX networks, optionally filtered
on a given tag, and configures the VLANs' IP addressing according to the
template and input octets.

=== USAGE ===
python[3] configure_vlans.py -f <input_file> -k <api_key> -o <org_id>
    [-t <tag>] [-m <mode>]
Mode defaults to "simulate" unless "commit" is specified.

'''


import csv
from datetime import datetime
import getopt
import logging
import sys

import requests
import meraki


logger = logging.getLogger(__name__)


def configure_logging(script_file):
    logging.basicConfig(
        filename=f'{script_file}_log_{datetime.now():%Y%m%d_%H%M%S}.txt',
        level=logging.DEBUG,
        format='%(asctime)s: %(levelname)7s: [%(name)s]: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')


# Prints READ_ME help message for user to read
def print_help():
    lines = READ_ME.split('\n')
    for line in lines:
        print('# {0}'.format(line))


def main(argv, csv_writer):
    # Set default values for command line arguments
    arg_file = api_key = org_id = arg_tag = arg_mode = None

    # Get command line arguments
    try:
        opts, args = getopt.getopt(argv, 'hf:k:o:t:m:')
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit()
        elif opt == '-f':
            arg_file = arg
        elif opt == '-k':
            api_key = arg
        elif opt == '-o':
            org_id = arg
        elif opt == '-t':
            arg_tag = arg
        elif opt == '-m':
            arg_mode = arg

    # Check if all required parameters have been input
    if arg_file == None or api_key == None or org_id == None:
        print_help()
        sys.exit(2)

    # Assign default mode to "simulate" unless "commit" specified
    if arg_mode != 'commit':
        arg_mode = 'simulate'

    # Read and process input file
    mappings = {}
    with open(arg_file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        next(csv_reader, None)
        # Iterate through CSV for each the vlan to adjust to network
        for row in csv_reader:
            name = row[0]
            subnet3 = row[1]
            subnet4 = row[2]
            subnet5 = row[3]
            subnet6 = row[4]
            subnet7 = row[5]
            subnet8 = row[6]
            subnet9 = row[7]
            subnet10 = row[8]
            subnet11 = row[9]
            mxip3 = row[10]
            mxip4 = row[11]
            mxip5 = row[12]
            mxip6 = row[13]
            mxip7 = row[14]
            mxip8 = row[15]
            mxip9 = row[16]
            mxip10 = row[17]
            mxip11 = row[18]
            relay = row[19]
            mappings[name] = (subnet3, subnet4, subnet5, subnet6, subnet7, subnet8, subnet9, subnet10, subnet11, mxip3, mxip4, mxip5, mxip6, mxip7, mxip8, mxip9, mxip10, mxip11, relay)

        logger.info(f'Processed {len(mappings)} rows from input CSV')


    # Get networks in org
    dashboard = meraki.DashboardAPI(api_key)
    networks = dashboard.organizations.getOrganizationNetworks(
    org_id, total_pages='all'
)

    # Filter on optional tag
    if arg_tag:
        target_networks = [network for network in networks if network['tags'] and arg_tag in network['tags']]
    else:
        target_networks = networks

    # Iterate through all networks
    logger.info(f'Iterating through {len(target_networks)} networks:')
    for network in target_networks:
        name = network['name']

        # Network not in input file
        if name not in mappings:
            logger.error(f'Did not find network {name} within input CSV file, so skipping!')
            continue

        # Configure VLANs for network
        if arg_mode == 'commit':
            logger.info(f'Configuring VLANs for network {name}...')
            net_id = network['id']

#            for
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 3, subnet=f'{subnet3}', applianceIp=f'{mxip3}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            name={result[name]}
            id=result[id]
            subnet=result[subnet]
            applianceIP=[applianceIP]
            writestatus(name,id,subnet,applianceIP)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 4, subnet=f'{subnet4}', applianceIp=f'{mxip4}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 5, subnet=f'{subnet5}', applianceIp=f'{mxip5}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 6, subnet=f'{subnet6}', applianceIp=f'{mxip6}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result= dashboard.appliance.updateNetworkApplianceVlan(net_id, 7, subnet=f'{subnet7}', applianceIp=f'{mxip7}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 8, subnet=f'{subnet8}', applianceIp=f'{mxip8}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 9, subnet=f'{subnet9}', applianceIp=f'{mxip9}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 10, subnet=f'{subnet10}', applianceIp=f'{mxip10}')
            writestatus(result)
            result = dashboard.appliance.updateNetworkApplianceVlan(net_id, 11, subnet=f'{subnet11}', applianceIp=f'{mxip11}', dhcpHandling='Relay DHCP to another server', dhcpRelayServerIps=[relay])
            writestatus(result)


        else:
            logger.info(f'Simulating configuration of VLANs for network {name}')

    logger.info('Completed iteration of networks!')

# Define Writestatus function
def writestatus(
   name,id,subnet,applianceIP,
):
    """Define Writestatus function"""
    (
    #if type(result) == dict and 'id' in result:
        csv_writer.writerow({'Network': name,
                             'VLAN Name': result['name'],
                             'VLAN ID': result['id'],
                             'Subnet': result['subnet'],
                             'MX IP': result['applianceIp'],
                             'Result': 'SUCCESS!'
                             })
#        logger.info(f'Successfully configured VLAN {vlan}!')
#    else:
#        csv_writer.writerow({'Network': name,
 #                            'Subnet': result['subnet'],
 #                            'MX IP': result[applianceIp],
 #                            'Result': result[0]
 #                            })
#        logger.error(f'Problem configuring VLAN {vlan}! Please see log/results.')
    )


if __name__ == '__main__':
    inputs = sys.argv[1:]
    if len(inputs) == 0:
        print_help()
        sys.exit(2)
    script_file = sys.argv[0].split('.')[0]

    # Configure logging to stdout
    configure_logging(script_file)
    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # Set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # Tell the handler to use this format
    console.setFormatter(formatter)
    # Add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # Set the CSV output file
    script_file = sys.argv[0].split('.')[0]
    time_now = f'{datetime.now():%Y%m%d_%H%M%S}'
    file_name = f'{script_file}_results_{time_now}.csv'
    output_file = open(file_name, mode='w', newline='\n')

    # Write the header row
    field_names = ['Network', 'VLAN Name', 'VLAN ID', 'Subnet', 'MX IP', 'Result']
    #csv_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    csv_writer = csv.DictWriter(output_file, field_names, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    #csv_writer.writerow(field_names)
    csv_writer.writeheader()
    logger.info(f'Output of results to file: {file_name}')

    # Output to logfile/console starting inputs, sans API key
    key_index = inputs.index('-k')
    inputs.pop(key_index+1)
    inputs.pop(key_index)
    start_time = datetime.now()
    logger.info(f'Started script at {start_time}')
    logger.info(f'Input parameters: {inputs}')

    # Call main function
    main(sys.argv[1:], csv_writer)

    # Finish output to logfile/console
    end_time = datetime.now()
    logger.info(f'Ended script at {end_time}')
    logger.info(f'Total run time = {end_time - start_time}')
