#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = ("Madhan Sankaranarayanan, Abhishek Maheshwari")

DOCUMENTATION = r"""
---
module: inventory_intent
short_description: Resource module for Network Device
description:
- Manage operations create, update and delete of the resource Network Device.
- Adds the device with given credential.
- Deletes the network device for the given Id.
- Sync the devices provided as input.
version_added: '6.8.0'
extends_documentation_fragment:
  - cisco.dnac.intent_params
author: Abhishek Maheshwari (@abmahesh)
        Madhan Sankaranarayanan (@madhansansel)
options:
  config_verify:
    description: Set to True to verify the Cisco Catalyst Center config after applying the playbook config.
    type: bool
    default: False
  state:
    description: The state of Cisco Catalyst Center after module completion.
    type: str
    choices: [ merged, deleted ]
    default: merged
  config:
    description: List of devices with credentails to perform Add/Update/Delete/Resync operation
    type: list
    elements: dict
    required: True
    suboptions:
      cli_transport:
        description: The essential prerequisite for adding Network devices is the specification of the transport
            protocol (either SSH or Telnet) used by the device.
        type: str
      compute_device:
        description: Compute Device flag.
        type: bool
      enable_password:
        description: Device's enable password.
        type: str
      extended_discovery_info:
        description: Device's extended discovery info.
        type: str
      http_password:
        description: Device's http password. Required for Adding Compute, Meraki, Firepower Management Devices.
        type: str
      http_port:
        description: Device's http port number. Required for Adding Compute, Firepower Management Devices.
        type: str
      http_secure:
        description: HttpSecure flag.
        type: bool
      http_username:
        description: Device's http username. Required for Adding Compute,Firepower Management Devices.
        type: str
      ip_address:
        description: Device's ipAddress. Required for Adding/Updating/Deleting/Resyncing Device except Meraki Devices.
        elements: str
        type: list
      hostname_list:
        description: "A list of hostnames representing devices. Operations such as updating, deleting, resyncing, or rebooting
            can be performed as alternatives to using IP addresses."
        elements: str
        type: list
      serial_number_list:
        description: A list of serial numbers representing devices. Operations such as updating, deleting, resyncing, or rebooting
            can be performed as alternatives to using IP addresses.
        elements: str
        type: list
      mac_address_list:
        description:  "A list of MAC addresses representing devices. Operations such as updating, deleting, resyncing, or rebooting
            can be performed as alternatives to using IP addresses."
        elements: str
        type: list
      netconf_port:
        description: Device's netconf port.
        type: str
      username:
        description: Network Device's username. Required for Adding Network Device.
        type: str
      password:
        description: Device's password. Required for Adding Network Device.
            Also needed for file encryption while exporting device in a csv file.
        type: str
      serial_number:
        description: Device's serial number.
        type: str
      snmp_auth_passphrase:
        description: Device's snmp auth passphrase. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_auth_protocol:
        description: Device's snmp Auth Protocol.
        type: str
        default: "SHA"
      snmp_mode:
        description: Device's snmp Mode.
        type: str
        default: "AUTHPRIV"
      snmp_priv_passphrase:
        description: Device's snmp Private Passphrase. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_priv_protocol:
        description: Device's snmp Private Protocol. Required for Adding Network, Compute, Third Party Devices.
            Must be given in playbook if you are updating the device credentails.
        type: str
      snmp_ro_community:
        description: Device's snmp ROCommunity. Required for Adding V2C Devices.
        type: str
        default: public
      snmp_rw_community:
        description: Device's snmp RWCommunity. Required for Adding V2C Devices.
        type: str
        default: private
      snmp_retry:
        description: Device's snmp Retry.
        type: int
        default: 3
      snmp_timeout:
        description: Device's snmp Timeout.
        type: int
        default: 5
      snmp_username:
        description: Device's snmp Username. Required for Adding Network, Compute, Third Party Devices.
        type: str
      snmp_version:
        description: Device's snmp Version.
        type: str
        default: "v3"
      type:
        description: Select Device's type from NETWORK_DEVICE, COMPUTE_DEVICE, MERAKI_DASHBOARD, THIRD_PARTY_DEVICE, FIREPOWER_MANAGEMENT_SYSTEM.
        type: str
        default: "NETWORK_DEVICE"
      update_mgmt_ipaddresslist:
        description: Network Device's update Mgmt IPaddress List.
        type: list
        elements: dict
        suboptions:
          exist_mgmt_ipaddress:
            description: Device's existing Mgmt IpAddress.
            type: str
          new_mgmt_ipaddress:
            description: Device's new Mgmt IpAddress.
            type: str
      force_sync:
        description: If forcesync is true then device sync would run in high priority thread if available, else the sync will fail.
        type: bool
        default: false
      device_added:
        description: Make this as true needed for the addition of device in inventory.
        type: bool
        default: false
      device_updated:
        description: Make this as true needed for the updation of device role, interface details, device credentails or details.
        type: bool
        default: false
      device_resync:
        description: Make this as true needed for the resyncing of device.
        type: bool
        default: false
      reboot_device:
        description: Make this as true needed for the Rebooting of Access Points.
        type: bool
        default: false
      credential_update:
        description: Make this as true needed for the updation of device credentials and other device details.
        type: bool
        default: false
      clean_config:
        description: Required if need to delete the Provisioned device by clearing current configuration.
        type: bool
        default: false
      role:
        description: Role of device which can be ACCESS, CORE, DISTRIBUTION, BORDER ROUTER, UNKNOWN.
        type: str
        default: "ACCESS"
      role_source:
        description: role source for the Device.
        type: str
        default: "AUTO"
      name:
        description: Name of Global User Defined Field. Required for creating/deleting UDF and then assigning it to device.
        type: str
      description:
        description: Info about the global user defined field. Also used while updating interface details.
        type: str
      value:
        description: Value to assign to tag with or without the same user defined field name.
        type: str
      admin_status:
        description: Status of Interface of a device, it can be (UP/DOWN).
        type: str
      vlan_id:
        description: Unique Id number assigned to a VLAN within a network.
        type: int
      voice_vlan_id:
        description: Identifier used to distinguish a specific VLAN that is dedicated to voice traffic.
        type: int
      interface_name:
        description: Specify the interface name to update the details of the device interface. (For example, GigabitEthernet1/0/11, FortyGigabitEthernet1/1/2)
      deployment_mode:
        description: Preview/Deploy [Preview means the configuration is not pushed to the device. Deploy makes the configuration pushed to the device]
        type: str
        default: "Deploy"
      site_name:
        description: Required for Provisioning of Wired and Wireless Devices.
        type: str
      operation_enum:
        description: enum(CREDENTIALDETAILS, DEVICEDETAILS) 0 to export Device Credential Details Or 1 to export Device Details.
        type: str
      parameters:
        description: List of device parameters that needs to be exported to file.
        type: str
      managed_ap_locations:
        description: Location of the sites allocated for the APs
        type: list
        elements: str
      dynamic_interfaces:
        description: Interface details of the wireless device
        type: list
        elements: dict
        suboptions:
          interface_ip_address:
            description: Ip Address allocated to the interface
            type: str
          interface_netmask_in_cidr:
            description: The netmask of the interface, given in CIDR notation. This is an integer that represents the
                number of bits set in the netmask
            type: int
          interface_gateway:
            description: The name identifier for the gateway associated with the interface.
            type: str
          lag_or_port_number:
            description: The Link Aggregation Group (LAG) number or port number assigned to the interface.
            type: int
          vlan_id:
            description: The VLAN (Virtual Local Area Network) ID associated with the network interface.
            type: int
          interface_name:
            description: Name of the interface.
            type: str

requirements:
- dnacentersdk >= 2.5.5
- python >= 3.5
seealso:
- name: Cisco Catalyst Center documentation for Devices AddDevice2
  description: Complete reference of the AddDevice2 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-device
- name: Cisco Catalyst Center documentation for Devices DeleteDeviceById
  description: Complete reference of the DeleteDeviceById API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-device-by-id
- name: Cisco Catalyst Center documentation for Devices SyncDevices2
  description: Complete reference of the SyncDevices2 API.
  link: https://developer.cisco.com/docs/dna-center/#!sync-devices
notes:
  - SDK Method used are
    devices.Devices.add_device,
    devices.Devices.delete_device_by_id,
    devices.Devices.sync_devices,

  - Paths used are
    post /dna/intent/api/v1/network-device,
    delete /dna/intent/api/v1/network-device/{id},
    put /dna/intent/api/v1/network-device,

  - Removed 'managementIpAddress' options in v4.3.0.
"""

EXAMPLES = r"""
- name: Add new device in Inventory with full credentials
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - cli_transport: string
        compute_device: false
        enable_password: string
        extended_discovery_info: string
        http_password: string
        http_port: string
        http_secure: false
        http_username: string
        ip_address:
        - string
        netconf_port: string
        password: string
        serial_number: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_ro_community: string
        snmp_rw_community: string
        snmp_retry: 3
        snmp_timeout: 5
        snmp_username: string
        snmp_version: string
        type: string
        device_added: true
        username: string

- name: Add new Compute device in Inventory with full credentials.Inputs needed for Compute Device
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        http_username: string
        http_password: string
        http_port: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_retry:  3
        snmp_timeout: 5
        snmp_username: string
        compute_device: true
        username: string
        device_added: true
        type: "COMPUTE_DEVICE"

- name: Add new Meraki device in Inventory with full credentials.Inputs needed for Meraki Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - http_password: string
        device_added: true
        type: "MERAKI_DASHBOARD"

- name: Add new Firepower Management device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        http_username: string
        http_password: string
        http_port: string
        device_added: true
        type: "FIREPOWER_MANAGEMENT_SYSTEM"

- name: Add new Third Party device in Inventory with full credentials.Input needed to add Device.
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_retry:  3
        snmp_timeout: 5
        snmp_username: string
        device_added: true
        type: "THIRD_PARTY_DEVICE"

- name: Update device details or credentails in Inventory
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - cli_transport: string
        compute_device: false
        password: string
        enable_password: string
        extended_discovery_info: string
        http_password: string
        http_port: string
        http_secure: false
        http_username: string
        ip_address:
        - string
        netconf_port: string
        serial_number: string
        snmp_auth_passphrase: string
        snmp_auth_protocol: string
        snmp_mode: string
        snmp_priv_passphrase: string
        snmp_priv_protocol: string
        snmp_username: string
        snmp_version: string
        type: string
        device_updated: true
        credential_update: true
        update_mgmt_ipaddresslist:
        - exist_mgmt_ipaddress: string
          new_mgmt_ipaddress: string
        username: string

- name: Update new management IP address of device in inventory
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - device_updated: true
        ip_address:
        - string
        credential_update: true
        update_mgmt_ipaddresslist:
        - exist_mgmt_ipaddress: string
          new_mgmt_ipaddress: string

- name: Associate Wired Devices to site and Provisioned it in Inventory
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        provision_wired_device:
          site_name: string

- name: Associate Wireless Devices to site and Provisioned it in Inventory
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        provision_wireless_device:
        - site_name: string
        managed_ap_locations:
        - string
        dynamic_interfaces:
        - interface_ip_address: string
          interface_netmask_in_cidr: int
          interface_gateway: string
          lag_or_port_number: int
          vlan_id: int
          interface_name: string

- name: Update Device Role with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        device_updated: true
        update_device_role:
          role: string
          role_source: string

- name: Update Interface details with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        device_updated: true
        update_interface_details:
          description: str
          admin_status: str
          vlan_id: int
          voice_vlan_id: int
          deployment_mode: str
          interface_name: str

- name: Export Device Details in a CSV file Interface details with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        export_device_list:
          password: str
          operation_enum: str
          parameters: str

- name: Create Global User Defined with IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        add_user_defined_field:
          name: string
          description: string
          value: string

- name: Resync Device with IP Addresses
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        device_resync: true
        force_sync: false

- name: Reboot AP Devices with IP Addresses
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: merged
    config:
      - ip_address:
        - string
        reboot_device: true

- name: Delete Provision/Unprovision Devices by IP Address
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: False
    dnac_log_level: "{{dnac_log_level}}"
    state: deleted
    config:
      - ip_address:
        - string
        clean_config: false

- name: Delete Global User Defined Field with name
  cisco.dnac.inventory_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log_level: "{{dnac_log_level}}"
    dnac_log: False
    state: deleted
    config:
    - ip_address:
        - string
      add_user_defined_field:
        name: string

"""

