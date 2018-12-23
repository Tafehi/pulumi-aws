# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Document(pulumi.CustomResource):
    """
    Provides an SSM Document resource
    
    > **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
    or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
    schema version you must recreate the resource.
    """
    def __init__(__self__, __name__, __opts__=None, content=None, document_format=None, document_type=None, name=None, permissions=None, tags=None):
        """Create a Document resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not content:
            raise TypeError('Missing required property content')
        __props__['content'] = content

        __props__['document_format'] = document_format

        if not document_type:
            raise TypeError('Missing required property document_type')
        __props__['document_type'] = document_type

        __props__['name'] = name

        __props__['permissions'] = permissions

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['created_date'] = None
        __props__['default_version'] = None
        __props__['description'] = None
        __props__['hash'] = None
        __props__['hash_type'] = None
        __props__['latest_version'] = None
        __props__['owner'] = None
        __props__['parameters'] = None
        __props__['platform_types'] = None
        __props__['schema_version'] = None
        __props__['status'] = None

        super(Document, __self__).__init__(
            'aws:ssm/document:Document',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

