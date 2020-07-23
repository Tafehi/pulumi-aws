# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'GetOrganizationalUnitsResult',
    'AwaitableGetOrganizationalUnitsResult',
    'get_organizational_units',
]


class GetOrganizationalUnitsResult:
    """
    A collection of values returned by getOrganizationalUnits.
    """
    def __init__(__self__, childrens=None, id=None, parent_id=None):
        if childrens and not isinstance(childrens, list):
            raise TypeError("Expected argument 'childrens' to be a list")
        __self__.childrens = childrens
        """
        List of child organizational units, which have the following attributes:
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        __self__.parent_id = parent_id


class AwaitableGetOrganizationalUnitsResult(GetOrganizationalUnitsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationalUnitsResult(
            childrens=self.childrens,
            id=self.id,
            parent_id=self.parent_id)


def get_organizational_units(parent_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationalUnitsResult:
    """
    Get all direct child organizational units under a parent organizational unit. This only provides immediate children, not all children.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    org = aws.organizations.get_organization()
    ou = aws.organizations.get_organizational_units(parent_id=org.roots[0]["id"])
    ```


    :param str parent_id: The parent ID of the organizational unit.
    """
    __args__ = dict()
    __args__['parentId'] = parent_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:organizations/getOrganizationalUnits:getOrganizationalUnits', __args__, opts=opts).value

    return AwaitableGetOrganizationalUnitsResult(
        childrens=__ret__.get('childrens'),
        id=__ret__.get('id'),
        parent_id=__ret__.get('parentId'))
