# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'S3BucketAssociationClassificationTypeArgs',
]

@pulumi.input_type
class S3BucketAssociationClassificationTypeArgs:
    def __init__(__self__, *,
                 continuous: Optional[pulumi.Input[str]] = None,
                 one_time: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] continuous: A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
               The only valid value is the default value, `FULL`.
        :param pulumi.Input[str] one_time: A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
               Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.
        """
        if continuous is not None:
            pulumi.set(__self__, "continuous", continuous)
        if one_time is not None:
            pulumi.set(__self__, "one_time", one_time)

    @property
    @pulumi.getter
    def continuous(self) -> Optional[pulumi.Input[str]]:
        """
        A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
        The only valid value is the default value, `FULL`.
        """
        ...

    @continuous.setter
    def continuous(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="oneTime")
    def one_time(self) -> Optional[pulumi.Input[str]]:
        """
        A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
        Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.
        """
        ...

    @one_time.setter
    def one_time(self, value: Optional[pulumi.Input[str]]):
        ...

