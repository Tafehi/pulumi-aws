# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = [
    'EventDestinationCloudwatchDestinationArgs',
    'EventDestinationKinesisDestinationArgs',
    'EventDestinationSnsDestinationArgs',
    'ReceiptRuleAddHeaderActionArgs',
    'ReceiptRuleBounceActionArgs',
    'ReceiptRuleLambdaActionArgs',
    'ReceiptRuleS3ActionArgs',
    'ReceiptRuleSnsActionArgs',
    'ReceiptRuleStopActionArgs',
    'ReceiptRuleWorkmailActionArgs',
]

@pulumi.input_type
class EventDestinationCloudwatchDestinationArgs:
    def __init__(__self__, *,
                 default_value: pulumi.Input[str],
                 dimension_name: pulumi.Input[str],
                 value_source: pulumi.Input[str]):
        """
        :param pulumi.Input[str] default_value: The default value for the event
        :param pulumi.Input[str] dimension_name: The name for the dimension
        :param pulumi.Input[str] value_source: The source for the value. It can be either `"messageTag"` or `"emailHeader"`
        """
        pulumi.set(__self__, "default_value", default_value)
        pulumi.set(__self__, "dimension_name", dimension_name)
        pulumi.set(__self__, "value_source", value_source)

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Input[str]:
        """
        The default value for the event
        """
        ...

    @default_value.setter
    def default_value(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="dimensionName")
    def dimension_name(self) -> pulumi.Input[str]:
        """
        The name for the dimension
        """
        ...

    @dimension_name.setter
    def dimension_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="valueSource")
    def value_source(self) -> pulumi.Input[str]:
        """
        The source for the value. It can be either `"messageTag"` or `"emailHeader"`
        """
        ...

    @value_source.setter
    def value_source(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class EventDestinationKinesisDestinationArgs:
    def __init__(__self__, *,
                 role_arn: pulumi.Input[str],
                 stream_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[str] role_arn: The ARN of the role that has permissions to access the Kinesis Stream
        :param pulumi.Input[str] stream_arn: The ARN of the Kinesis Stream
        """
        pulumi.set(__self__, "role_arn", role_arn)
        pulumi.set(__self__, "stream_arn", stream_arn)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that has permissions to access the Kinesis Stream
        """
        ...

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the Kinesis Stream
        """
        ...

    @stream_arn.setter
    def stream_arn(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class EventDestinationSnsDestinationArgs:
    def __init__(__self__, *,
                 topic_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[str] topic_arn: The ARN of the SNS topic
        """
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the SNS topic
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class ReceiptRuleAddHeaderActionArgs:
    def __init__(__self__, *,
                 header_name: pulumi.Input[str],
                 header_value: pulumi.Input[str],
                 position: pulumi.Input[float]):
        """
        :param pulumi.Input[str] header_name: The name of the header to add
        :param pulumi.Input[str] header_value: The value of the header to add
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        """
        pulumi.set(__self__, "header_name", header_name)
        pulumi.set(__self__, "header_value", header_value)
        pulumi.set(__self__, "position", position)

    @property
    @pulumi.getter(name="headerName")
    def header_name(self) -> pulumi.Input[str]:
        """
        The name of the header to add
        """
        ...

    @header_name.setter
    def header_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[str]:
        """
        The value of the header to add
        """
        ...

    @header_value.setter
    def header_value(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...


@pulumi.input_type
class ReceiptRuleBounceActionArgs:
    def __init__(__self__, *,
                 message: pulumi.Input[str],
                 position: pulumi.Input[float],
                 sender: pulumi.Input[str],
                 smtp_reply_code: pulumi.Input[str],
                 status_code: Optional[pulumi.Input[str]] = None,
                 topic_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] message: The message to send
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] sender: The email address of the sender
        :param pulumi.Input[str] smtp_reply_code: The RFC 5321 SMTP reply code
        :param pulumi.Input[str] status_code: The RFC 3463 SMTP enhanced status code
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "message", message)
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "sender", sender)
        pulumi.set(__self__, "smtp_reply_code", smtp_reply_code)
        if status_code is not None:
            pulumi.set(__self__, "status_code", status_code)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def message(self) -> pulumi.Input[str]:
        """
        The message to send
        """
        ...

    @message.setter
    def message(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter
    def sender(self) -> pulumi.Input[str]:
        """
        The email address of the sender
        """
        ...

    @sender.setter
    def sender(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="smtpReplyCode")
    def smtp_reply_code(self) -> pulumi.Input[str]:
        """
        The RFC 5321 SMTP reply code
        """
        ...

    @smtp_reply_code.setter
    def smtp_reply_code(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="statusCode")
    def status_code(self) -> Optional[pulumi.Input[str]]:
        """
        The RFC 3463 SMTP enhanced status code
        """
        ...

    @status_code.setter
    def status_code(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class ReceiptRuleLambdaActionArgs:
    def __init__(__self__, *,
                 function_arn: pulumi.Input[str],
                 position: pulumi.Input[float],
                 invocation_type: Optional[pulumi.Input[str]] = None,
                 topic_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] function_arn: The ARN of the Lambda function to invoke
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] invocation_type: Event or RequestResponse
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "function_arn", function_arn)
        pulumi.set(__self__, "position", position)
        if invocation_type is not None:
            pulumi.set(__self__, "invocation_type", invocation_type)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="functionArn")
    def function_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the Lambda function to invoke
        """
        ...

    @function_arn.setter
    def function_arn(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="invocationType")
    def invocation_type(self) -> Optional[pulumi.Input[str]]:
        """
        Event or RequestResponse
        """
        ...

    @invocation_type.setter
    def invocation_type(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class ReceiptRuleS3ActionArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 position: pulumi.Input[float],
                 kms_key_arn: Optional[pulumi.Input[str]] = None,
                 object_key_prefix: Optional[pulumi.Input[str]] = None,
                 topic_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] bucket_name: The name of the S3 bucket
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] kms_key_arn: The ARN of the KMS key
        :param pulumi.Input[str] object_key_prefix: The key prefix of the S3 bucket
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "bucket_name", bucket_name)
        pulumi.set(__self__, "position", position)
        if kms_key_arn is not None:
            pulumi.set(__self__, "kms_key_arn", kms_key_arn)
        if object_key_prefix is not None:
            pulumi.set(__self__, "object_key_prefix", object_key_prefix)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        The name of the S3 bucket
        """
        ...

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the KMS key
        """
        ...

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="objectKeyPrefix")
    def object_key_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The key prefix of the S3 bucket
        """
        ...

    @object_key_prefix.setter
    def object_key_prefix(self, value: Optional[pulumi.Input[str]]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class ReceiptRuleSnsActionArgs:
    def __init__(__self__, *,
                 position: pulumi.Input[float],
                 topic_arn: pulumi.Input[str]):
        """
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> pulumi.Input[str]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: pulumi.Input[str]):
        ...


@pulumi.input_type
class ReceiptRuleStopActionArgs:
    def __init__(__self__, *,
                 position: pulumi.Input[float],
                 scope: pulumi.Input[str],
                 topic_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] scope: The scope to apply
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "position", position)
        pulumi.set(__self__, "scope", scope)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope to apply
        """
        ...

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[str]]):
        ...


