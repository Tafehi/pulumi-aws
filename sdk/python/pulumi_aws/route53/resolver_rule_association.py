# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ResolverRuleAssociation(pulumi.CustomResource):
    name: pulumi.Output[str]
    """
    A name for the association that you're creating between a resolver rule and a VPC.
    """
    resolver_rule_id: pulumi.Output[str]
    """
    The ID of the resolver rule that you want to associate with the VPC.
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of the VPC that you want to associate the resolver rule with.
    """
    def __init__(__self__, resource_name, opts=None, name=None, resolver_rule_id=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Route53 Resolver rule association.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A name for the association that you're creating between a resolver rule and a VPC.
        :param pulumi.Input[str] resolver_rule_id: The ID of the resolver rule that you want to associate with the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC that you want to associate the resolver rule with.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule_association.html.markdown.
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

            __props__['name'] = name
            if resolver_rule_id is None:
                raise TypeError("Missing required property 'resolver_rule_id'")
            __props__['resolver_rule_id'] = resolver_rule_id
            if vpc_id is None:
                raise TypeError("Missing required property 'vpc_id'")
            __props__['vpc_id'] = vpc_id
        super(ResolverRuleAssociation, __self__).__init__(
            'aws:route53/resolverRuleAssociation:ResolverRuleAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, name=None, resolver_rule_id=None, vpc_id=None):
        """
        Get an existing ResolverRuleAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: A name for the association that you're creating between a resolver rule and a VPC.
        :param pulumi.Input[str] resolver_rule_id: The ID of the resolver rule that you want to associate with the VPC.
        :param pulumi.Input[str] vpc_id: The ID of the VPC that you want to associate the resolver rule with.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/route53_resolver_rule_association.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["name"] = name
        __props__["resolver_rule_id"] = resolver_rule_id
        __props__["vpc_id"] = vpc_id
        return ResolverRuleAssociation(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

