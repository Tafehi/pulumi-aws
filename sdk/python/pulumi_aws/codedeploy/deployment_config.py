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

__all__ = ['DeploymentConfig']


class DeploymentConfig(pulumi.CustomResource):
    compute_platform: pulumi.Output[Optional[str]] = pulumi.property("computePlatform")
    """
    The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
    """

    deployment_config_id: pulumi.Output[str] = pulumi.property("deploymentConfigId")
    """
    The AWS Assigned deployment config id
    """

    deployment_config_name: pulumi.Output[str] = pulumi.property("deploymentConfigName")
    """
    The name of the deployment config.
    """

    minimum_healthy_hosts: pulumi.Output[Optional['outputs.DeploymentConfigMinimumHealthyHosts']] = pulumi.property("minimumHealthyHosts")
    """
    A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
    """

    traffic_routing_config: pulumi.Output[Optional['outputs.DeploymentConfigTrafficRoutingConfig']] = pulumi.property("trafficRoutingConfig")
    """
    A traffic_routing_config block. Traffic Routing Config is documented below.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_platform: Optional[pulumi.Input[str]] = None,
                 deployment_config_name: Optional[pulumi.Input[str]] = None,
                 minimum_healthy_hosts: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']]] = None,
                 traffic_routing_config: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CodeDeploy deployment config for an application

        ## Example Usage
        ### Server Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo_deployment_config = aws.codedeploy.DeploymentConfig("fooDeploymentConfig",
            deployment_config_name="test-deployment-config",
            minimum_healthy_hosts={
                "type": "HOST_COUNT",
                "value": 2,
            })
        foo_deployment_group = aws.codedeploy.DeploymentGroup("fooDeploymentGroup",
            alarm_configuration={
                "alarms": ["my-alarm-name"],
                "enabled": True,
            },
            app_name=aws_codedeploy_app["foo_app"]["name"],
            auto_rollback_configuration={
                "enabled": True,
                "events": ["DEPLOYMENT_FAILURE"],
            },
            deployment_config_name=foo_deployment_config.id,
            deployment_group_name="bar",
            ec2_tag_filters=[{
                "key": "filterkey",
                "type": "KEY_AND_VALUE",
                "value": "filtervalue",
            }],
            service_role_arn=aws_iam_role["foo_role"]["arn"],
            trigger_configurations=[{
                "triggerEvents": ["DeploymentFailure"],
                "triggerName": "foo-trigger",
                "triggerTargetArn": "foo-topic-arn",
            }])
        ```
        ### Lambda Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        foo_deployment_config = aws.codedeploy.DeploymentConfig("fooDeploymentConfig",
            compute_platform="Lambda",
            deployment_config_name="test-deployment-config",
            traffic_routing_config={
                "timeBasedLinear": {
                    "interval": 10,
                    "percentage": 10,
                },
                "type": "TimeBasedLinear",
            })
        foo_deployment_group = aws.codedeploy.DeploymentGroup("fooDeploymentGroup",
            alarm_configuration={
                "alarms": ["my-alarm-name"],
                "enabled": True,
            },
            app_name=aws_codedeploy_app["foo_app"]["name"],
            auto_rollback_configuration={
                "enabled": True,
                "events": ["DEPLOYMENT_STOP_ON_ALARM"],
            },
            deployment_config_name=foo_deployment_config.id,
            deployment_group_name="bar",
            service_role_arn=aws_iam_role["foo_role"]["arn"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        :param pulumi.Input[str] deployment_config_name: The name of the deployment config.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']] minimum_healthy_hosts: A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['compute_platform'] = compute_platform
            if deployment_config_name is None:
                raise TypeError("Missing required property 'deployment_config_name'")
            __props__['deployment_config_name'] = deployment_config_name
            __props__['minimum_healthy_hosts'] = minimum_healthy_hosts
            __props__['traffic_routing_config'] = traffic_routing_config
            __props__['deployment_config_id'] = None
        super(DeploymentConfig, __self__).__init__(
            'aws:codedeploy/deploymentConfig:DeploymentConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_platform: Optional[pulumi.Input[str]] = None,
            deployment_config_id: Optional[pulumi.Input[str]] = None,
            deployment_config_name: Optional[pulumi.Input[str]] = None,
            minimum_healthy_hosts: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']]] = None,
            traffic_routing_config: Optional[pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']]] = None) -> 'DeploymentConfig':
        """
        Get an existing DeploymentConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_platform: The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
        :param pulumi.Input[str] deployment_config_id: The AWS Assigned deployment config id
        :param pulumi.Input[str] deployment_config_name: The name of the deployment config.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigMinimumHealthyHostsArgs']] minimum_healthy_hosts: A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
        :param pulumi.Input[pulumi.InputType['DeploymentConfigTrafficRoutingConfigArgs']] traffic_routing_config: A traffic_routing_config block. Traffic Routing Config is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["compute_platform"] = compute_platform
        __props__["deployment_config_id"] = deployment_config_id
        __props__["deployment_config_name"] = deployment_config_name
        __props__["minimum_healthy_hosts"] = minimum_healthy_hosts
        __props__["traffic_routing_config"] = traffic_routing_config
        return DeploymentConfig(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

