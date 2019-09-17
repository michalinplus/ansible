#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for vyos_lldp_interfaces
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: vyos_lldp_interfaces
version_added: 2.9
short_description: Manages attributes of lldp interfaces on VyOS devices.
description: This module manages attributes of lldp interfaces on VyOS network devices.
notes:
  - Tested against VyOS 1.1.8 (helium).
  - This module works with connection C(network_cli). See L(the VyOS OS Platform Options,../network/user_guide/platform_vyos.html).
author:
   - Rohit Thakur (@rohitthakur2590)
options:
  config:
    description: A list of lldp interfaces configurations.
    type: list
    suboptions:
      name:
        description:
          - Name of the  lldp interface.
        type: str
        required: True
      enable:
        description:
          - to disable lldp on the interface.
        type: bool
        default: True
      location:
        description:
          - LLDP-MED location data.
        type: dict
        suboptions:
          civic_based:
            description:
              - Civic-based location data.
            type: dict
            suboptions:
              ca_info:
                 description: LLDP-MED address info
                 type: list
                 suboptions:
                   ca_type:
                     description: LLDP-MED Civic Address type.
                     type: int
                     required: True
                   ca_value:
                     description: LLDP-MED Civic Address value.
                     type: str
                     required: True
              country_code:
                description: Country Code
                type: str
                required: True
          coordinate_based:
            description:
              - Coordinate-based location.
            type: dict
            suboptions:
              altitude:
                description: Altitude in meters.
                type: int
              datum:
                description: Coordinate datum type.
                type: str
                choices:
                  - WGS84
                  - NAD83
                  - MLLW
              latitude:
                description: Latitude.
                type: str
                required: True
              longitude:
                description: Longitude.
                type: str
                required: True
          elin:
            description: Emergency Call Service ELIN number (between 10-25 numbers).
            type: str
  state:
    description:
      - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged

"""
EXAMPLES = """
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration  commands | grep lldp
#
- name: Merge provided configuration with device configuration
  vyos_lldp_interfaces:
    config:
      - name: 'eth1'
        location:
          civic_based:
            country_code: 'US'
            ca_info:
              - ca_type: 0
                ca_value: 'ENGLISH'

      - name: 'eth2'
        location:
          coordinate_based:
           altitude: 2200
           datum: 'WGS84'
           longitude: '222.267255W'
           latitude: '33.524449N'
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": []
#
#    "commands": [
#        "set service lldp interface eth1 location civic-based country-code 'US'",
#        "set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'",
#        "set service lldp interface eth1",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth2 location coordinate-based altitude '2200'",
#        "set service lldp interface eth2 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth2 location coordinate-based longitude '222.267255W'",
#        "set service lldp interface eth2"
#
# "after": [
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth1"
#        }
#    ],
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'


# Using replaced
#
# Before state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth1 location civic-based country-code 'US'
# set service lldp interface eth2 location coordinate-based altitude '2200'
# set service lldp interface eth2 location coordinate-based datum 'WGS84'
# set service lldp interface eth2 location coordinate-based latitude '33.524449N'
# set service lldp interface eth2 location coordinate-based longitude '222.267255W'
#
- name: Replace device configurations of listed LLDP interfaces with provided configurations
  vyos_lldp_interfaces:
    config:
      - name: 'eth2'
        location:
          civic_based:
            country_code: 'US'
            ca_info:
              - ca_type: 0
                ca_value: 'ENGLISH'

      - name: 'eth1'
        location:
          coordinate_based:
           altitude: 2200
           datum: 'WGS84'
           longitude: '222.267255W'
           latitude: '33.524449N'
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": [
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
#    "commands": [
#        "delete service lldp interface eth2 location",
#        "set service lldp interface eth2 'disable'",
#        "set service lldp interface eth2 location civic-based country-code 'US'",
#        "set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'",
#        "delete service lldp interface eth1 location",
#        "set service lldp interface eth1 'disable'",
#        "set service lldp interface eth1 location coordinate-based latitude '33.524449N'",
#        "set service lldp interface eth1 location coordinate-based altitude '2200'",
#        "set service lldp interface eth1 location coordinate-based datum 'WGS84'",
#        "set service lldp interface eth1 location coordinate-based longitude '222.267255W'"
#    ]
#
#    "after": [
#        {
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
# After state:
# -------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth2 location civic-based country-code 'US'


# Using overridden
#
# Before state
# --------------
#
# vyos@vyos:~$ show configuration commands | grep lldp
# set service lldp interface eth1 'disable'
# set service lldp interface eth1 location coordinate-based altitude '2200'
# set service lldp interface eth1 location coordinate-based datum 'WGS84'
# set service lldp interface eth1 location coordinate-based latitude '33.524449N'
# set service lldp interface eth1 location coordinate-based longitude '222.267255W'
# set service lldp interface eth2 'disable'
# set service lldp interface eth2 location civic-based ca-type 0 ca-value 'ENGLISH'
# set service lldp interface eth2 location civic-based country-code 'US'
#
- name: Overrides all device configuration with provided configuration
  vyos_lag_interfaces:
    config:
     - name: 'eth2'
       location:
         elin: 0000000911

    state: overridden
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": [
#        {
#            "enable": false,
#            "location": {
#                "civic_based": {
#                    "ca_info": [
#                        {
#                            "ca_type": 0,
#                            "ca_value": "ENGLISH"
#                        }
#                    ],
#                    "country_code": "US"
#                }
#            },
#            "name": "eth2"
#        },
#        {
#            "enable": false,
#            "location": {
#                "coordinate_based": {
#                    "altitude": 2200,
#                    "datum": "WGS84",
#                    "latitude": "33.524449N",
#                    "longitude": "222.267255W"
#                }
#            },
#            "name": "eth1"
#        }
#    ]
#
#    "commands": [
#        "delete service lldp interface eth2 location",
#        "delete service lldp interface eth2 disable",
#        "set service lldp interface eth2 location elin 0000000911"
#
#
#    "after": [
#        {
#            "location": {
#                "elin": 0000000911
#            },
#            "name": "eth2"
#        }
#    ]
#
#
# After state
# ------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'


# Using deleted
#
# Before state
# -------------
#
# vyos@vyos# run show configuration commands | grep lldp
# set service lldp interface eth2 location elin '0000000911'
#
- name: Delete lldp  interface attributes of given interfaces.
  vyos_lag_interfaces:
    config:
     - name: 'eth2'
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
    "before": [
        {
            "location": {
                "elin": 0000000911
            },
            "name": "eth2"
        }
    ]
# "commands": [
#    "commands": [
#        "delete service lldp interface eth2"
#    ]
#
# "after": []
# After state
# ------------
# vyos@vyos# run show configuration commands | grep lldp
# set service 'lldp'


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "set service lldp interface eth2 'disable'"
    - "delete service lldp interface eth1 location"
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.vyos.argspec.lldp_interfaces.lldp_interfaces import Lldp_interfacesArgs
from ansible.module_utils.network.vyos.config.lldp_interfaces.lldp_interfaces import Lldp_interfaces


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',)),
                   ('state', 'overridden', ('config',))]
    module = AnsibleModule(argument_spec=Lldp_interfacesArgs.argument_spec, required_if=required_if,
                           supports_check_mode=True)

    result = Lldp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
