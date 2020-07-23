# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'TrailEventSelectorArgs',
    'TrailEventSelectorDataResourceArgs',
]

@pulumi.input_type
class TrailEventSelectorArgs:
    def __init__(__self__, *,
                 data_resources: Optional[pulumi.Input[List[pulumi.Input['TrailEventSelectorDataResourceArgs']]]] = None,
                 include_management_events: Optional[pulumi.Input[bool]] = None,
                 read_write_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[List[pulumi.Input['TrailEventSelectorDataResourceArgs']]] data_resources: Specifies logging data events. Fields documented below.
        :param pulumi.Input[bool] include_management_events: Specify if you want your event selector to include management events for your trail.
        :param pulumi.Input[str] read_write_type: Specify if you want your trail to log read-only events, write-only events, or all. By default, the value is All. You can specify only the following value: "ReadOnly", "WriteOnly", "All". Defaults to `All`.
        """
        pulumi.set(__self__, "dataResources", data_resources)
        pulumi.set(__self__, "includeManagementEvents", include_management_events)
        pulumi.set(__self__, "readWriteType", read_write_type)

    @property
    @pulumi.getter(name="dataResources")
    def data_resources(self) -> Optional[pulumi.Input[List[pulumi.Input['TrailEventSelectorDataResourceArgs']]]]:
        """
        Specifies logging data events. Fields documented below.
        """
        ...

    @data_resources.setter
    def data_resources(self, value: Optional[pulumi.Input[List[pulumi.Input['TrailEventSelectorDataResourceArgs']]]]):
        ...

    @property
    @pulumi.getter(name="includeManagementEvents")
    def include_management_events(self) -> Optional[pulumi.Input[bool]]:
        """
        Specify if you want your event selector to include management events for your trail.
        """
        ...

    @include_management_events.setter
    def include_management_events(self, value: Optional[pulumi.Input[bool]]):
        ...

    @property
    @pulumi.getter(name="readWriteType")
    def read_write_type(self) -> Optional[pulumi.Input[str]]:
        """
        Specify if you want your trail to log read-only events, write-only events, or all. By default, the value is All. You can specify only the following value: "ReadOnly", "WriteOnly", "All". Defaults to `All`.
        """
        ...

    @read_write_type.setter
    def read_write_type(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class TrailEventSelectorDataResourceArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 values: pulumi.Input[List[pulumi.Input[str]]]):
        """
        :param pulumi.Input[str] type: The resource type in which you want to log data events. You can specify only the following value: "AWS::S3::Object", "AWS::Lambda::Function"
        :param pulumi.Input[List[pulumi.Input[str]]] values: A list of ARN for the specified S3 buckets and object prefixes..
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The resource type in which you want to log data events. You can specify only the following value: "AWS::S3::Object", "AWS::Lambda::Function"
        """
        ...

    @type.setter
    def type(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def values(self) -> pulumi.Input[List[pulumi.Input[str]]]:
        """
        A list of ARN for the specified S3 buckets and object prefixes..
        """
        ...

    @values.setter
    def values(self, value: pulumi.Input[List[pulumi.Input[str]]]):
        ...


