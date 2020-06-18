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
# pylint: skip-file

"""
The module file for iosxr_lacp
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: iosxr_lacp
short_description: LACP resource module
description:
- This module manages Global Link Aggregation Control Protocol (LACP) on IOS-XR devices.
version_added: 1.0.0
author:
- Nilashish Chakraborty (@nilashishc)
- Rohit Thakur (@rohitthakur2590)
notes:
- Tested against IOS-XR 6.1.3.
- This module works with connection C(network_cli). See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
options:
  config:
    description: The provided configurations.
    type: dict
    suboptions:
      system:
        description: This option sets the default system parameters for LACP bundles.
        type: dict
        suboptions:
          priority:
            description:
            - The system priority to use in LACP negotiations.
            - Lower value is higher priority.
            - Refer to vendor documentation for valid values.
            type: int
          mac:
            type: dict
            description:
            - The system MAC related configuration for LACP.
            suboptions:
              address:
                description:
                - The system ID to use in LACP negotiations.
                type: str
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the IOS-XR device
      by executing the command B(show running-config lacp).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - deleted
    - parsed
    - rendered
    - gathered
    default: merged
"""
EXAMPLES = """
# Using merged
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#show running-config lacp
# Tue Jul 16 17:46:08.147 UTC
# % No such configuration item(s)
#
#

- name: Merge provided configuration with device configuration
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 10
        mac:
          address: 00c1.4c00.bd15
    state: merged

#
#
# -----------------------
# Module Execution Result
# -----------------------
#
# "before": {}
#
#
# "commands": [
#    "lacp system priority 10",
#    "lacp system mac 00c1.4c00.bd15"
#  ]
#
#
# "after": {
#    "system": {
#       "mac": {
#          "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#     }
#  }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:51:29.365 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#
#

# Using replaced
#
#
# -------------
# Before state
# -------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 17:53:59.904 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 10
#

- name: Replace device global lacp configuration with the given configuration
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 11
    state: replaced
#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 10
#    }
#  }
#
#
# "commands": [
#    "no lacp system mac",
#    "lacp system priority 11"
#  ]
#
#
# "after": {
#    "system": {
#       "priority": 11
#    }
# }
#
# -----------
# After state
# -----------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:02:40.379 UTC
# lacp system priority 11
#
#

# Using deleted
#
#
# ------------
# Before state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:37:09.727 UTC
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
#
#

- name: Delete global LACP configurations from the device
  cisco.iosxr.iosxr_lacp:
    state: deleted

#
#
# -----------------------
# Module Execution Result
# -----------------------
# "before": {
#    "system": {
#       "mac": {
#         "address": "00c1.4c00.bd15"
#       },
#       "priority": 11
#    }
# }
#
#
# "commands": [
#     "no lacp system mac",
#     "no lacp system priority"
# ]
#
#
# "after": {}
#
# ------------
# After state
# ------------
#
#
# RP/0/0/CPU0:iosxr01#sh run lacp
# Tue Jul 16 18:39:44.116 UTC
# % No such configuration item(s)
#
#


# Using parsed
# parsed.cfg
# ------------
#
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
# - name: Convert LACP config to argspec without connecting to the appliance
#   cisco.iosxr.iosxr_lacp:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": {
#         "system": {
#             "mac": {
#                 "address": "00c1.4c00.bd15"
#             },
#             "priority": 11
#         }
#     }


# Using rendered
- name: Render platform specific commands from task input using rendered state
  cisco.iosxr.iosxr_lacp:
    config:
      system:
        priority: 11
        mac:
          address: 00c1.4c00.bd15
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": [
#         "lacp system priority 11",
#         "lacp system mac 00c1.4c00.bd15"
#     ]


# Using gathered
# Before state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config lacp
# lacp system mac 00c1.4c00.bd15
# lacp system priority 11
- name: Gather IOSXR LACP configuration
  cisco.iosxr.iosxr_lacp:
    config:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": {
#         "system": {
#             "mac": {
#                 "address": "00c1.4c00.bd15"
#             },
#             "priority": 11
#         }
#     }
# After state:
# ------------
#
# RP/0/0/CPU0:an-iosxr-02#show running-config lacp
# lacp system mac 00c1.4c00.bd15
# lacp system priority


"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: dict
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['lacp system priority 10', 'lacp system mac 00c1.4c00.bd15']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.lacp.lacp import (
    LacpArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.lacp.lacp import (
    Lacp,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]

    mutually_exclusive = [("config", "running_config")]
    module = AnsibleModule(
        argument_spec=LacpArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
        mutually_exclusive=mutually_exclusive,
    )

    result = Lacp(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
