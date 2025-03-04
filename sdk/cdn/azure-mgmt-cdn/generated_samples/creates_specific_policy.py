# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.cdn import CdnManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cdn
# USAGE
    python creates_specific_policy.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret 
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CdnManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.policies.begin_create_or_update(
        resource_group_name="rg1",
        policy_name="MicrosoftCdnWafPolicy",
        cdn_web_application_firewall_policy={
            "location": "WestUs",
            "properties": {
                "customRules": {
                    "rules": [
                        {
                            "action": "Block",
                            "enabledState": "Enabled",
                            "matchConditions": [
                                {
                                    "matchValue": ["CH"],
                                    "matchVariable": "RemoteAddr",
                                    "negateCondition": False,
                                    "operator": "GeoMatch",
                                    "selector": None,
                                    "transforms": [],
                                },
                                {
                                    "matchValue": ["windows"],
                                    "matchVariable": "RequestHeader",
                                    "negateCondition": False,
                                    "operator": "Contains",
                                    "selector": "UserAgent",
                                    "transforms": [],
                                },
                                {
                                    "matchValue": ["<?php", "?>"],
                                    "matchVariable": "QueryString",
                                    "negateCondition": False,
                                    "operator": "Contains",
                                    "selector": "search",
                                    "transforms": ["UrlDecode", "Lowercase"],
                                },
                            ],
                            "name": "CustomRule1",
                            "priority": 2,
                        }
                    ]
                },
                "managedRules": {
                    "managedRuleSets": [
                        {
                            "ruleGroupOverrides": [
                                {
                                    "ruleGroupName": "Group1",
                                    "rules": [
                                        {"action": "Redirect", "enabledState": "Enabled", "ruleId": "GROUP1-0001"},
                                        {"enabledState": "Disabled", "ruleId": "GROUP1-0002"},
                                    ],
                                }
                            ],
                            "ruleSetType": "DefaultRuleSet",
                            "ruleSetVersion": "preview-1.0",
                        }
                    ]
                },
                "policySettings": {
                    "defaultCustomBlockResponseBody": "PGh0bWw+CjxoZWFkZXI+PHRpdGxlPkhlbGxvPC90aXRsZT48L2hlYWRlcj4KPGJvZHk+CkhlbGxvIHdvcmxkCjwvYm9keT4KPC9odG1sPg==",
                    "defaultCustomBlockResponseStatusCode": 200,
                    "defaultRedirectUrl": "http://www.bing.com",
                },
                "rateLimitRules": {
                    "rules": [
                        {
                            "action": "Block",
                            "enabledState": "Enabled",
                            "matchConditions": [
                                {
                                    "matchValue": ["192.168.1.0/24", "10.0.0.0/24"],
                                    "matchVariable": "RemoteAddr",
                                    "negateCondition": False,
                                    "operator": "IPMatch",
                                    "selector": None,
                                    "transforms": [],
                                }
                            ],
                            "name": "RateLimitRule1",
                            "priority": 1,
                            "rateLimitDurationInMinutes": 0,
                            "rateLimitThreshold": 1000,
                        }
                    ]
                },
            },
            "sku": {"name": "Standard_Microsoft"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cdn/resource-manager/Microsoft.Cdn/stable/2021-06-01/examples/WafPolicyCreateOrUpdate.json
if __name__ == "__main__":
    main()
