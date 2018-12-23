# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class VpcEndpointService(pulumi.CustomResource):
    """
    Provides a VPC Endpoint Service resource.
    Service consumers can create an _Interface_ VPC Endpoint to connect to the service.
    
    > **NOTE on VPC Endpoint Services and VPC Endpoint Service Allowed Principals:** Terraform provides
    both a standalone VPC Endpoint Service Allowed Principal resource
    and a VPC Endpoint Service resource with an `allowed_principals` attribute. Do not use the same principal ARN in both
    a VPC Endpoint Service resource and a VPC Endpoint Service Allowed Principal resource. Doing so will cause a conflict
    and will overwrite the association.
    """
    def __init__(__self__, __name__, __opts__=None, acceptance_required=None, allowed_principals=None, network_load_balancer_arns=None):
        """Create a VpcEndpointService resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not acceptance_required:
            raise TypeError('Missing required property acceptance_required')
        __props__['acceptance_required'] = acceptance_required

        __props__['allowed_principals'] = allowed_principals

        if not network_load_balancer_arns:
            raise TypeError('Missing required property network_load_balancer_arns')
        __props__['network_load_balancer_arns'] = network_load_balancer_arns

        __props__['availability_zones'] = None
        __props__['base_endpoint_dns_names'] = None
        __props__['private_dns_name'] = None
        __props__['service_name'] = None
        __props__['service_type'] = None
        __props__['state'] = None

        super(VpcEndpointService, __self__).__init__(
            'aws:ec2/vpcEndpointService:VpcEndpointService',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

