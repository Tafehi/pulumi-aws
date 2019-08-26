# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Webhook(pulumi.CustomResource):
    branch_filter: pulumi.Output[str]
    """
    A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filter_group` over `branch_filter`.
    """
    filter_groups: pulumi.Output[list]
    """
    Information about the webhook's trigger. Filter group blocks are documented below.
    """
    payload_url: pulumi.Output[str]
    """
    The CodeBuild endpoint where webhook events are sent.
    """
    project_name: pulumi.Output[str]
    """
    The name of the build project.
    """
    secret: pulumi.Output[str]
    """
    The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
    """
    url: pulumi.Output[str]
    """
    The URL to the webhook.
    """
    def __init__(__self__, resource_name, opts=None, branch_filter=None, filter_groups=None, project_name=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a CodeBuild webhook, which is an endpoint accepted by the CodeBuild service to trigger builds from source code repositories. Depending on the source type of the CodeBuild project, the CodeBuild service may also automatically create and delete the actual repository webhook as well.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_filter: A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filter_group` over `branch_filter`.
        :param pulumi.Input[list] filter_groups: Information about the webhook's trigger. Filter group blocks are documented below.
        :param pulumi.Input[str] project_name: The name of the build project.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown.
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

            __props__['branch_filter'] = branch_filter
            __props__['filter_groups'] = filter_groups
            if project_name is None:
                raise TypeError("Missing required property 'project_name'")
            __props__['project_name'] = project_name
            __props__['payload_url'] = None
            __props__['secret'] = None
            __props__['url'] = None
        super(Webhook, __self__).__init__(
            'aws:codebuild/webhook:Webhook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, branch_filter=None, filter_groups=None, payload_url=None, project_name=None, secret=None, url=None):
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_filter: A regular expression used to determine which branches get built. Default is all branches are built. It is recommended to use `filter_group` over `branch_filter`.
        :param pulumi.Input[list] filter_groups: Information about the webhook's trigger. Filter group blocks are documented below.
        :param pulumi.Input[str] payload_url: The CodeBuild endpoint where webhook events are sent.
        :param pulumi.Input[str] project_name: The name of the build project.
        :param pulumi.Input[str] secret: The secret token of the associated repository. Not returned by the CodeBuild API for all source types.
        :param pulumi.Input[str] url: The URL to the webhook.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codebuild_webhook.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["branch_filter"] = branch_filter
        __props__["filter_groups"] = filter_groups
        __props__["payload_url"] = payload_url
        __props__["project_name"] = project_name
        __props__["secret"] = secret
        __props__["url"] = url
        return Webhook(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

