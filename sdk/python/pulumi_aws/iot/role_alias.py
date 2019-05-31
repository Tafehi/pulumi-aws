# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class RoleAlias(pulumi.CustomResource):
    alias: pulumi.Output[str]
    """
    The name of the role alias.
    """
    arn: pulumi.Output[str]
    """
    The ARN assigned by AWS to this role alias.
    """
    credential_duration: pulumi.Output[float]
    """
    The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).
    """
    role_arn: pulumi.Output[str]
    """
    The identity of the role to which the alias refers.
    """
    def __init__(__self__, resource_name, opts=None, alias=None, credential_duration=None, role_arn=None, __name__=None, __opts__=None):
        """
        Provides an IoT role alias.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alias: The name of the role alias.
        :param pulumi.Input[float] credential_duration: The duration of the credential, in seconds. If you do not specify a value for this setting, the default maximum of one hour is applied. This setting can have a value from 900 seconds (15 minutes) to 3600 seconds (60 minutes).
        :param pulumi.Input[str] role_arn: The identity of the role to which the alias refers.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if alias is None:
            raise TypeError("Missing required property 'alias'")
        __props__['alias'] = alias

        __props__['credential_duration'] = credential_duration

        if role_arn is None:
            raise TypeError("Missing required property 'role_arn'")
        __props__['role_arn'] = role_arn

        __props__['arn'] = None

        super(RoleAlias, __self__).__init__(
            'aws:iot/roleAlias:RoleAlias',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

