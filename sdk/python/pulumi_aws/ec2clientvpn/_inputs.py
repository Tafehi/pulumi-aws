# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EndpointAuthenticationOptionArgs',
    'EndpointConnectionLogOptionsArgs',
]

@pulumi.input_type
class EndpointAuthenticationOptionArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 active_directory_id: Optional[pulumi.Input[str]] = None,
                 root_certificate_chain_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] type: The type of client authentication to be used. Specify `certificate-authentication` to use certificate-based authentication, or `directory-service-authentication` to use Active Directory authentication.
        :param pulumi.Input[str] active_directory_id: The ID of the Active Directory to be used for authentication if type is `directory-service-authentication`.
        :param pulumi.Input[str] root_certificate_chain_arn: The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to `certificate-authentication`.
        """
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "activeDirectoryId", active_directory_id)
        pulumi.set(__self__, "rootCertificateChainArn", root_certificate_chain_arn)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of client authentication to be used. Specify `certificate-authentication` to use certificate-based authentication, or `directory-service-authentication` to use Active Directory authentication.
        """
        ...

    @type.setter
    def type(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="activeDirectoryId")
    def active_directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Active Directory to be used for authentication if type is `directory-service-authentication`.
        """
        ...

    @active_directory_id.setter
    def active_directory_id(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="rootCertificateChainArn")
    def root_certificate_chain_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to `certificate-authentication`.
        """
        ...

    @root_certificate_chain_arn.setter
    def root_certificate_chain_arn(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class EndpointConnectionLogOptionsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 cloudwatch_log_group: Optional[pulumi.Input[str]] = None,
                 cloudwatch_log_stream: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] enabled: Indicates whether connection logging is enabled.
        :param pulumi.Input[str] cloudwatch_log_group: The name of the CloudWatch Logs log group.
        :param pulumi.Input[str] cloudwatch_log_stream: The name of the CloudWatch Logs log stream to which the connection data is published.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "cloudwatchLogGroup", cloudwatch_log_group)
        pulumi.set(__self__, "cloudwatchLogStream", cloudwatch_log_stream)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Indicates whether connection logging is enabled.
        """
        ...

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        ...

    @property
    @pulumi.getter(name="cloudwatchLogGroup")
    def cloudwatch_log_group(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the CloudWatch Logs log group.
        """
        ...

    @cloudwatch_log_group.setter
    def cloudwatch_log_group(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="cloudwatchLogStream")
    def cloudwatch_log_stream(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the CloudWatch Logs log stream to which the connection data is published.
        """
        ...

    @cloudwatch_log_stream.setter
    def cloudwatch_log_stream(self, value: Optional[pulumi.Input[str]]):
        ...


