# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetEventCategoriesResult:
    """
    A collection of values returned by getEventCategories.
    """
    def __init__(__self__, event_categories=None, source_type=None, id=None):
        if event_categories and not isinstance(event_categories, list):
            raise TypeError("Expected argument 'event_categories' to be a list")
        __self__.event_categories = event_categories
        """
        A list of the event categories.
        """
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        __self__.source_type = source_type
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetEventCategoriesResult(GetEventCategoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventCategoriesResult(
            event_categories=self.event_categories,
            source_type=self.source_type,
            id=self.id)

def get_event_categories(source_type=None,opts=None):
    __args__ = dict()

    __args__['sourceType'] = source_type
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:rds/getEventCategories:getEventCategories', __args__, opts=opts).value

    return AwaitableGetEventCategoriesResult(
        event_categories=__ret__.get('eventCategories'),
        source_type=__ret__.get('sourceType'),
        id=__ret__.get('id'))