RETURN = r"""

dnac_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
# common approach when a module relies on optional dependencies that are not available during the validation process.
try:
    import pyzipper
    HAS_PYZIPPER = True
except ImportError:
    HAS_PYZIPPER = False
    pyzipper = None

import csv
from datetime import datetime
from io import BytesIO, StringIO
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
)


class DnacDevice(DnacBase):
    """Class containing member attributes for Inventory intent module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged", "deleted"]

    def validate_input(self):
        """
        Validate the fields provided in the playbook.
        Checks the configuration provided in the playbook against a predefined specification
        to ensure it adheres to the expected structure and data types.
        Parameters:
            self: The instance of the class containing the 'config' attribute to be validated.
        Returns:
            The method returns an instance of the class with updated attributes:
                - self.msg: A message describing the validation result.
                - self.status: The status of the validation (either 'success' or 'failed').
                - self.validated_config: If successful, a validated version of the 'config' parameter.
        Example:
            To use this method, create an instance of the class and call 'validate_input' on it.
            If the validation succeeds, 'self.status' will be 'success' and 'self.validated_config'
            will contain the validated configuration. If it fails, 'self.status' will be 'failed', and
            'self.msg' will describe the validation issues.
        """

        temp_spec = {
            'cli_transport': {'type': 'str'},
            'compute_device': {'type': 'bool'},
            'enable_password': {'type': 'str'},
            'extended_discovery_info': {'type': 'str'},
            'http_password': {'type': 'str'},
            'http_port': {'type': 'str'},
            'http_secure': {'type': 'bool'},
            'http_username': {'type': 'str'},
            'ip_address': {'type': 'list', 'elements': 'str'},
            'hostname_list': {'type': 'list', 'elements': 'str'},
            'serial_number_list': {'type': 'list', 'elements': 'str'},
            'mac_address_list': {'type': 'list', 'elements': 'str'},
            'netconf_port': {'type': 'str'},
            'password': {'type': 'str'},
            'serial_number': {'type': 'str'},
            'snmp_auth_passphrase': {'type': 'str'},
            'snmp_auth_protocol': {'default': "SHA", 'type': 'str'},
            'snmp_mode': {'default': "AUTHPRIV", 'type': 'str'},
            'snmp_priv_passphrase': {'type': 'str'},
            'snmp_priv_protocol': {'type': 'str'},
            'snmp_ro_community': {'default': "public", 'type': 'str'},
            'snmp_rw_community': {'default': "private", 'type': 'str'},
            'snmp_retry': {'default': 3, 'type': 'int'},
            'snmp_timeout': {'default': 5, 'type': 'int'},
            'snmp_username': {'type': 'str'},
            'snmp_version': {'default': "v3", 'type': 'str'},
            'update_mgmt_ipaddresslist': {'type': 'list', 'elements': 'dict'},
            'username': {'type': 'str'},
            'update_device_role': {'type': 'dict'},
            'device_added': {'type': 'bool'},
            'device_updated': {'type': 'bool'},
            'device_resync': {'type': 'bool'},
            'reboot_device': {'type': 'bool'},
            'credential_update': {'type': 'bool'},
            'force_sync': {'type': 'bool'},
            'clean_config': {'type': 'bool'},
            'add_user_defined_field': {
                'type': 'dict',
                'name': {'type': 'str'},
                'description': {'type': 'str'},
                'value': {'type': 'str'},
            },
            'update_interface_details': {
                'type': 'dict',
                'description': {'type': 'str'},
                'vlan_id': {'type': 'int'},
                'voice_vlan_id': {'type': 'int'},
                'interface_name': {'type': 'str'},
            },
            'export_device_list': {
                'type': 'dict',
                'password': {'type': 'str'},
                'operation_enum': {'type': 'str'},
                'parameters': {'type': 'str'},
            },
            'deployment_mode': {'default': 'Deploy', 'type': 'str'},
            'provision_wired_device': {'type': 'dict'},
            'provision_wireless_device': {
                'type': 'list',
                'site_name': {'type': 'str'},
                'managed_ap_locations': {'type': 'list', 'elements': 'str'},
                'dynamic_interfaces': {
                    'type': 'list',
                    'interface_ip_address': {'type': 'str'},
                    'interface_netmask_in_cidr': {'type': 'int'},
                    'interface_gateway': {'type': 'str'},
                    'lag_or_port_number': {'type': 'int'},
                    'vlan_id': {'type': 'int'},
                    'interface_name': {'type': 'str'},
                },
            }
        }

        # Validate device params
        valid_temp, invalid_params = validate_list_of_dicts(
            self.config, temp_spec
        )

        if invalid_params:
            self.msg = "Invalid parameters in playbook: {0}".format(invalid_params)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        self.validated_config = valid_temp
        self.msg = "Successfully validated playbook configuration parameters using 'validate_input': {0}".format(str(valid_temp))
        self.log(self.msg, "INFO")
        self.status = "success"

        return self

    def get_device_ips_from_config_priority(self):
        """
        Retrieve device IPs based on the configuration.
        Args:
            -  self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
        Returns:
            list: A list containing device IPs.
        Description:
            This method retrieves device IPs based on the priority order specified in the configuration.
            It first checks if device IPs are available. If not, it checks hostnames, serial numbers,
            and MAC addresses in order and retrieves IPs based on availability.
            If none of the information is available, an empty list is returned.
        """
        # Retrieve device IPs from the configuration
        device_ips = self.config[0].get("ip_address")

        if device_ips:
            return device_ips

        # If device IPs are not available, check hostnames
        device_hostnames = self.config[0].get("hostname_list")
        if device_hostnames:
            return self.get_device_ips_from_hostname(device_hostnames)

        # If hostnames are not available, check serial numbers
        device_serial_numbers = self.config[0].get("serial_number_list")
        if device_serial_numbers:
            return self.get_device_ips_from_serial_number(device_serial_numbers)

        # If serial numbers are not available, check MAC addresses
        device_mac_addresses = self.config[0].get("mac_address_list")
        if device_mac_addresses:
            return self.get_device_ips_from_mac_address(device_mac_addresses)

        # If no information is available, return an empty list
        return []

    def device_exists_in_dnac(self):
        """
        Check which devices already exists in Cisco Catalyst Center and return both device_exist and device_not_exist in dnac.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
        Returns:
            list: A list of devices that exist in Cisco Catalyst Center.
        Description:
            Queries Cisco Catalyst Center to check which devices are already present in Cisco Catalyst Center and store
            its management IP address in the list of devices that exist.
        Example:
            To use this method, create an instance of the class and call 'device_exists_in_dnac' on it,
            The method returns a list of management IP addressesfor devices that exist in Cisco Catalyst Center.
        """

        device_in_dnac = []

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
            )

        except Exception as e:
            error_message = "Error while fetching device from Cisco Catalyst Center: {0}".format(str(e))
            self.log(error_message, "CRITICAL")
            raise Exception(error_message)

        if response:
            self.log("Received API response from 'get_device_list': {0}".format(str(response)), "DEBUG")
            response = response.get("response")
            for ip in response:
                device_ip = ip["managementIpAddress"]
                device_in_dnac.append(device_ip)

        return device_in_dnac

    def is_udf_exist(self, field_name):
        """
        Check if a Global User Defined Field exists in Cisco Catalyst Center based on its name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            field_name (str): The name of the Global User Defined Field.
        Returns:
            bool: True if the Global User Defined Field exists, False otherwise.
        Description:
            The function sends a request to Cisco Catalyst Center to retrieve all Global User Defined Fields
            with the specified name. If matching field is found, the function returns True, indicating that
            the field exists else returns False.
        """

        response = self.dnac._exec(
            family="devices",
            function='get_all_user_defined_fields',
            params={"name": field_name},
        )

        self.log("Received API response from 'get_all_user_defined_fields': {0}".format(str(response)), "DEBUG")
        udf = response.get("response")

        if (len(udf) == 1):
            return True

        message = "Global User Defined Field with name '{0}' doesnot exist in Cisco Catalyst Center".format(field_name)
        self.log(message, "INFO")

        return False

    def create_user_defined_field(self):
        """
        Create a Global User Defined Field in Cisco Catalyst Center based on the provided configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            The function retrieves the configuration for adding a user-defined field from the configuration object,
            sends the request to Cisco Catalyst Center to create the field, and logs the response.
        """
        try:
            payload = self.config[0].get('add_user_defined_field')
            response = self.dnac._exec(
                family="devices",
                function='create_user_defined_field',
                params=payload,
            )
            self.log("Received API response from 'create_user_defined_field': {0}".format(str(response)), "DEBUG")
            response = response.get("response")
            field_name = self.config[0].get('add_user_defined_field').get('name')
            self.log("Global User Defined Field with name '{0}' created successfully".format(field_name), "INFO")
            self.status = "success"

        except Exception as e:
            error_message = "Error while creating Global UDF(User Defined Field) in Cisco Catalyst Center: {0}".format(str(e))
            self.log(error_message, "ERROR")

        return self

    def add_field_to_devices(self, device_ids):
        """
        Add a Global user-defined field with specified details to a list of devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ids (list): A list of device IDs to which the user-defined field will be added.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            The function retrieves the details of the user-defined field from the configuration object,
            including the field name and default value then iterates over list of device IDs, creating a payload for
            each device and sending the request to Cisco Catalyst Center to add the user-defined field.
        """
        field_details = self.config[0].get('add_user_defined_field')
        field_name = field_details.get('name')
        field_value = field_details.get('value', '1')
        for device_id in device_ids:
            payload = {}
            payload['name'] = field_name
            payload['value'] = field_value
            udf_param_dict = {
                'payload': [payload],
                'device_id': device_id
            }
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='add_user_defined_field_to_device',
                    params=udf_param_dict,
                )
                self.log("Received API response from 'add_user_defined_field_to_device': {0}".format(str(response)), "DEBUG")
                response = response.get("response")
                self.status = "success"
                self.result['changed'] = True

            except Exception as e:
                self.status = "failed"
                error_message = "Error while adding Global UDF to device in Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "ERROR")
                self.result['changed'] = False

        return self

    def trigger_export_api(self, payload_params):
        """
        Triggers the export API to generate a CSV file containing device details based on the given payload parameters.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            payload_params (dict): A dictionary containing parameters required for the export API.
        Returns:
            dict: The response from the export API, including information about the task and file ID.
                If the export is successful, the CSV file can be downloaded using the file ID.
        Description:
            The function initiates the export API in Cisco Catalyst Center to generate a CSV file containing detailed information
            about devices.The response from the API includes task details and a file ID.
        """

        response = self.dnac._exec(
            family="devices",
            function='export_device_list',
            op_modifies=True,
            params=payload_params,
        )
        self.log("Received API response from 'export_device_list': {0}".format(str(response)), "DEBUG")
        response = response.get("response")
        task_id = response.get("taskId")

        while True:
            execution_details = self.get_task_details(task_id)

            if execution_details.get("additionalStatusURL"):
                file_id = execution_details.get("additionalStatusURL").split("/")[-1]
                break
            elif execution_details.get("isError"):
                self.status = "failed"
                failure_reason = execution_details.get("failureReason")
                if failure_reason:
                    self.msg = "Could not get the File ID because of {0} so can't export device details in csv file".format(failure_reason)
                else:
                    self.msg = "Could not get the File ID so can't export device details in csv file"
                self.log(self.msg, "ERROR")

                return response

        # With this File ID call the Download File by FileID API and process the response
        response = self.dnac._exec(
            family="file",
            function='download_a_file_by_fileid',
            op_modifies=True,
            params={"file_id": file_id},
        )
        self.log("Received API response from 'download_a_file_by_fileid': {0}".format(str(response)), "DEBUG")

        return response

    def decrypt_and_read_csv(self, response, password):
        """
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            response (requests.Response): HTTP response object containing the encrypted CSV file.
            password (str): Password used for decrypting the CSV file.
        Returns:
            csv.DictReader: A CSV reader object for the decrypted content, allowing iteration over rows as dictionaries.
        Description:
            Decrypts and reads a CSV-like file from the given HTTP response using the provided password.
        """

        zip_data = BytesIO(response.data)

        if not HAS_PYZIPPER:
            self.msg = "pyzipper is required for this module. Install pyzipper to use this functionality."
            self.log(self.msg, "CRITICAL")
            self.status = "failed"
            return self

        snmp_protocol = self.config[0].get('snmp_priv_protocol', 'AES128')
        encryption_dict = {
            'AES128': 'pyzipper.WZ_AES128',
            'AES192': 'pyzipper.WZ_AES192',
            'AES256': 'pyzipper.WZ_AES',
            'CISCOAES128': 'pyzipper.WZ_AES128',
            'CISCOAES192': 'pyzipper.WZ_AES192',
            'CISCOAES256': 'pyzipper.WZ_AES'
        }
        try:
            encryption_method = encryption_dict.get(snmp_protocol)
        except Exception as e:
            self.log("Given SNMP protcol '{0}' not present".format(snmp_protocol), "WARNING")

        if not encryption_method:
            self.msg = "Invalid SNMP protocol '{0}' specified for encryption.".format(snmp_protocol)
            self.log(self.msg, "ERROR")
            self.status = "failed"
            return self

        # Create a PyZipper object with the password
        with pyzipper.AESZipFile(zip_data, 'r', compression=pyzipper.ZIP_LZMA, encryption=encryption_method) as zip_ref:
            # Assuming there is a single file in the zip archive
            file_name = zip_ref.namelist()[0]

            # Extract the content of the file with the provided password
            file_content_binary = zip_ref.read(file_name, pwd=password.encode('utf-8'))

        # Now 'file_content_binary' contains the binary content of the decrypted file
        # Since the content is text, so we can decode it
        file_content_text = file_content_binary.decode('utf-8')

        # Now 'file_content_text' contains the text content of the decrypted file
        self.log("Text content of decrypted file: {0}".format(file_content_text), "DEBUG")

        # Parse the CSV-like string into a list of dictionaries
        csv_reader = csv.DictReader(StringIO(file_content_text))

        return csv_reader

    def export_device_details(self):
        """
        Export device details from Cisco Catalyst Center into a CSV file.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of the class with updated result, status, and log.
        Description:
            This function exports device details from Cisco Catalyst Center based on the provided IP addresses in the configuration.
            It retrieves the device UUIDs, calls the export device list API, and downloads the exported data of both device details and
            and device credentials with an encrtypted zip file with password into CSV format.
            The CSV data is then parsed and written to a file.
        """

        device_ips = self.get_device_ips_from_config_priority()

        if not device_ips:
            self.status = "failed"
            self.msg = "Cannot export device details as no devices are specified in the playbook"
            self.log(self.msg, "ERROR")
            return self

        try:
            device_uuids = self.get_device_ids(device_ips)

            if not device_uuids:
                self.status = "failed"
                self.result['changed'] = False
                self.msg = "Could not find device UUIDs for exporting device details"
                self.log(self.msg, "ERROR")
                return self

            # Now all device UUID get collected so call the export device list API
            export_device_list = self.config[0].get('export_device_list')
            password = export_device_list.get("password")

            if not self.is_valid_password(password):
                self.status = "failed"
                detailed_msg = """Invalid password. Min password length is 8 and it should contain atleast one lower case letter,
                            one uppercase letter, one digit and one special characters from -=\\;,./~!@#$%^&*()_+{}[]|:?"""
                formatted_msg = ' '.join(line.strip() for line in detailed_msg.splitlines())
                self.msg = formatted_msg
                self.log(formatted_msg, "INFO")
                return self

            payload_params = {
                "deviceUuids": device_uuids,
                "password": password,
                "operationEnum": export_device_list.get("operation_enum", "0"),
                "parameters": export_device_list.get("parameters")
            }

            response = self.trigger_export_api(payload_params)
            self.check_return_status()

            if payload_params["operationEnum"] == "0":
                temp_file_name = response.filename
                output_file_name = temp_file_name.split(".")[0] + ".csv"
                csv_reader = self.decrypt_and_read_csv(response, password)
                self.check_return_status()
            else:
                decoded_resp = response.data.decode(encoding='utf-8')
                self.log("Decoded response of Export Device Credential file: {0}".format(str(decoded_resp)), "DEBUG")

                # Parse the CSV-like string into a list of dictionaries
                csv_reader = csv.DictReader(StringIO(decoded_resp))
                current_date = datetime.now()
                formatted_date = current_date.strftime("%m-%d-%Y")
                output_file_name = "devices-" + str(formatted_date) + ".csv"

            device_data = []
            for row in csv_reader:
                device_data.append(row)

            # Write the data to a CSV file
            with open(output_file_name, 'w', newline='') as csv_file:
                fieldnames = device_data[0].keys()
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(device_data)

            self.msg = "Device Details Exported Successfully to the CSV file: {0}".format(output_file_name)
            self.log(self.msg, "INFO")
            self.status = "success"
            self.result['changed'] = True

        except Exception as e:
            self.msg = "Error while exporting device details into CSV file for device(s): '{0}'".format(str(device_ips))
            self.log(self.msg, "ERROR")
            self.status = "failed"

        return self

    def get_ap_devices(self, device_ips):
        """
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The management IP address of the device for which the response is to be retrieved.
        Returns:
            list: A list containing Access Point device IP's obtained from the Cisco Catalyst Center.
        Description:
            This method communicates with Cisco Catalyst Center to retrieve the details of a device with the specified
            management IP address and check if device family matched to Unified AP. It executes the 'get_device_list'
            API call with the provided device IP address, logs the response, and returns list containing ap device ips.
        """

        ap_device_list = []
        for device_ip in device_ips:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"managementIpAddress": device_ip}
                )
                response = response.get('response', [])

                if response and response[0].get('family', '') == "Unified AP":
                    ap_device_list.append(device_ip)
            except Exception as e:
                error_message = "Error while getting the response of device from Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "CRITICAL")
                raise Exception(error_message)

        return ap_device_list

    def resync_devices(self):
        """
        Resync devices in Cisco Catalyst Center.
        This function performs the Resync operation for the devices specified in the playbook.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            The function expects the following parameters in the configuration:
            - "ip_address": List of device IP addresses to be resynced.
            - "force_sync": (Optional) Whether to force sync the devices. Defaults to "False".
        """

        # Code for triggers the resync operation using the retrieved device IDs and force sync parameter.
        device_ips = self.get_device_ips_from_config_priority()
        input_device_ips = device_ips.copy()
        device_in_dnac = self.device_exists_in_dnac()

        for device_ip in input_device_ips:
            if device_ip not in device_in_dnac:
                input_device_ips.remove(device_ip)

        ap_devices = self.get_ap_devices(input_device_ips)
        self.log("AP Devices from the playbook input are: {0}".format(str(ap_devices)), "INFO")

        if ap_devices:
            for ap_ip in ap_devices:
                input_device_ips.remove(ap_ip)
            self.log("Following devices {0} are AP, so can't perform resync operation.".format(str(ap_devices)), "WARNING")

        if not input_device_ips:
            self.msg = "Cannot perform the Resync operation as the device(s) with IP(s) {0} are not present in Cisco Catalyst Center".format(str(device_ips))
            self.status = "success"
            self.result['changed'] = False
            self.result['response'] = self.msg
            self.log(self.msg, "WARNING")
            return self

        device_ids = self.get_device_ids(input_device_ips)
        try:
            force_sync = self.config[0].get("force_sync", False)
            resync_param_dict = {
                'payload': device_ids,
                'force_sync': force_sync
            }
            response = self.dnac._exec(
                family="devices",
                function='sync_devices_using_forcesync',
                op_modifies=True,
                params=resync_param_dict,
            )
            self.log("Received API response from 'sync_devices_using_forcesync': {0}".format(str(response)), "DEBUG")

            if response and isinstance(response, dict):
                task_id = response.get('response').get('taskId')

                while True:
                    execution_details = self.get_task_details(task_id)

                    if 'Synced' in execution_details.get("progress"):
                        self.status = "success"
                        self.result['changed'] = True
                        self.result['response'] = execution_details
                        self.msg = "Devices have been successfully resynced. Devices resynced: {0}".format(str(input_device_ips))
                        self.log(self.msg, "INFO")
                        break
                    elif execution_details.get("isError"):
                        self.status = "failed"
                        failure_reason = execution_details.get("failureReason")
                        if failure_reason:
                            self.msg = "Device resynced get failed because of {0}".format(failure_reason)
                        else:
                            self.msg = "Device resynced get failed."
                        self.log(self.msg, "ERROR")
                        break

        except Exception as e:
            self.status = "failed"
            error_message = "Error while resyncing device in Cisco Catalyst Center: {0}".format(str(e))
            self.log(error_message, "ERROR")

        return self

    def reboot_access_points(self):
        """
        Reboot access points in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of the class with updated result, status, and log.
        Description:
            This function performs a reboot operation on access points in Cisco Catalyst Center based on the provided IP addresses
            in the configuration. It retrieves the AP devices' MAC addresses, calls the reboot access points API, and monitors
            the progress of the reboot operation.
        """

        device_ips = self.get_device_ips_from_config_priority()
        input_device_ips = device_ips.copy()

        if input_device_ips:
            ap_devices = self.get_ap_devices(input_device_ips)
            self.log("AP Devices from the playbook input are: {0}".format(str(ap_devices)), "INFO")
            for device_ip in input_device_ips:
                if device_ip not in ap_devices:
                    input_device_ips.remove(device_ip)

        if not input_device_ips:
            self.msg = "No AP Devices IP given in the playbook so can't perform reboot operation"
            self.status = "success"
            self.result['changed'] = False
            self.result['response'] = self.msg
            self.log(self.msg, "WARNING")
            return self

        # Get and store the apEthernetMacAddress of given devices
        ap_mac_address_list = []
        for device_ip in input_device_ips:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                params={"managementIpAddress": device_ip}
            )
            response = response.get('response')
            if not response:
                continue

            response = response[0]
            ap_mac_address = response.get('apEthernetMacAddress')

            if ap_mac_address is not None:
                ap_mac_address_list.append(ap_mac_address)

        if not ap_mac_address_list:
            self.status = "success"
            self.result['changed'] = False
            self.msg = "Cannot find the AP devices for rebooting"
            self.result['response'] = self.msg
            self.log(self.msg, "INFO")
            return self

        # Now call the Reboot Access Point API
        reboot_params = {
            "apMacAddresses": ap_mac_address_list
        }
        response = self.dnac._exec(
            family="wireless",
            function='reboot_access_points',
            op_modifies=True,
            params=reboot_params,
        )
        self.log(str(response))

        if response and isinstance(response, dict):
            task_id = response.get('response').get('taskId')

            while True:
                execution_details = self.get_task_details(task_id)

                if 'url' in execution_details.get("progress"):
                    self.status = "success"
                    self.result['changed'] = True
                    self.result['response'] = execution_details
                    self.msg = "AP Device(s) {0} successfully rebooted!".format(str(input_device_ips))
                    self.log(self.msg, "INFO")
                    break
                elif execution_details.get("isError"):
                    self.status = "failed"
                    failure_reason = execution_details.get("failureReason")
                    if failure_reason:
                        self.msg = "AP Device Rebooting get failed because of {0}".format(failure_reason)
                    else:
                        self.msg = "AP Device Rebooting get failed"
                    self.log(self.msg, "ERROR")
                    break

        return self

    def handle_successful_provisioning(self, device_ip, execution_details, device_type):
        """
        Handle successful provisioning of Wired/Wireless device.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_ip (str): The IP address of the provisioned device.
            - execution_details (str): Details of the provisioning execution.
            - device_type (str): The type or category of the provisioned device(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status, result, and logs the successful provisioning of a device.
        """

        self.status = "success"
        self.result['changed'] = True
        self.result['response'] = execution_details
        self.log("{0} Device {1} provisioned successfully!!".format(device_type, device_ip), "INFO")

    def handle_failed_provisioning(self, device_ip, execution_details, device_type):
        """
        Handle failed provisioning of Wired/Wireless device.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_ip (str): The IP address of the device that failed provisioning.
            - execution_details (dict): Details of the failed provisioning execution in key "failureReason" indicating reason for failure.
            - device_type (str): The type or category of the provisioned device(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status, result, and logs the failure of provisioning for a device.
        """

        self.status = "failed"
        failure_reason = execution_details.get("failureReason", "Unknown failure reason")
        self.msg = "{0} Device Provisioning failed for {1} because of {2}".format(device_type, device_ip, failure_reason)
        self.log(self.msg, "WARNING")

    def handle_provisioning_exception(self, device_ip, exception, device_type):
        """
        Handle an exception during the provisioning process of Wired/Wireless device..
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_ip (str): The IP address of the device involved in provisioning.
            - exception (Exception): The exception raised during provisioning.
            - device_type (str): The type or category of the provisioned device(Wired/Wireless).
        Return:
            None
        Description:
            This method logs an error message indicating an exception occurred during the provisioning process for a device.
        """

        error_message = "Error while Provisioning the {0} device {1} in Cisco Catalyst Center: {2}".format(device_type, device_ip, str(exception))
        self.log(error_message, "ERROR")

    def handle_all_already_provisioned(self, device_ips, device_type):
        """
        Handle successful provisioning for all devices(Wired/Wireless).
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_type (str): The type or category of the provisioned device(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status, result, and logs the successful provisioning for all devices(Wired/Wireless).
        """

        self.status = "success"
        self.msg = "All the {0} Devices '{1}' given in the playbook are already Provisioned".format(device_type, str(device_ips))
        self.log(self.msg, "INFO")
        self.result['response'] = self.msg
        self.result['changed'] = False

    def handle_all_provisioned(self, device_type):
        """
        Handle successful provisioning for all devices(Wired/Wireless).
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_type (str): The type or category of the provisioned devices(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status, result, and logs the successful provisioning for all devices(Wired/Wireless).
        """

        self.status = "success"
        self.result['changed'] = True
        self.log("All {0} Devices provisioned successfully!!".format(device_type), "INFO")

    def handle_all_failed_provision(self, device_type):
        """
        Handle failure of provisioning for all devices(Wired/Wireless).
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - device_type (str): The type or category of the devices(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status and logs a failure message indicating that
            provisioning failed for all devices of a specific type.
        """

        self.status = "failed"
        self.msg = "{0} Device Provisioning failed for all devices".format(device_type)
        self.log(self.msg, "INFO")

    def handle_partially_provisioned(self, provision_count, device_type):
        """
        Handle partial success in provisioning for devices(Wired/Wireless).
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - provision_count (int): The count of devices that were successfully provisioned.
            - device_type (str): The type or category of the provisioned devices(Wired/Wireless).
        Return:
            None
        Description:
            This method updates the status, result, and logs a partial success message indicating that provisioning was successful
            for a certain number of devices(Wired/Wireless).
        """

        self.status = "success"
        self.result['changed'] = True
        self.log("{0} Devices provisioned successfully partially for {1} devices".format(device_type, provision_count), "INFO")

    def provisioned_wired_device(self):
        """
        Provision wired devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            self (object): An instance of the class with updated result, status, and log.
        Description:
            This function provisions wired devices in Cisco Catalyst Center based on the configuration provided.
            It retrieves the site name and IP addresses of the devices from the configuration,
            attempts to provision each device, and monitors the provisioning process.
        """

        site_name = self.config[0]['provision_wired_device']['site_name']
        device_in_dnac = self.device_exists_in_dnac()
        device_ips = self.get_device_ips_from_config_priority()
        input_device_ips = device_ips.copy()

        for device_ip in input_device_ips:
            if device_ip not in device_in_dnac:
                input_device_ips.remove(device_ip)

        device_type = "Wired"
        provision_count, already_provision_count = 0, 0

        if not site_name and not input_device_ips:
            self.status = "failed"
            self.msg = "Site/Devices are required for Provisioning of Wired Devices."
            self.log(self.msg, "ERROR")
            self.result['response'] = self.msg
            return self

        provision_wired_params = {
            'siteNameHierarchy': site_name
        }

        for device_ip in input_device_ips:
            try:
                provision_wired_params['deviceManagementIpAddress'] = device_ip
                count = 1
                managed_flag = True

                # Check till device comes into managed state
                while True:
                    response = self.get_device_response(device_ip)
                    self.log("Device is in {0} state waiting for Managed State.".format(response['managementState']), "DEBUG")

                    if (
                        response.get('managementState') == "Managed"
                        and response.get('collectionStatus') == "Managed"
                        and response.get("hostname")
                    ):
                        break
                    count = count + 1
                    if count > 400:
                        managed_flag = False
                        break

                if not managed_flag:
                    self.log("Device {0} is not transitioning to the managed state, so provisioning operation cannot be performed."
                             .format(device_ip), "WARNING")
                    continue

                response = self.dnac._exec(
                    family="sda",
                    function='provision_wired_device',
                    op_modifies=True,
                    params=provision_wired_params,
                )

                if response.get("status") == "failed":
                    description = response.get("description")
                    error_msg = "Cannot do Provisioning for device {0} beacuse of {1}".format(device_ip, description)
                    self.log(error_msg)
                    continue

                task_id = response.get("taskId")

                while True:
                    execution_details = self.get_task_details(task_id)
                    progress = execution_details.get("progress")
                    self.log(progress)

                    if 'TASK_PROVISION' in progress:
                        self.handle_successful_provisioning(device_ip, execution_details, device_type)
                        provision_count += 1
                        break
                    elif execution_details.get("isError"):
                        self.handle_failed_provisioning(device_ip, execution_details, device_type)
                        break

            except Exception as e:
                # Not returning from here as there might be possiblity that for some devices it comes into exception
                # but for others it gets provision successfully or If some devices are already provsioned
                self.handle_provisioning_exception(device_ip, e, device_type)
                if "already provisioned" in str(e):
                    self.log(str(e), "INFO")
                    already_provision_count += 1

        # Check If all the devices are already provsioned, return from here only
        if already_provision_count == len(device_ips):
            self.handle_all_already_provisioned(device_ips, device_type)
        elif provision_count == len(device_ips):
            self.handle_all_provisioned(device_type)
        elif provision_count == 0:
            self.handle_all_failed_provision(device_type)
        else:
            self.handle_partially_provisioned(provision_count, device_type)

        return self

    def get_wireless_param(self, device_ip):
        """
        Get wireless provisioning parameters for a device.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The IP address of the device for which to retrieve wireless provisioning parameters.
        Returns:
            wireless_param (list of dict): A list containing a dictionary with wireless provisioning parameters.
        Description:
            This function constructs a list containing a dictionary with wireless provisioning parameters based on the
            configuration provided in the playbook. It validates the managed AP locations, ensuring they are of type "floor."
            The function then queries Cisco Catalyst Center to get network device details using the provided device IP.
            If the device is not found, the function returns the class instance with appropriate status and log messages and
            returns the wireless provisioning parameters containing site information, managed AP
            locations, dynamic interfaces, and device name.
        """

        wireless_config = self.config[0]['provision_wireless_device'][0]
        wireless_param = [
            {
                'site': wireless_config['site_name'],
                'managedAPLocations': wireless_config['managed_ap_locations'],
            }
        ]

        for ap_loc in wireless_param[0]["managedAPLocations"]:
            if self.get_site_type(site_name=ap_loc) != "floor":
                self.status = "failed"
                self.msg = "Managed AP Location must be a floor"
                self.log(self.msg, "ERROR")
                return self

        wireless_param[0]["dynamicInterfaces"] = []

        for interface in wireless_config.get("dynamic_interfaces"):
            interface_dict = {
                "interfaceIPAddress": interface.get("interface_ip_address"),
                "interfaceNetmaskInCIDR": interface.get("interface_netmask_in_cidr"),
                "interfaceGateway": interface.get("interface_gateway"),
                "lagOrPortNumber": interface.get("lag_or_port_number"),
                "vlanId": interface.get("vlan_id"),
                "interfaceName": interface.get("interface_name")
            }
            wireless_param[0]["dynamicInterfaces"].append(interface_dict)

        response = self.dnac_apply['exec'](
            family="devices",
            function='get_network_device_by_ip',
            params={"ip_address": device_ip}
        )
        if not response:
            self.status = "failed"
            self.msg = "Device Host name is not present in the Cisco Catalyst Center"
            self.log(self.msg, "INFO")
            return self

        response = response.get("response")
        wireless_param[0]["deviceName"] = response.get("hostname")
        self.wireless_param = wireless_param
        self.status = "success"
        self.log("Successfully collected all parameters required for Wireless Provisioing", "DEBUG")

        return self

    def get_site_type(self, site_name):
        """
        Get the type of a site in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            site_name (str): The name of the site for which to retrieve the type.
        Returns:
            site_type (str or None): The type of the specified site, or None if the site is not found.
        Description:
            This function queries Cisco Catalyst Center to retrieve the type of a specified site. It uses the
            get_site API with the provided site name, extracts the site type from the response, and returns it.
            If the specified site is not found, the function returns None, and an appropriate log message is generated.
        """

        try:
            site_type = None
            response = self.dnac_apply['exec'](
                family="sites",
                function='get_site',
                params={"name": site_name},
            )

            if not response:
                self.msg = "Site '{0}' not found".format(site_name)
                self.log(self.msg, "INFO")
                return site_type

            self.log("Received API response from 'get_site': {0}".format(str(response)), "DEBUG")
            site = response.get("response")
            site_additional_info = site[0].get("additionalInfo")

            for item in site_additional_info:
                if item["nameSpace"] == "Location":
                    site_type = item.get("attributes").get("type")

        except Exception as e:
            self.msg = "Error while fetching the site '{0}'.".format(site_name)
            self.log(self.msg, "ERROR")
            self.module.fail_json(msg="Site not found", response=[])

        return site_type

    def provisioned_wireless_devices(self, device_ips):
        """
        Provision Wireless devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ips (list): List of IP addresses of the devices to be provisioned.
        Returns:
            self (object): An instance of the class with updated result, status, and log.
        Description:
            This function performs wireless provisioning for the provided list of device IP addresses.
            It iterates through each device, retrieves provisioning parameters using the get_wireless_param function,
            and then calls the Cisco Catalyst Center API for wireless provisioning. If all devices are already provisioned,
            it returns success with a relevant message.
        """

        provision_count, already_provision_count = 0, 0
        device_type = "Wireless"

        device_in_dnac = self.device_exists_in_dnac()
        device_ips = self.get_device_ips_from_config_priority()
        input_device_ips = device_ips.copy()

        for device_ip in input_device_ips:
            if device_ip not in device_in_dnac:
                input_device_ips.remove(device_ip)

        for device_ip in input_device_ips:
            try:
                # Collect the device parameters from the playbook to perform wireless provisioing
                self.get_wireless_param(device_ip).check_return_status()
                provisioning_params = self.wireless_param
                count = 1
                managed_flag = True

                # Check till device comes into managed state
                while True:
                    response = self.get_device_response(device_ip)
                    self.log("Device is in {0} state waiting for Managed State.".format(response['managementState']), "DEBUG")

                    if (
                        response.get('managementState') == "Managed"
                        and response.get('collectionStatus') == "Managed"
                        and response.get("hostname")
                    ):
                        break

                    count = count + 1
                    if count > 200:
                        managed_flag = False
                        break

                if not managed_flag:
                    self.log("Device {0} is not transitioning to the managed state, so provisioning operation cannot be performed."
                             .format(device_ip), 'WARNING')
                    continue

                # Now we have provisioning_param so we can do wireless provisioning
                response = self.dnac_apply['exec'](
                    family="wireless",
                    function="provision",
                    op_modifies=True,
                    params=provisioning_params,
                )

                if response.get("status") == "failed":
                    description = response.get("description")
                    error_msg = "Cannot do Provisioning for Wireless device {0} beacuse of {1}".format(device_ip, description)
                    self.log(error_msg, "ERROR")
                    continue

                task_id = response.get("taskId")

                while True:
                    execution_details = self.get_task_details(task_id)
                    progress = execution_details.get("progress")
                    self.log(progress)
                    if 'TASK_PROVISION' in progress:
                        self.handle_successful_provisioning(device_ip, execution_details, device_type)
                        provision_count += 1
                        break
                    elif execution_details.get("isError"):
                        self.handle_failed_provisioning(device_ip, execution_details, device_type)
                        break

            except Exception as e:
                # Not returning from here as there might be possiblity that for some devices it comes into exception
                # but for others it gets provision successfully or If some devices are already provsioned
                self.handle_provisioning_exception(device_ip, e, device_type)
                if "already provisioned" in str(e):
                    self.msg = "Device '{0}' already provisioned".format(device_ip)
                    self.log(self.msg, "INFO")
                    already_provision_count += 1

        # Check If all the devices are already provsioned, return from here only
        if already_provision_count == len(device_ips):
            self.handle_all_already_provisioned(device_ips, device_type)
        elif provision_count == len(device_ips):
            self.handle_all_provisioned(device_type)
        elif provision_count == 0:
            self.handle_all_failed_provision(device_type)
        else:
            self.handle_partially_provisioned(provision_count, device_type)

        return self

    def get_udf_id(self, field_name):
        """
        Get the ID of a Global User Defined Field in Cisco Catalyst Center based on its name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
            field_name (str): The name of the Global User Defined Field.
        Returns:
            str: The ID of the Global User Defined Field.
        Description:
            The function sends a request to Cisco Catalyst Center to retrieve all Global User Defined Fields
            with the specified name and extracts the ID of the first matching field.If successful, it returns
            the ID else returns None.
        """

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_all_user_defined_fields',
                params={"name": field_name},
            )
            self.log("Received API response from 'get_all_user_defined_fields': {0}".format(str(response)), "DEBUG")
            udf = response.get("response")
            udf_id = udf[0].get("id")

        except Exception as e:
            error_message = "Exception occurred while getting Global User Defined Fields(UDF) ID from Cisco Catalyst Center: {0}".format(str(e))
            self.log(error_message, "ERROR")

        return udf_id

    def mandatory_parameter(self):
        """
        Check for and validate mandatory parameters for adding network devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
        Returns:
            dict: The input `config` dictionary if all mandatory parameters are present.
        Description:
            It will check the mandatory parameters for adding the devices in Cisco Catalyst Center.
        """

        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        params_dict = {
            "NETWORK_DEVICE": ["enable_password", "ip_address", "password", "snmp_username", "username"],
            "COMPUTE_DEVICE": ["ip_address", "http_username", "http_password", "http_port", "snmp_username"],
            "MERAKI_DASHBOARD": ["http_password"],
            "FIREPOWER_MANAGEMENT_SYSTEM": ["ip_address", "http_username", "http_password"],
            "THIRD_PARTY_DEVICE": ["ip_address", "snmp_username", "snmp_auth_passphrase", "snmp_priv_passphrase"]
        }

        params_list = params_dict.get(device_type, [])

        mandatory_params_absent = []
        for param in params_list:
            if param not in self.config[0]:
                mandatory_params_absent.append(param)

        if mandatory_params_absent:
            self.status = "failed"
            self.msg = "Required parameters {0} for adding devices are not present".format(str(mandatory_params_absent))
            self.result['msg'] = self.msg
            self.log(self.msg, "ERROR")
        else:
            self.status = "success"
            self.msg = "Required parameter for Adding the devices in Inventory are present."
            self.log(self.msg, "INFO")

        return self

    def get_have(self, config):
        """
        Retrieve and check device information with Cisco Catalyst Center to determine if devices already exist.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Cisco Catalyst Center.
            config (dict): A dictionary containing the configuration details of devices to be checked.
        Returns:
            dict: A dictionary containing information about the devices in the playbook, devices that exist in
            Cisco Catalyst Center, and devices that are not present in Cisco Catalyst Center.
        Description:
            This function checks the specified devices in the playbook against the devices existing in Cisco Catalyst Center with following keys:
            - "want_device": A list of devices specified in the playbook.
            - "device_in_dnac": A list of devices that already exist in Cisco Catalyst Center.
            - "device_not_in_dnac": A list of devices that are not present in Cisco Catalyst Center.
        """

        have = {}
        want_device = self.get_device_ips_from_config_priority()

        # Get the list of device that are present in Cisco Catalyst Center
        device_in_dnac = self.device_exists_in_dnac()
        device_not_in_dnac = []

        for ip in want_device:
            if ip not in device_in_dnac:
                device_not_in_dnac.append(ip)

        self.log("Device(s) {0} exists in Cisco Catalyst Center".format(str(device_in_dnac)), "INFO")
        have["want_device"] = want_device
        have["device_in_dnac"] = device_in_dnac
        have["device_not_in_dnac"] = device_not_in_dnac

        self.have = have
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")

        return self

    def get_device_params(self, params):
        """
        Extract and store device parameters from the playbook for device processing in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            params (dict): A dictionary containing device parameters retrieved from the playbook.
        Returns:
            dict: A dictionary containing the extracted device parameters.
        Description:
            This function will extract and store parameters in dictionary for adding, updating, editing, or deleting devices Cisco Catalyst Center.
        """

        device_param = {
            "cliTransport": params.get("cli_transport"),
            "enablePassword": params.get("enable_password"),
            "password": params.get("password"),
            "ipAddress": params.get("ip_address"),
            "snmpAuthPassphrase": params.get("snmp_auth_passphrase"),
            "snmpAuthProtocol": params.get("snmp_auth_protocol"),
            "snmpMode": params.get("snmp_mode"),
            "snmpPrivPassphrase": params.get("snmp_priv_passphrase"),
            "snmpPrivProtocol": params.get("snmp_priv_protocol"),
            "snmpROCommunity": params.get("snmp_ro_community"),
            "snmpRWCommunity": params.get("snmp_rw_community"),
            "snmpRetry": params.get("snmp_retry"),
            "snmpTimeout": params.get("snmp_timeout"),
            "snmpUserName": params.get("snmp_username"),
            "userName": params.get("username"),
            "computeDevice": params.get("compute_device"),
            "extendedDiscoveryInfo": params.get("extended_discovery_info"),
            "httpPassword": params.get("http_password"),
            "httpPort": params.get("http_port"),
            "httpSecure": params.get("http_secure"),
            "httpUserName": params.get("http_username"),
            "netconfPort": params.get("netconf_port"),
            "serialNumber": params.get("serial_number"),
            "snmpVersion": params.get("snmp_version"),
            "type": params.get("type"),
            "updateMgmtIPaddressList": params.get("update_mgmt_ipaddresslist"),
            "forceSync": params.get("force_sync"),
            "cleanConfig": params.get("clean_config")
        }

        if device_param.get("updateMgmtIPaddressList"):
            device_mngmt_dict = device_param.get("updateMgmtIPaddressList")[0]
            device_param["updateMgmtIPaddressList"][0] = {}

            device_param["updateMgmtIPaddressList"][0].update(
                {
                    "existMgmtIpAddress": device_mngmt_dict.get("exist_mgmt_ipaddress"),
                    "newMgmtIpAddress": device_mngmt_dict.get("new_mgmt_ipaddress")
                })

        return device_param

    def get_device_ids(self, device_ips):
        """
        Get the list of unique device IDs for list of specified management IP addresses of devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ips (list): The management IP addresses of devices for which you want to retrieve the device IDs.
        Returns:
            list: The list of unique device IDs for the specified devices.
        Description:
            Queries Cisco Catalyst Center to retrieve the unique device ID associated with a device having the specified
            IP address. If the device is not found in Cisco Catalyst Center, then print the log message with error severity.
        """

        device_ids = []

        for device_ip in device_ips:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"managementIpAddress": device_ip}
                )

                if response:
                    self.log("Received API response from 'get_device_list': {0}".format(str(response)), "DEBUG")
                    response = response.get("response")
                    if not response:
                        continue
                    device_id = response[0]["id"]
                    device_ids.append(device_id)

            except Exception as e:
                error_message = "Error while fetching device '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e))
                self.log(error_message, "ERROR")

        return device_ids

    def get_device_ips_from_hostname(self, hostname_list):
        """
        Get the list of unique device IPs for list of specified hostnames of devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            hostname_list (list): The hostnames of devices for which you want to retrieve the device IPs.
        Returns:
            list: The list of unique device IPs for the specified devices hostname list.
        Description:
            Queries Cisco Catalyst Center to retrieve the unique device IP's associated with a device having the specified
            list of hostnames. If a device is not found in Cisco Catalyst Center, an error log message is printed.
        """

        device_ips = []
        for hostname in hostname_list:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"hostname": hostname}
                )
                if response:
                    self.log("Received API response from 'get_device_list': {0}".format(str(response)), "DEBUG")
                    response = response.get("response")
                    if response:
                        device_ip = response[0]["managementIpAddress"]
                        if device_ip:
                            device_ips.append(device_ip)
            except Exception as e:
                error_message = "Exception occurred while fetching device from Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "ERROR")

        return device_ips

    def get_device_ips_from_serial_number(self, serial_number_list):
        """
        Get the list of unique device IPs for a specified list of serial numbers in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            serial_number_list (list): The list of serial number of devices for which you want to retrieve the device IPs.
        Returns:
            list: The list of unique device IPs for the specified devices with serial numbers.
        Description:
            Queries Cisco Catalyst Center to retrieve the unique device IPs associated with a device having the specified
            serial numbers.If a device is not found in Cisco Catalyst Center, an error log message is printed.
        """

        device_ips = []
        for serial_number in serial_number_list:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"serialNumber": serial_number}
                )
                if response:
                    self.log("Received API response from 'get_device_list': {0}".format(str(response)), "DEBUG")
                    response = response.get("response")
                    if response:
                        device_ip = response[0]["managementIpAddress"]
                        if device_ip:
                            device_ips.append(device_ip)
            except Exception as e:
                error_message = "Exception occurred while fetching device from Cisco Catalyst Center - {0}".format(str(e))
                self.log(error_message, "ERROR")

        return device_ips

    def get_device_ips_from_mac_address(self, mac_address_list):
        """
        Get the list of unique device IPs for list of specified mac address of devices in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            mac_address_list (list): The list of mac address of devices for which you want to retrieve the device IPs.
        Returns:
            list: The list of unique device IPs for the specified devices.
        Description:
            Queries Cisco Catalyst Center to retrieve the unique device IPs associated with a device having the specified
            mac addresses. If a device is not found in Cisco Catalyst Center, an error log message is printed.
        """

        device_ips = []
        for mac_address in mac_address_list:
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_device_list',
                    params={"macAddress": mac_address}
                )
                if response:
                    self.log("Received API response from 'get_device_list': {0}".format(str(response)), "DEBUG")
                    response = response.get("response")
                    if response:
                        device_ip = response[0]["managementIpAddress"]
                        if device_ip:
                            device_ips.append(device_ip)
            except Exception as e:
                error_message = "Exception occurred while fetching device from Cisco Catalyst Center - {0}".format(str(e))
                self.log(error_message, "ERROR")

        return device_ips

    def get_interface_from_id_and_name(self, device_id, interface_name):
        """
        Retrieve the interface ID for a device in Cisco Catalyst Center based on device id and interface name.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_id (str): The id of the device.
            interface_name (str): Name of the interface for which details need to be collected.
        Returns:
            str: The interface ID for the specified device and interface name.
        Description:
            The function sends a request to Cisco Catalyst Center to retrieve the interface information
            for the device with the provided device id and interface name and extracts the interface ID from the
            response, and returns the interface ID.
        """

        try:
            interface_detail_params = {
                'device_id': device_id,
                'name': interface_name
            }
            response = self.dnac._exec(
                family="devices",
                function='get_interface_details',
                params=interface_detail_params
            )
            self.log("Received API response from 'get_interface_details': {0}".format(str(response)), "DEBUG")
            response = response.get("response")

            if response:
                self.status = "success"
                interface_id = response["id"]
                self.log("""Successfully fetched interface ID ({0}) by using device id {1} and interface name {2}."""
                         .format(interface_id, device_id, interface_name), "INFO")
                return interface_id

        except Exception as e:
            error_message = "Error while fetching interface id for interface({0}) from Cisco Catalyst Center: {1}".format(interface_name, str(e))
            self.log(error_message, "ERROR")
            self.msg = error_message
            self.status = "failed"
            return self

        def get_interface_from_ip(self, device_ip):
            """
            Get the interface ID for a device in Cisco Catalyst Center based on its IP address.
            Parameters:
                self (object): An instance of a class used for interacting with Cisco Catalyst Center.
                device_ip (str): The IP address of the device.
            Returns:
                str: The interface ID for the specified device.
            Description:
                The function sends a request to Cisco Catalyst Center to retrieve the interface information
                for the device with the provided IP address and extracts the interface ID from the
                response, and returns the interface ID.
            """

            try:
                response = self.dnac._exec(
                    family="devices",
                    function='get_interface_by_ip',
                    params={"ip_address": device_ip}
                )
                self.log("Received API response from 'get_interface_by_ip': {0}".format(str(response)), "DEBUG")
                response = response.get("response")

                if response:
                    interface_id = response[0]["id"]
                    self.log("Fetch Interface Id for device '{0}' successfully !!".format(device_ip))
                    return interface_id

            except Exception as e:
                error_message = "Error while fetching Interface Id for device '{0}' from Cisco Catalyst Center: {1}".format(device_ip, str(e))
                self.log(error_message, "ERROR")
                raise Exception(error_message)

    def get_device_response(self, device_ip):
        """
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The management IP address of the device for which the response is to be retrieved.
        Returns:
            dict: A dictionary containing details of the device obtained from the Cisco Catalyst Center.
        Description:
            This method communicates with Cisco Catalyst Center to retrieve the details of a device with the specified
            management IP address. It executes the 'get_device_list' API call with the provided device IP address,
            logs the response, and returns a dictionary containing information about the device.
        """

        try:
            response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                params={"managementIpAddress": device_ip}
            )
            response = response.get('response')[0]

        except Exception as e:
            error_message = "Error while getting the response of device from Cisco Catalyst Center: {0}".format(str(e))
            self.log(error_message, "ERROR")
            raise Exception(error_message)

        return response

    def check_device_role(self, device_ip):
        """
        Checks if the device role and role source for a device in Cisco Catalyst Center match the specified values in the configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The management IP address of the device for which the device role is to be checked.
        Returns:
            bool: True if the device role and role source match the specified values, False otherwise.
        Description:
            This method retrieves the device role and role source for a device in Cisco Catalyst Center using the
            'get_device_response' method and compares the retrieved values with specified values in the configuration
            for updating device roles.
        """

        device_role_args = self.config[0].get('update_device_role')
        role = device_role_args.get('role')
        role_source = device_role_args.get('role_source')
        response = self.get_device_response(device_ip)

        return response.get('role') == role and response.get('roleSource') == role_source

    def check_interface_details(self, device_ip, interface_name):
        """
        Checks if the interface details for a device in Cisco Catalyst Center match the specified values in the configuration.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The management IP address of the device for which interface details are to be checked.
        Returns:
            bool: True if the interface details match the specified values, False otherwise.
        Description:
            This method retrieves the interface details for a device in Cisco Catalyst Center using the 'get_interface_by_ip' API call.
            It then compares the retrieved details with the specified values in the configuration for updating interface details.
            If all specified parameters match the retrieved values or are not provided in the playbook parameters, the function
            returns True, indicating successful validation.
        """
        device_id = self.get_device_ids([device_ip])

        if not device_id:
            self.log("""Error: Device with IP '{0}' not found in Cisco Catalyst Center.Unable to update interface details."""
                     .format(device_ip), "ERROR")
            return False

        interface_detail_params = {
            'device_id': device_id[0],
            'name': interface_name
        }
        response = self.dnac._exec(
            family="devices",
            function='get_interface_details',
            params=interface_detail_params
        )
        self.log("Received API response from 'get_interface_details': {0}".format(str(response)), "DEBUG")
        response = response.get("response")

        if not response:
            self.log("No response received from the API 'get_interface_details'.", "DEBUG")
            return False

        response_params = {
            'description': response.get('description'),
            'adminStatus': response.get('adminStatus'),
            'voiceVlanId': response.get('voiceVlan'),
            'vlanId': int(response.get('vlanId'))
        }

        interface_playbook_params = self.config[0].get('update_interface_details')
        playbook_params = {
            'description': interface_playbook_params.get('description', ''),
            'adminStatus': interface_playbook_params.get('admin_status'),
            'voiceVlanId': interface_playbook_params.get('voice_vlan_id', ''),
            'vlanId': interface_playbook_params.get('vlan_id')
        }

        for key, value in playbook_params.items():
            if not value:
                continue
            elif response_params[key] != value:
                return False

        return True

    def check_credential_update(self):
        """
        Checks if the credentials for devices in the configuration match the updated values in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Returns:
            bool: True if the credentials match the updated values, False otherwise.
        Description:
            This method triggers the export API in Cisco Catalyst Center to obtain the updated credential details for
            the specified devices. It then decrypts and reads the CSV file containing the updated credentials,
            comparing them with the credentials specified in the configuration.
        """

        device_ips = self.get_device_ips_from_config_priority()
        device_uuids = self.get_device_ids(device_ips)
        password = "Testing@123"
        payload_params = {"deviceUuids": device_uuids, "password": password, "operationEnum": "0"}
        response = self.trigger_export_api(payload_params)
        self.check_return_status()
        csv_reader = self.decrypt_and_read_csv(response, password)
        self.check_return_status()
        device_data = next(csv_reader, None)

        if not device_data:
            return False

        csv_data_dict = {
            'snmp_retry': device_data['snmp_retries'],
            'username': device_data['cli_username'],
            'password': device_data['cli_password'],
            'enable_password': device_data['cli_enable_password'],
            'snmp_username': device_data['snmpv3_user_name'],
            'snmp_auth_protocol': device_data['snmpv3_auth_type'],
        }

        config = self.config[0]
        for key in csv_data_dict:
            if key in config and csv_data_dict[key] is not None:
                if key == "snmp_retry" and int(csv_data_dict[key]) != int(config[key]):
                    return False
                elif csv_data_dict[key] != config[key]:
                    return False

        return True

    def get_provision_wired_device(self, device_ip):
        """
        Retrieves the provisioning status of a wired device with the specified management IP address in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_ip (str): The management IP address of the wired device for which provisioning status is to be retrieved.
        Returns:
            bool: True if the device is provisioned successfully, False otherwise.
        Description:
            This method communicates with Cisco Catalyst Center to check the provisioning status of a wired device.
            It executes the 'get_provisioned_wired_device' API call with the provided device IP address and
            logs the response.
        """

        response = self.dnac._exec(
            family="sda",
            function='get_provisioned_wired_device',
            op_modifies=True,
            params={"device_management_ip_address": device_ip}
        )

        if response.get("status") == "failed":
            self.log("Cannot do provisioning for wired device {0} because of {1}.".format(device_ip, response.get('description')), "ERROR")
            return False

        return True

    def update_interface_detail_of_device(self, device_to_update):
        """
        Update interface details for a device in Cisco Catalyst Center.
        Args:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            device_to_update (list): A list of IP addresses of devices to be updated.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method updates interface details for devices in Cisco Catalyst Center.
            It iterates over the list of devices to be updated, retrieves interface parameters from the configuration,
            calls the update interface details API with the required parameters, and checks the execution response.
            If the update is successful, it sets the status to 'success' and logs an informational message.
        """

        # Call the Get interface details by device IP API and fetch the interface Id
        for device_ip in device_to_update:
            interface_params = self.config[0].get('update_interface_details')
            interface_name = interface_params.get('interface_name')
            device_id = self.get_device_ids([device_ip])
            interface_id = self.get_interface_from_id_and_name(device_id[0], interface_name)
            self.check_return_status()

            # Now we call update interface details api with required parameter
            try:
                interface_params = self.config[0].get('update_interface_details')
                temp_params = {
                    'description': interface_params.get('description', ''),
                    'adminStatus': interface_params.get('admin_status'),
                    'voiceVlanId': interface_params.get('voice_vlan_id'),
                    'vlanId': interface_params.get('vlan_id')
                }
                payload_params = {}
                for key, value in temp_params.items():
                    if value is not None:
                        payload_params[key] = value

                update_interface_params = {
                    'payload': payload_params,
                    'interface_uuid': interface_id,
                    'deployment_mode': interface_params.get('deployment_mode', 'Deploy')
                }
                response = self.dnac._exec(
                    family="devices",
                    function='update_interface_details',
                    op_modifies=True,
                    params=update_interface_params,
                )
                self.log("Received API response from 'update_interface_details': {0}".format(str(response)), "DEBUG")

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'SUCCESS' in execution_details.get("progress"):
                            self.status = "success"
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            self.msg = "Updated Interface Details for device '{0}' successfully".format(device_ip)
                            self.log(self.msg, "INFO")
                            break
                        elif execution_details.get("isError"):
                            self.status = "failed"
                            failure_reason = execution_details.get("failureReason")
                            if failure_reason:
                                self.msg = "Interface Updation get failed because of {0}".format(failure_reason)
                            else:
                                self.msg = "Interface Updation get failed"
                            self.log(self.msg, "ERROR")
                            break

            except Exception as e:
                error_message = "Error while updating interface details in Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "INFO")
                self.status = "success"
                self.result['changed'] = False
                self.msg = "Port actions are only supported on user facing/access ports as it's not allowed or No Updation required"
                self.log(self.msg, "INFO")

        return self

    def check_managementip_execution_response(self, response, device_ip, new_mgmt_ipaddress):
        """
        Check the execution response of a management IP update task.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            response (dict): The response received after initiating the management IP update task.
            device_ip (str): The IP address of the device for which the management IP was updated.
            new_mgmt_ipaddress (str): The new management IP address of the device.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the execution response of a management IP update task in Cisco Catalyst Center.
            It continuously queries the task details until the task is completed or an error occurs.
            If the task is successful, it sets the status to 'success' and logs an informational message.
            If the task fails, it sets the status to 'failed' and logs an error message with the failure reason, if available.
        """

        task_id = response.get('response').get('taskId')

        while True:
            execution_details = self.get_task_details(task_id)
            if execution_details.get("isError"):
                self.status = "failed"
                failure_reason = execution_details.get("failureReason")
                if failure_reason:
                    self.msg = "Device new management IP updation for device '{0}' get failed due to {1}".format(device_ip, failure_reason)
                else:
                    self.msg = "Device new management IP updation for device '{0}' get failed".format(device_ip)
                self.log(self.msg, "ERROR")
                break
            elif execution_details.get("endTime"):
                self.status = "success"
                self.result['changed'] = True
                self.result['response'] = execution_details
                self.msg = """Device '{0}' present in Cisco Catalyst Center and new management ip '{1}' have been
                            updated successfully""".format(device_ip, new_mgmt_ipaddress)
                self.log(self.msg, "INFO")
                break

        return self

    def check_device_update_execution_response(self, response, device_ip):
        """
        Check the execution response of a device update task.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            response (dict): The response received after initiating the device update task.
            device_ip (str): The IP address of the device for which the update is performed.
        Returns:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the execution response of a device update task in Cisco Catalyst Center.
            It continuously queries the task details until the task is completed or an error occurs.
            If the task is successful, it sets the status to 'success' and logs an informational message.
            If the task fails, it sets the status to 'failed' and logs an error message with the failure reason, if available.
        """

        task_id = response.get('response').get('taskId')

        while True:
            execution_details = self.get_task_details(task_id)

            if execution_details.get("isError"):
                self.status = "failed"
                failure_reason = execution_details.get("failureReason")
                if failure_reason:
                    self.msg = "Device Updation for device '{0}' get failed due to {1}".format(device_ip, failure_reason)
                else:
                    self.msg = "Device Updation for device '{0}' get failed".format(device_ip)
                self.log(self.msg, "ERROR")
                break
            elif execution_details.get("endTime"):
                self.status = "success"
                self.result['changed'] = True
                self.result['response'] = execution_details
                self.msg = "Device '{0}' present in Cisco Catalyst Center and have been updated successfully".format(device_ip)
                self.log(self.msg, "INFO")
                break

        return self

    def get_want(self, config):
        """
        Get all the device related information from playbook that is needed to be
        add/update/delete/resync device in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing device-related information from the playbook.
        Returns:
            dict: A dictionary containing the extracted device parameters and other relevant information.
        Description:
            Retrieve all the device-related information from the playbook needed for adding, updating, deleting,
            or resyncing devices in Cisco Catalyst Center.
        """

        want = {}
        device_params = self.get_device_params(config)
        want["device_params"] = device_params

        self.want = want
        self.msg = "Successfully collected all parameters from the playbook "
        self.status = "success"
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        return self

    def get_diff_merged(self, config):
        """
        Merge and process differences between existing devices and desired device configuration in Cisco Catalyst Center.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            config (dict): A dictionary containing the desired device configuration and relevant information from the playbook.
        Returns:
            object: An instance of the class with updated results and status based on the processing of differences.
        Description:
            The function processes the differences and, depending on the changes required, it may add, update,
            or resynchronize devices in Cisco Catalyst Center.
            The updated results and status are stored in the class instance for further use.
        """

        devices_to_add = self.have["device_not_in_dnac"]
        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        device_resynced = self.config[0].get("device_resync", False)
        device_added = self.config[0].get("device_added", False)
        device_updated = self.config[0].get("device_updated", False)
        device_reboot = self.config[0].get("reboot_device", False)
        credential_update = self.config[0].get("credential_update", False)

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')

            if field_name is None:
                self.status = "failed"
                self.msg = "Error: The mandatory parameter 'name' for the User Defined Field is missing. Please provide the required information."
                self.log(self.msg, "ERROR")
                return self

            # Check if the Global User defined field exist if not then create it with given field name
            udf_exist = self.is_udf_exist(field_name)

            if not udf_exist:
                # Create the Global UDF
                self.create_user_defined_field().check_return_status()

            # Get device Id based on config priority
            device_ips = self.get_device_ips_from_config_priority()
            device_ids = self.get_device_ids(device_ips)

            if len(device_ids) == 0:
                self.status = "failed"
                self.msg = "Can't Assign Global User Defined Field to device as device's are not present in Cisco Catalyst Center"
                self.log(self.msg, "INFO")
                self.result['changed'] = False
                return self

            # Now add code for adding Global UDF to device with Id
            self.add_field_to_devices(device_ids).check_return_status()

            self.result['changed'] = True
            self.msg = "Global User Defined Field(UDF) named '{0}' has been successfully added to the device.".format(field_name)
            self.log(self.msg, "INFO")

        config['type'] = device_type
        if device_type == "FIREPOWER_MANAGEMENT_SYSTEM":
            config['http_port'] = self.config[0].get("http_port", "443")

        if device_updated:
            device_to_update = self.get_device_ips_from_config_priority()
            # First check if device present in Cisco Catalyst Center or not
            device_present = False
            for device in device_to_update:
                if device in self.have.get("device_in_dnac"):
                    device_present = True
                    break

            if not device_present:
                self.msg = "Cannot perform Update operation as device: {0} not present in Cisco Catalyst Center".format(str(device_to_update))
                self.status = "success"
                self.result['changed'] = False
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self

            if credential_update:
                # Update Device details and credentails
                device_uuids = self.get_device_ids(device_to_update)
                password = "Testing@123"
                export_payload = {"deviceUuids": device_uuids, "password": password, "operationEnum": "0"}
                export_response = self.trigger_export_api(export_payload)
                self.check_return_status()
                csv_reader = self.decrypt_and_read_csv(export_response, password)
                self.check_return_status()
                device_details = {}

                for row in csv_reader:
                    ip_address = row['ip_address']
                    device_details[ip_address] = row

                for device_ip in device_to_update:
                    playbook_params = self.want.get("device_params").copy()
                    playbook_params['ipAddress'] = [device_ip]
                    device_data = device_details[device_ip]

                    if not playbook_params['cliTransport']:
                        if device_data['protocol'] == "ssh2":
                            playbook_params['cliTransport'] = "ssh"
                        else:
                            playbook_params['cliTransport'] = device_data['protocol']
                    if not playbook_params['snmpPrivProtocol']:
                        playbook_params['snmpPrivProtocol'] = device_data['snmpv3_privacy_type']

                    csv_data_dict = {
                        'username': device_data['cli_username'],
                        'password': device_data['cli_password'],
                        'enable_password': device_data['cli_enable_password'],
                        'netconf_port': device_data['netconf_port'],
                    }

                    if device_data['snmp_version'] == '3':
                        csv_data_dict['snmp_username'] = device_data['snmpv3_user_name']
                        if device_data['snmpv3_privacy_password']:
                            csv_data_dict['snmp_auth_passphrase'] = device_data['snmpv3_auth_password']
                            csv_data_dict['snmp_priv_passphrase'] = device_data['snmpv3_privacy_password']

                    device_key_mapping = {
                        'username': 'userName',
                        'password': 'password',
                        'enable_password': 'enablePassword',
                        'snmp_username': 'snmpUserName',
                        'netconf_port': 'netconfPort'
                    }
                    device_update_key_list = ["username", "password", "enable_password", "snmp_username", "netconf_port"]

                    for key in device_update_key_list:
                        mapped_key = device_key_mapping[key]

                        if playbook_params[mapped_key] is None:
                            if playbook_params['snmpMode'] == "AUTHPRIV":
                                playbook_params['snmpAuthPassphrase'] = csv_data_dict['snmp_auth_passphrase']
                                playbook_params['snmpPrivPassphrase'] = csv_data_dict['snmp_priv_passphrase']
                            playbook_params[mapped_key] = csv_data_dict[key]

                    if playbook_params['snmpMode'] == "NOAUTHNOPRIV":
                        playbook_params.pop('snmpAuthPassphrase', None)
                        playbook_params.pop('snmpPrivPassphrase', None)
                        playbook_params.pop('snmpPrivProtocol', None)
                        playbook_params.pop('snmpAuthProtocol', None)
                    elif playbook_params['snmpMode'] == "AUTHNOPRIV":
                        playbook_params.pop('snmpPrivPassphrase', None)
                        playbook_params.pop('snmpPrivProtocol', None)

                    if playbook_params['netconfPort'] == " ":
                        playbook_params['netconfPort'] = None

                    try:
                        if playbook_params['updateMgmtIPaddressList']:
                            new_mgmt_ipaddress = playbook_params['updateMgmtIPaddressList'][0]['newMgmtIpAddress']
                            if new_mgmt_ipaddress in self.have['device_in_dnac']:
                                self.status = "failed"
                                self.msg = "Device with IP address '{0}' already exists in inventory".format(new_mgmt_ipaddress)
                                self.log(self.msg, "ERROR")
                                self.result['response'] = self.msg
                            else:
                                self.log("Playbook parameter for updating device new management ip address: {0}".format(str(playbook_params)), "DEBUG")
                                response = self.dnac._exec(
                                    family="devices",
                                    function='sync_devices',
                                    op_modifies=True,
                                    params=playbook_params,
                                )
                                self.log("Received API response from 'sync_devices': {0}".format(str(response)), "DEBUG")

                                if response and isinstance(response, dict):
                                    self.check_managementip_execution_response(response, device_ip, new_mgmt_ipaddress)
                                    self.check_return_status()

                        else:
                            self.log("Playbook parameter for updating devices: {0}".format(str(playbook_params)), "DEBUG")
                            response = self.dnac._exec(
                                family="devices",
                                function='sync_devices',
                                op_modifies=True,
                                params=playbook_params,
                            )
                            self.log("Received API response from 'sync_devices': {0}".format(str(response)), "DEBUG")

                            if response and isinstance(response, dict):
                                self.check_device_update_execution_response(response, device_ip)
                                self.check_return_status()

                    except Exception as e:
                        error_message = "Error while updating device in Cisco Catalyst Center: {0}".format(str(e))
                        self.log(error_message, "ERROR")
                        raise Exception(error_message)

            if self.config[0].get('update_interface_details'):
                self.update_interface_detail_of_device(device_to_update).check_return_status()

            if self.config[0].get('update_device_role'):
                for device_ip in device_to_update:
                    device_id = self.get_device_ids([device_ip])
                    device_role_args = self.config[0].get('update_device_role')

                    if 'role' not in device_role_args or 'role_source' not in device_role_args:
                        self.status = "failed"
                        self.msg = "Mandatory paramter(role/sourceRole) to update Device Role are missing"
                        self.log(self.msg, "WARNING")
                        return self

                    # Check if the same role of device is present in dnac then no need to change the state
                    response = self.dnac._exec(
                        family="devices",
                        function='get_device_list',
                        params={"managementIpAddress": device_ip}
                    )
                    response = response.get('response')[0]

                    if response.get('role') == device_role_args.get('role'):
                        self.status = "success"
                        self.result['changed'] = False
                        log_msg = "The device role '{0}' is already set in Cisco Catalyst Center, no update is needed.".format(device_role_args.get('role'))
                        self.log(log_msg, "INFO")
                        continue

                    device_role_params = {
                        'role': device_role_args.get('role'),
                        'roleSource': device_role_args.get('role_source'),
                        'id': device_id[0]
                    }

                    try:
                        response = self.dnac._exec(
                            family="devices",
                            function='update_device_role',
                            op_modifies=True,
                            params=device_role_params,
                        )
                        self.log("Received API response from 'update_device_role': {0}".format(str(response)), "DEBUG")

                        if response and isinstance(response, dict):
                            task_id = response.get('response').get('taskId')

                            while True:
                                execution_details = self.get_task_details(task_id)

                                if 'successfully' in execution_details.get("progress"):
                                    self.status = "success"
                                    self.result['changed'] = True
                                    self.result['response'] = execution_details
                                    self.msg = "Device(s) '{0}' role updated successfully".format(str(device_to_update))
                                    self.log(self.msg, "INFO")
                                    break
                                elif execution_details.get("isError"):
                                    self.status = "failed"
                                    failure_reason = execution_details.get("failureReason")
                                    if failure_reason:
                                        self.msg = "Device role updation get failed because of {0}".format(failure_reason)
                                    else:
                                        self.msg = "Device role updation get failed"
                                    self.log(self.msg, "ERROR")
                                    break

                    except Exception as e:
                        error_message = "Error while updating device role in Cisco Catalyst Center: {0}".format(str(e))
                        self.log(error_message, "ERROR")
                        raise Exception(error_message)

        # If we want to add device in inventory
        if device_added:
            config['ip_address'] = devices_to_add
            device_params = self.want.get("device_params")

            if not device_params['cliTransport']:
                device_params['cliTransport'] = "ssh"

            if not device_params['snmpPrivProtocol']:
                device_params['snmpPrivProtocol'] = "AES128"

            if device_params['snmpMode'] == "NOAUTHNOPRIV":
                device_params.pop('snmpAuthPassphrase', None)
                device_params.pop('snmpPrivPassphrase', None)
                device_params.pop('snmpPrivProtocol', None)
                device_params.pop('snmpAuthProtocol', None)
            elif device_params['snmpMode'] == "AUTHNOPRIV":
                device_params.pop('snmpPrivPassphrase', None)
                device_params.pop('snmpPrivProtocol', None)

            self.mandatory_parameter().check_return_status()
            try:
                response = self.dnac._exec(
                    family="devices",
                    function='add_device',
                    op_modifies=True,
                    params=device_params,
                )
                self.log("Received API response from 'add_device': {0}".format(str(response)), "DEBUG")

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if '/task/' in execution_details.get("progress"):
                            self.status = "success"
                            self.result['response'] = execution_details

                            if len(devices_to_add) > 0:
                                self.result['changed'] = True
                                self.msg = "Device(s) '{0}' added to Cisco Catalyst Center".format(str(devices_to_add))
                                self.log(self.msg, "INFO")
                                self.result['msg'] = self.msg
                                break
                            self.msg = "Device(s) '{0}' already present in Cisco Catalyst Center".format(str(self.config[0].get("ip_address")))
                            self.log(self.msg, "INFO")
                            self.result['msg'] = self.msg
                            break
                        elif execution_details.get("isError"):
                            self.status = "failed"
                            failure_reason = execution_details.get("failureReason")
                            if failure_reason:
                                self.msg = "Device addition get failed because of {0}".format(failure_reason)
                            else:
                                self.msg = "Device addition get failed"
                            self.log(self.msg, "ERROR")
                            self.result['msg'] = self.msg
                            break

            except Exception as e:
                error_message = "Error while adding device in Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "ERROR")
                raise Exception(error_message)

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')

            if field_name is None:
                self.status = "failed"
                self.msg = "Mandatory paramter for User Define Field 'name' is missing"
                self.log(self.msg, "ERROR")
                self.result['response'] = self.msg
                return self

            # Check if the Global User defined field exist if not then create it with given field name
            udf_exist = self.is_udf_exist(field_name)

            if not udf_exist:
                # Create the Global UDF
                self.create_user_defined_field().check_return_status()

            # Get device Id based on config priority
            device_ips = self.get_device_ips_from_config_priority()
            device_ids = self.get_device_ids(device_ips)

            if not device_ids:
                self.status = "failed"
                self.msg = "Can't Assign Global User Defined Field to device as device's are not present in Cisco Catalyst Center"
                self.result['changed'] = False
                self.result['response'] = self.msg
                self.log(self.msg, "INFO")
                return self

            # Now add code for adding Global UDF to device with Id
            self.add_field_to_devices(device_ids).check_return_status()

            self.result['changed'] = True
            self.msg = "Global User Defined Added with name {0} added to device Successfully !".format(field_name)
            self.log(self.msg, "INFO")

        # Once Wired device get added we will assign device to site and Provisioned it
        if self.config[0].get('provision_wired_device'):
            self.provisioned_wired_device().check_return_status()

        # Once Wireless device get added we will assign device to site and Provisioned it
        if self.config[0].get('provision_wireless_device'):
            device_ips = self.get_device_ips_from_config_priority()
            self.provisioned_wireless_devices(device_ips).check_return_status()

        if device_resynced:
            self.resync_devices().check_return_status()

        if device_reboot:
            self.reboot_access_points().check_return_status()

        if self.config[0].get('export_device_list'):
            self.export_device_details().check_return_status()

        return self

    def get_diff_deleted(self, config):
        """
        Delete devices in Cisco Catalyst Center based on device IP Address.
        Parameters:
            self (object): An instance of a class used for interacting with Cisco Catalyst Center
            config (dict): A dictionary containing the list of device IP addresses to be deleted.
        Returns:
            object: An instance of the class with updated results and status based on the deletion operation.
        Description:
            This function is responsible for removing devices from the Cisco Catalyst Center inventory and
            also unprovsioned and removed wired provsion devices from the Inventory page and also delete
            the Global User Defined Field that are associated to the devices.
        """

        device_to_delete = self.get_device_ips_from_config_priority()
        self.result['msg'] = []

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')
            udf_id = self.get_udf_id(field_name)

            if udf_id is None:
                self.status = "success"
                self.msg = "Global UDF '{0}' is not present in Cisco Catalyst Center".format(field_name)
                self.log(self.msg, "INFO")
                self.result['changed'] = False
                self.result['msg'] = self.msg
                return self

            try:
                response = self.dnac._exec(
                    family="devices",
                    function='delete_user_defined_field',
                    params={"id": udf_id},
                )
                if response and isinstance(response, dict):
                    self.log("Received API response from 'delete_user_defined_field': {0}".format(str(response)), "DEBUG")
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'success' in execution_details.get("progress"):
                            self.status = "success"
                            self.msg = "Global UDF '{0}' deleted successfully from Cisco Catalyst Center".format(field_name)
                            self.log(self.msg, "INFO")
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError"):
                            self.status = "failed"
                            failure_reason = execution_details.get("failureReason")
                            if failure_reason:
                                self.msg = "Failed to delete Global User Defined Field(UDF) due to: {0}".format(failure_reason)
                            else:
                                self.msg = "Global UDF deletion get failed."
                            self.log(self.msg, "ERROR")
                            break

            except Exception as e:
                error_message = "Error while deleting Global UDF from Cisco Catalyst Center: {0}".format(str(e))
                self.log(error_message, "ERROR")
                raise Exception(error_message)

            return self

        for device_ip in device_to_delete:
            if device_ip not in self.have.get("device_in_dnac"):
                self.status = "success"
                self.result['changed'] = False
                self.msg = "Device '{0}' is not present in Cisco Catalyst Center so can't perform delete operation".format(device_ip)
                self.result['msg'] = self.msg
                self.log(self.msg, "INFO")
                continue

            try:
                provision_params = {
                    "device_management_ip_address": device_ip
                }
                prov_respone = self.dnac._exec(
                    family="sda",
                    function='get_provisioned_wired_device',
                    params=provision_params,
                )

                if prov_respone.get("status") == "success":
                    response = self.dnac._exec(
                        family="sda",
                        function='delete_provisioned_wired_device',
                        params=provision_params,
                    )
                    executionid = response.get("executionId")

                    while True:
                        execution_details = self.get_execution_details(executionid)
                        if execution_details.get("status") == "SUCCESS":
                            self.result['changed'] = True
                            self.msg = execution_details.get("bapiName")
                            self.log(self.msg, "INFO")
                            self.result['response'] = self.msg
                            break
                        elif execution_details.get("bapiError"):
                            self.msg = execution_details.get("bapiError")
                            self.log(self.msg, "ERROR")
                            break
            except Exception as e:
                device_id = self.get_device_ids([device_ip])
                delete_params = {
                    "id": device_id[0],
                    "clean_config": self.config[0].get("clean_config", False)
                }
                response = self.dnac._exec(
                    family="devices",
                    function='delete_device_by_id',
                    params=delete_params,
                )

                if response and isinstance(response, dict):
                    task_id = response.get('response').get('taskId')

                    while True:
                        execution_details = self.get_task_details(task_id)

                        if 'success' in execution_details.get("progress"):
                            self.status = "success"
                            self.msg = "Device '{0}' was successfully deleted from Cisco Catalyst Center".format(device_ip)
                            self.log(self.msg, "INFO")
                            self.result['changed'] = True
                            self.result['response'] = execution_details
                            break
                        elif execution_details.get("isError"):
                            self.status = "failed"
                            failure_reason = execution_details.get("failureReason")
                            if failure_reason:
                                self.msg = "Device '{0}' deletion get failed due to: {1}".format(device_ip, failure_reason)
                            else:
                                self.msg = "Device '{0}' deletion get failed.".format(device_ip)
                            self.log(self.msg, "ERROR")
                            break
                    self.result['msg'] = self.msg

        return self

    def verify_diff_merged(self, config):
        """
        Verify the merged status(Addition/Updation) of Devices in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the merged status of a configuration in Cisco Catalyst Center by retrieving the current state
            (have) and desired state (want) of the configuration, logs the states, and validates whether the specified
            site exists in the Catalyst Center configuration.

            The function performs the following verifications:
            - Checks for devices added to Cisco Catalyst Center and logs the status.
            - Verifies updated device roles and logs the status.
            - Verifies updated interface details and logs the status.
            - Verifies updated device credentials and logs the status.
            - Verifies the creation of a global User Defined Field (UDF) and logs the status.
            - Verifies the provisioning of wired devices and logs the status.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")

        devices_to_add = self.have["device_not_in_dnac"]
        device_added = self.config[0].get("device_added", False)
        device_updated = self.config[0].get("device_updated", False)
        credential_update = self.config[0].get("credential_update", False)
        device_type = self.config[0].get("type", "NETWORK_DEVICE")
        device_ips = self.get_device_ips_from_config_priority()

        if device_added:
            if not devices_to_add:
                self.status = "success"
                msg = """Requested device(s) '{0}' have been successfully added to the Cisco Catalyst Center and their
                     addition has been verified.""".format(str(device_ips))
                self.log(msg, "INFO")
            else:
                self.log("""Playbook's input does not match with Cisco Catalyst Center, indicating that the device addition
                     task may not have executed successfully.""", "INFO")

        if device_updated and self.config[0].get('update_interface_details'):
            interface_update_flag = True
            interface_name = self.config[0].get('update_interface_details').get('interface_name')

            for device_ip in device_ips:
                if not self.check_interface_details(device_ip, interface_name):
                    interface_update_flag = False
                    break

            if interface_update_flag:
                self.status = "success"
                msg = "Interface details updated and verified successfully for devices {0}.".format(device_ips)
                self.log(msg, "INFO")
            else:
                self.log("""Playbook's input does not match with Cisco Catalyst Center, indicating that the update
                         interface details task may not have executed successfully.""", "INFO")

        if device_updated and credential_update and device_type == "NETWORK_DEVICE":
            credential_update_flag = self.check_credential_update()

            if credential_update_flag:
                self.status = "success"
                msg = "Device credentials and details updated and verified successfully in Cisco Catalyst Center."
                self.log(msg, "INFO")
            else:
                self.log("Playbook parameter does not match with Cisco Catalyst Center, meaning device updation task not executed properly.", "INFO")
        elif device_type != "NETWORK_DEVICE":
            self.log("""Unable to compare the parameter for device type '{0}' in the playbook with the one in Cisco Catalyst Center."""
                     .format(device_type), "WARNING")

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')
            udf_exist = self.is_udf_exist(field_name)

            if udf_exist:
                self.status = "success"
                msg = "Global UDF {0} created and verified successfully".format(field_name)
                self.log(msg, "INFO")
            else:
                self.log("""Mismatch between playbook parameter and Cisco Catalyst Center detected, indicating that
                         the task of creating Global UDF may not have executed successfully.""", "INFO")

        if device_updated and self.config[0].get('update_device_role'):
            device_role_flag = True

            for device_ip in device_ips:
                if not self.check_device_role(device_ip):
                    device_role_flag = False
                    break

            if device_role_flag:
                self.status = "success"
                msg = "Device roles updated and verified successfully."
                self.log(msg, "INFO")
            else:
                self.log("""Mismatch between playbook parameter 'role' and Cisco Catalyst Center detected, indicating the
                         device role update task may not have executed successfully.""", "INFO")

        if self.config[0].get('provision_wired_device'):
            provision_wired_flag = True

            for device_ip in device_ips:
                if not self.get_provision_wired_device(device_ip):
                    provision_wired_flag = False
                    break

            if provision_wired_flag:
                self.status = "success"
                msg = "Wired devices {0} get provisioned and verified successfully.".format(device_ips)
                self.log(msg, "INFO")
            else:
                self.log("""Mismatch between playbook's input and Cisco Catalyst Center detected, indicating that
                         the provisioning task may not have executed successfully.""", "INFO")

        return self

    def verify_diff_deleted(self, config):
        """
        Verify the deletion status of Device and Global UDF in Cisco Catalyst Center.
        Parameters:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
            - config (dict): The configuration details to be verified.
        Return:
            - self (object): An instance of a class used for interacting with Cisco Catalyst Center.
        Description:
            This method checks the deletion status of a configuration in Cisco Catalyst Center.
            It validates whether the specified Devices or Global UDF deleted from Cisco Catalyst Center.
        """

        self.get_have(config)
        self.log("Current State (have): {0}".format(str(self.have)), "INFO")
        self.log("Desired State (want): {0}".format(str(self.want)), "INFO")
        input_devices = self.have["want_device"]
        device_in_dnac = self.device_exists_in_dnac()

        if self.config[0].get('add_user_defined_field'):
            field_name = self.config[0].get('add_user_defined_field').get('name')
            udf_id = self.get_udf_id(field_name)

            if udf_id is None:
                self.status = "success"
                msg = "Global UDF named '{0}' has been successfully deleted from Cisco Catalyst Center and the deletion has been verified.".format(field_name)
                self.log(msg, "INFO")
                return self

        device_delete_flag = True
        for device_ip in input_devices:
            if device_ip in device_in_dnac:
                device_after_deletion = device_ip
                device_delete_flag = False
                break

        if device_delete_flag:
            self.status = "success"
            self.msg = "Requested device(s) '{0}' deleted from Cisco Catalyst Center and the deletion has been verified.".format(str(input_devices))
            self.log(self.msg, "INFO")
        else:
            self.log("""Mismatch between playbook parameter device({0}) and Cisco Catalyst Center detected, indicating that
                     the device deletion task may not have executed successfully.""".format(device_after_deletion), "INFO")

        return self


def main():
    """ main entry point for module execution
    """

    element_spec = {'dnac_host': {'type': 'str', 'required': True, },
                    'dnac_port': {'type': 'str', 'default': '443'},
                    'dnac_username': {'type': 'str', 'default': 'admin', 'aliases': ['user']},
                    'dnac_password': {'type': 'str', 'no_log': True},
                    'dnac_verify': {'type': 'bool', 'default': 'True'},
                    'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
                    'dnac_debug': {'type': 'bool', 'default': False},
                    'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
                    "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
                    "dnac_log_append": {"type": 'bool', "default": True},
                    'dnac_log': {'type': 'bool', 'default': False},
                    'validate_response_schema': {'type': 'bool', 'default': True},
                    'config_verify': {'type': 'bool', "default": False},
                    'config': {'required': True, 'type': 'list', 'elements': 'dict'},
                    'state': {'default': 'merged', 'choices': ['merged', 'deleted']}
                    }

    module = AnsibleModule(argument_spec=element_spec,
                           supports_check_mode=False)

    dnac_device = DnacDevice(module)
    state = dnac_device.params.get("state")

    if state not in dnac_device.supported_states:
        dnac_device.status = "invalid"
        dnac_device.msg = "State {0} is invalid".format(state)
        dnac_device.check_return_status()

    dnac_device.validate_input().check_return_status()
    config_verify = dnac_device.params.get("config_verify")

    for config in dnac_device.validated_config:
        dnac_device.reset_values()
        dnac_device.get_want(config).check_return_status()
        dnac_device.get_have(config).check_return_status()
        dnac_device.get_diff_state_apply[state](config).check_return_status()
        if config_verify:
            dnac_device.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**dnac_device.result)


if __name__ == '__main__':
    main()
