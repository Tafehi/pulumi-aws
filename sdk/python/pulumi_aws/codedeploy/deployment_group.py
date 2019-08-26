# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class DeploymentGroup(pulumi.CustomResource):
    alarm_configuration: pulumi.Output[dict]
    """
    Configuration block of alarms associated with the deployment group (documented below).
    """
    app_name: pulumi.Output[str]
    """
    The name of the application.
    """
    auto_rollback_configuration: pulumi.Output[dict]
    """
    Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
    """
    autoscaling_groups: pulumi.Output[list]
    """
    Autoscaling groups associated with the deployment group.
    """
    blue_green_deployment_config: pulumi.Output[dict]
    """
    Configuration block of the blue/green deployment options for a deployment group (documented below).
    """
    deployment_config_name: pulumi.Output[str]
    """
    The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
    """
    deployment_group_name: pulumi.Output[str]
    """
    The name of the deployment group.
    """
    deployment_style: pulumi.Output[dict]
    """
    Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
    """
    ec2_tag_filters: pulumi.Output[list]
    """
    Tag filters associated with the deployment group. See the AWS docs for details.
    """
    ec2_tag_sets: pulumi.Output[list]
    """
    Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
    """
    ecs_service: pulumi.Output[dict]
    """
    Configuration block(s) of the ECS services for a deployment group (documented below).
    """
    load_balancer_info: pulumi.Output[dict]
    """
    Single configuration block of the load balancer to use in a blue/green deployment (documented below).
    """
    on_premises_instance_tag_filters: pulumi.Output[list]
    """
    On premise tag filters associated with the group. See the AWS docs for details.
    """
    service_role_arn: pulumi.Output[str]
    """
    The service role ARN that allows deployments.
    """
    trigger_configurations: pulumi.Output[list]
    """
    Configuration block(s) of the triggers for the deployment group (documented below).
    """
    def __init__(__self__, resource_name, opts=None, alarm_configuration=None, app_name=None, auto_rollback_configuration=None, autoscaling_groups=None, blue_green_deployment_config=None, deployment_config_name=None, deployment_group_name=None, deployment_style=None, ec2_tag_filters=None, ec2_tag_sets=None, ecs_service=None, load_balancer_info=None, on_premises_instance_tag_filters=None, service_role_arn=None, trigger_configurations=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a CodeDeploy Deployment Group for a CodeDeploy Application
        
        > **NOTE on blue/green deployments:** When using `green_fleet_provisioning_option` with the `COPY_AUTO_SCALING_GROUP` action, CodeDeploy will create a new ASG with a different name. This ASG is _not_ managed by this provider and will conflict with existing configuration and state. You may want to use a different approach to managing deployments that involve multiple ASG, such as `DISCOVER_EXISTING` with separate blue and green ASG.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] alarm_configuration: Configuration block of alarms associated with the deployment group (documented below).
        :param pulumi.Input[str] app_name: The name of the application.
        :param pulumi.Input[dict] auto_rollback_configuration: Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
        :param pulumi.Input[list] autoscaling_groups: Autoscaling groups associated with the deployment group.
        :param pulumi.Input[dict] blue_green_deployment_config: Configuration block of the blue/green deployment options for a deployment group (documented below).
        :param pulumi.Input[str] deployment_config_name: The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
        :param pulumi.Input[str] deployment_group_name: The name of the deployment group.
        :param pulumi.Input[dict] deployment_style: Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
        :param pulumi.Input[list] ec2_tag_filters: Tag filters associated with the deployment group. See the AWS docs for details.
        :param pulumi.Input[list] ec2_tag_sets: Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
        :param pulumi.Input[dict] ecs_service: Configuration block(s) of the ECS services for a deployment group (documented below).
        :param pulumi.Input[dict] load_balancer_info: Single configuration block of the load balancer to use in a blue/green deployment (documented below).
        :param pulumi.Input[list] on_premises_instance_tag_filters: On premise tag filters associated with the group. See the AWS docs for details.
        :param pulumi.Input[str] service_role_arn: The service role ARN that allows deployments.
        :param pulumi.Input[list] trigger_configurations: Configuration block(s) of the triggers for the deployment group (documented below).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['alarm_configuration'] = alarm_configuration
            if app_name is None:
                raise TypeError("Missing required property 'app_name'")
            __props__['app_name'] = app_name
            __props__['auto_rollback_configuration'] = auto_rollback_configuration
            __props__['autoscaling_groups'] = autoscaling_groups
            __props__['blue_green_deployment_config'] = blue_green_deployment_config
            __props__['deployment_config_name'] = deployment_config_name
            if deployment_group_name is None:
                raise TypeError("Missing required property 'deployment_group_name'")
            __props__['deployment_group_name'] = deployment_group_name
            __props__['deployment_style'] = deployment_style
            __props__['ec2_tag_filters'] = ec2_tag_filters
            __props__['ec2_tag_sets'] = ec2_tag_sets
            __props__['ecs_service'] = ecs_service
            __props__['load_balancer_info'] = load_balancer_info
            __props__['on_premises_instance_tag_filters'] = on_premises_instance_tag_filters
            if service_role_arn is None:
                raise TypeError("Missing required property 'service_role_arn'")
            __props__['service_role_arn'] = service_role_arn
            __props__['trigger_configurations'] = trigger_configurations
        super(DeploymentGroup, __self__).__init__(
            'aws:codedeploy/deploymentGroup:DeploymentGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, alarm_configuration=None, app_name=None, auto_rollback_configuration=None, autoscaling_groups=None, blue_green_deployment_config=None, deployment_config_name=None, deployment_group_name=None, deployment_style=None, ec2_tag_filters=None, ec2_tag_sets=None, ecs_service=None, load_balancer_info=None, on_premises_instance_tag_filters=None, service_role_arn=None, trigger_configurations=None):
        """
        Get an existing DeploymentGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] alarm_configuration: Configuration block of alarms associated with the deployment group (documented below).
        :param pulumi.Input[str] app_name: The name of the application.
        :param pulumi.Input[dict] auto_rollback_configuration: Configuration block of the automatic rollback configuration associated with the deployment group (documented below).
        :param pulumi.Input[list] autoscaling_groups: Autoscaling groups associated with the deployment group.
        :param pulumi.Input[dict] blue_green_deployment_config: Configuration block of the blue/green deployment options for a deployment group (documented below).
        :param pulumi.Input[str] deployment_config_name: The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".
        :param pulumi.Input[str] deployment_group_name: The name of the deployment group.
        :param pulumi.Input[dict] deployment_style: Configuration block of the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).
        :param pulumi.Input[list] ec2_tag_filters: Tag filters associated with the deployment group. See the AWS docs for details.
        :param pulumi.Input[list] ec2_tag_sets: Configuration block(s) of Tag filters associated with the deployment group, which are also referred to as tag groups (documented below). See the AWS docs for details.
        :param pulumi.Input[dict] ecs_service: Configuration block(s) of the ECS services for a deployment group (documented below).
        :param pulumi.Input[dict] load_balancer_info: Single configuration block of the load balancer to use in a blue/green deployment (documented below).
        :param pulumi.Input[list] on_premises_instance_tag_filters: On premise tag filters associated with the group. See the AWS docs for details.
        :param pulumi.Input[str] service_role_arn: The service role ARN that allows deployments.
        :param pulumi.Input[list] trigger_configurations: Configuration block(s) of the triggers for the deployment group (documented below).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_group.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["alarm_configuration"] = alarm_configuration
        __props__["app_name"] = app_name
        __props__["auto_rollback_configuration"] = auto_rollback_configuration
        __props__["autoscaling_groups"] = autoscaling_groups
        __props__["blue_green_deployment_config"] = blue_green_deployment_config
        __props__["deployment_config_name"] = deployment_config_name
        __props__["deployment_group_name"] = deployment_group_name
        __props__["deployment_style"] = deployment_style
        __props__["ec2_tag_filters"] = ec2_tag_filters
        __props__["ec2_tag_sets"] = ec2_tag_sets
        __props__["ecs_service"] = ecs_service
        __props__["load_balancer_info"] = load_balancer_info
        __props__["on_premises_instance_tag_filters"] = on_premises_instance_tag_filters
        __props__["service_role_arn"] = service_role_arn
        __props__["trigger_configurations"] = trigger_configurations
        return DeploymentGroup(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