@pulumi.input_type
class ReceiptRuleWorkmailActionArgs:
    def __init__(__self__, *,
                 organization_arn: pulumi.Input[str],
                 position: pulumi.Input[float],
                 topic_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] organization_arn: The ARN of the WorkMail organization
        :param pulumi.Input[float] position: The position of the action in the receipt rule
        :param pulumi.Input[str] topic_arn: The ARN of an SNS topic to notify
        """
        pulumi.set(__self__, "organization_arn", organization_arn)
        pulumi.set(__self__, "position", position)
        if topic_arn is not None:
            pulumi.set(__self__, "topic_arn", topic_arn)

    @property
    @pulumi.getter(name="organizationArn")
    def organization_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the WorkMail organization
        """
        ...

    @organization_arn.setter
    def organization_arn(self, value: pulumi.Input[str]):
        ...

    @property
    @pulumi.getter
    def position(self) -> pulumi.Input[float]:
        """
        The position of the action in the receipt rule
        """
        ...

    @position.setter
    def position(self, value: pulumi.Input[float]):
        ...

    @property
    @pulumi.getter(name="topicArn")
    def topic_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of an SNS topic to notify
        """
        ...

    @topic_arn.setter
    def topic_arn(self, value: Optional[pulumi.Input[str]]):
        ...

