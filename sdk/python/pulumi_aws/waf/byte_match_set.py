# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ByteMatchSet(pulumi.CustomResource):
    byte_match_tuples: pulumi.Output[list]
    """
    Specifies the bytes (typically a string that corresponds
    with ASCII characters) that you want to search for in web requests,
    the location in requests that you want to search, and other settings.
    """
    name: pulumi.Output[str]
    """
    The name or description of the Byte Match Set.
    """
    def __init__(__self__, resource_name, opts=None, byte_match_tuples=None, name=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a WAF Byte Match Set Resource
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] byte_match_tuples: Specifies the bytes (typically a string that corresponds
               with ASCII characters) that you want to search for in web requests,
               the location in requests that you want to search, and other settings.
        :param pulumi.Input[str] name: The name or description of the Byte Match Set.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['byte_match_tuples'] = byte_match_tuples
            __props__['name'] = name
        super(ByteMatchSet, __self__).__init__(
            'aws:waf/byteMatchSet:ByteMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, byte_match_tuples=None, name=None):
        """
        Get an existing ByteMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] byte_match_tuples: Specifies the bytes (typically a string that corresponds
               with ASCII characters) that you want to search for in web requests,
               the location in requests that you want to search, and other settings.
        :param pulumi.Input[str] name: The name or description of the Byte Match Set.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_byte_match_set.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["byte_match_tuples"] = byte_match_tuples
        __props__["name"] = name
        return ByteMatchSet(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

