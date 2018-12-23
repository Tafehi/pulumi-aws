# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Listener(pulumi.CustomResource):
    """
    Provides a Load Balancer Listener resource.
    
    > **Note:** `aws_alb_listener` is known as `aws_lb_listener`. The functionality is identical.
    """
    def __init__(__self__, __name__, __opts__=None, certificate_arn=None, default_action=None, load_balancer_arn=None, port=None, protocol=None, ssl_policy=None):
        """Create a Listener resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['certificate_arn'] = certificate_arn

        if not default_action:
            raise TypeError('Missing required property default_action')
        __props__['default_action'] = default_action

        if not load_balancer_arn:
            raise TypeError('Missing required property load_balancer_arn')
        __props__['load_balancer_arn'] = load_balancer_arn

        if not port:
            raise TypeError('Missing required property port')
        __props__['port'] = port

        __props__['protocol'] = protocol

        __props__['ssl_policy'] = ssl_policy

        __props__['arn'] = None

        super(Listener, __self__).__init__(
            'aws:applicationloadbalancing/listener:Listener',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

