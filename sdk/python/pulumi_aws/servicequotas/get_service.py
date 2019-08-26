# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, service_code=None, service_name=None, id=None):
        if service_code and not isinstance(service_code, str):
            raise TypeError("Expected argument 'service_code' to be a str")
        __self__.service_code = service_code
        """
        Code of the service.
        """
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        __self__.service_name = service_name
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            service_code=self.service_code,
            service_name=self.service_name,
            id=self.id)

def get_service(service_name=None,opts=None):
    """
    Retrieve information about a Service Quotas Service.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/servicequotas_service.html.markdown.
    """
    __args__ = dict()

    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws:servicequotas/getService:getService', __args__, opts=opts).value

    return AwaitableGetServiceResult(
        service_code=__ret__.get('serviceCode'),
        service_name=__ret__.get('serviceName'),
        id=__ret__.get('id'))
