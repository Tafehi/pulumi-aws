# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = [
    'GetLocalGatewaysResult',
    'AwaitableGetLocalGatewaysResult',
    'get_local_gateways',
]


class GetLocalGatewaysResult:
    """
    A collection of values returned by getLocalGateways.
    """
    def __init__(__self__, filters=None, id=None, ids=None, tags=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        __self__.filters = filters
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        __self__.ids = ids
        """
        Set of all the Local Gateway identifiers
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags


class AwaitableGetLocalGatewaysResult(GetLocalGatewaysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalGatewaysResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            tags=self.tags)


def get_local_gateways(filters: Optional[List[pulumi.InputType['GetLocalGatewaysFilterArgs']]] = None,
                       tags: Optional[Mapping[str, str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalGatewaysResult:
    """
    Provides information for multiple EC2 Local Gateways, such as their identifiers.

    ## Example Usage

    The following example retrieves Local Gateways with a resource tag of `service` set to `production`.

    ```python
    import pulumi
    import pulumi_aws as aws

    foo_local_gateways = aws.ec2.get_local_gateways(tags={
        "service": "production",
    })
    pulumi.export("foo", foo_local_gateways.ids)
    ```


    :param List[pulumi.InputType['GetLocalGatewaysFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A mapping of tags, each pair of which must exactly match
           a pair on the desired local_gateways.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getLocalGateways:getLocalGateways', __args__, opts=opts).value

    return AwaitableGetLocalGatewaysResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        tags=__ret__.get('tags'))
