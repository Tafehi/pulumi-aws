# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Recorder(pulumi.CustomResource):
    """
    Provides an AWS Config Configuration Recorder. Please note that this resource **does not start** the created recorder automatically.
    
    > **Note:** _Starting_ the Configuration Recorder requires a [delivery channel](https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html) (while delivery channel creation requires Configuration Recorder). This is why [`aws_config_configuration_recorder_status`](https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html) is a separate resource.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, recording_group=None, role_arn=None):
        """Create a Recorder resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        __props__['recording_group'] = recording_group

        if not role_arn:
            raise TypeError('Missing required property role_arn')
        __props__['role_arn'] = role_arn

        super(Recorder, __self__).__init__(
            'aws:cfg/recorder:Recorder',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

