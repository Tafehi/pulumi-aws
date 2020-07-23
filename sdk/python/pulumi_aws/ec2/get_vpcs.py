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
    'GetVpcsResult',
    'AwaitableGetVpcsResult',
    'get_vpcs',
]


class GetVpcsResult:
    """
    A collection of values returned by getVpcs.
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
        A list of all the VPC Ids found. This data source will fail if none are found.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        __self__.tags = tags


class AwaitableGetVpcsResult(GetVpcsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcsResult(
            filters=self.filters,
            id=self.id,
            ids=self.ids,
            tags=self.tags)


def get_vpcs(filters: Optional[List[pulumi.InputType['GetVpcsFilterArgs']]] = None,
             tags: Optional[Mapping[str, str]] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcsResult:
    """
    This resource can be useful for getting back a list of VPC Ids for a region.

    The following example retrieves a list of VPC Ids with a custom tag of `service` set to a value of "production".

    ## Example Usage

    The following shows outputing all VPC Ids.

    ```python
    import pulumi
    import pulumi_aws as aws

    foo_vpcs = aws.ec2.get_vpcs(tags={
        "service": "production",
    })
    pulumi.export("foo", foo_vpcs.ids)
    ```

    An example use case would be interpolate the `ec2.getVpcs` output into `count` of an ec2.FlowLog resource.

    ```python
    import pulumi
    import pulumi_aws as aws

    foo_vpcs = aws.ec2.get_vpcs()
    test_flow_log = []
    for range in [{"value": i} for i in range(0, len(foo_vpcs.ids))]:
        test_flow_log.append(aws.ec2.FlowLog(f"testFlowLog-{range['value']}", vpc_id=foo_vpcs.ids[range["value"]]))
    pulumi.export("foo", foo_vpcs.ids)
    ```


    :param List[pulumi.InputType['GetVpcsFilterArgs']] filters: Custom filter block as described below.
    :param Mapping[str, str] tags: A map of tags, each pair of which must exactly match
           a pair on the desired vpcs.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:ec2/getVpcs:getVpcs', __args__, opts=opts).value

    return AwaitableGetVpcsResult(
        filters=__ret__.get('filters'),
        id=__ret__.get('id'),
        ids=__ret__.get('ids'),
        tags=__ret__.get('tags'))
