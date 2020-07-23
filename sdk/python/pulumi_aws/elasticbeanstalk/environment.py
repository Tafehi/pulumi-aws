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

__all__ = ['Environment']


class Environment(pulumi.CustomResource):
    all_settings: pulumi.Output[List['outputs.EnvironmentAllSetting']] = pulumi.property("allSettings")
    """
    List of all option settings configured in this Environment. These
    are a combination of default settings and their overrides from `setting` in
    the configuration.
    """

    application: pulumi.Output[str] = pulumi.property("application")
    """
    Name of the application that contains the version
    to be deployed
    """

    arn: pulumi.Output[str] = pulumi.property("arn")

    autoscaling_groups: pulumi.Output[List[str]] = pulumi.property("autoscalingGroups")
    """
    The autoscaling groups used by this Environment.
    """

    cname: pulumi.Output[str] = pulumi.property("cname")
    """
    Fully qualified DNS name for this Environment.
    """

    cname_prefix: pulumi.Output[str] = pulumi.property("cnamePrefix")
    """
    Prefix to use for the fully qualified DNS name of
    the Environment.
    """

    description: pulumi.Output[Optional[str]] = pulumi.property("description")
    """
    Short description of the Environment
    """

    endpoint_url: pulumi.Output[str] = pulumi.property("endpointUrl")
    """
    The URL to the Load Balancer for this Environment
    """

    instances: pulumi.Output[List[str]] = pulumi.property("instances")
    """
    Instances used by this Environment.
    """

    launch_configurations: pulumi.Output[List[str]] = pulumi.property("launchConfigurations")
    """
    Launch configurations in use by this Environment.
    """

    load_balancers: pulumi.Output[List[str]] = pulumi.property("loadBalancers")
    """
    Elastic load balancers in use by this Environment.
    """

    name: pulumi.Output[str] = pulumi.property("name")
    """
    A unique name for this Environment. This name is used
    in the application URL
    """

    platform_arn: pulumi.Output[str] = pulumi.property("platformArn")
    """
    The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Elastic Beanstalk [Platform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn)
    to use in deployment
    """

    poll_interval: pulumi.Output[Optional[str]] = pulumi.property("pollInterval")
    """
    The time between polling the AWS API to
    check if changes have been applied. Use this to adjust the rate of API calls
    for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
    use the default behavior, which is an exponential backoff
    """

    queues: pulumi.Output[List[str]] = pulumi.property("queues")
    """
    SQS queues in use by this Environment.
    """

    settings: pulumi.Output[Optional[List['outputs.EnvironmentSetting']]] = pulumi.property("settings")
    """
    Option settings to configure the new Environment. These
    override specific values that are set as defaults. The format is detailed
    below in Option Settings
    """

    solution_stack_name: pulumi.Output[str] = pulumi.property("solutionStackName")
    """
    A solution stack to base your environment
    off of. Example stacks can be found in the [Amazon API documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html)
    """

    tags: pulumi.Output[Optional[Mapping[str, str]]] = pulumi.property("tags")
    """
    A set of tags to apply to the Environment.
    """

    template_name: pulumi.Output[Optional[str]] = pulumi.property("templateName")
    """
    The name of the Elastic Beanstalk Configuration
    template to use in deployment
    """

    tier: pulumi.Output[Optional[str]] = pulumi.property("tier")
    """
    Elastic Beanstalk Environment tier. Valid values are `Worker`
    or `WebServer`. If tier is left blank `WebServer` will be used.
    """

    triggers: pulumi.Output[List[str]] = pulumi.property("triggers")
    """
    Autoscaling triggers in use by this Environment.
    """

    version: pulumi.Output[str] = pulumi.property("version")
    """
    The name of the Elastic Beanstalk Application Version
    to use in deployment.
    """

    wait_for_ready_timeout: pulumi.Output[Optional[str]] = pulumi.property("waitForReadyTimeout")
    """
    The maximum
    [duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
    wait for an Elastic Beanstalk Environment to be in a ready state before timing
    out.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application: Optional[pulumi.Input[str]] = None,
                 cname_prefix: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 platform_arn: Optional[pulumi.Input[str]] = None,
                 poll_interval: Optional[pulumi.Input[str]] = None,
                 settings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentSettingArgs']]]]] = None,
                 solution_stack_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 tier: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 wait_for_ready_timeout: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
        you to deploy and manage applications in the AWS cloud without worrying about
        the infrastructure that runs those applications.

        Environments are often things such as `development`, `integration`, or
        `production`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        tftest = aws.elasticbeanstalk.Application("tftest", description="tf-test-desc")
        tfenvtest = aws.elasticbeanstalk.Environment("tfenvtest",
            application=tftest.name,
            solution_stack_name="64bit Amazon Linux 2015.03 v2.0.3 running Go 1.4")
        ```
        ## Option Settings

        Some options can be stack-specific, check [AWS Docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html)
        for supported options and examples.

        The `setting` and `all_settings` mappings support the following format:

        * `namespace` - unique namespace identifying the option's associated AWS resource
        * `name` - name of the configuration option
        * `value` - value for the configuration option
        * `resource` - (Optional) resource name for [scheduled action](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction)

        ### Example With Options

        ```python
        import pulumi
        import pulumi_aws as aws

        tftest = aws.elasticbeanstalk.Application("tftest", description="tf-test-desc")
        tfenvtest = aws.elasticbeanstalk.Environment("tfenvtest",
            application=tftest.name,
            settings=[
                {
                    "name": "VPCId",
                    "namespace": "aws:ec2:vpc",
                    "value": "vpc-xxxxxxxx",
                },
                {
                    "name": "Subnets",
                    "namespace": "aws:ec2:vpc",
                    "value": "subnet-xxxxxxxx",
                },
            ],
            solution_stack_name="64bit Amazon Linux 2015.03 v2.0.3 running Go 1.4")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application: Name of the application that contains the version
               to be deployed
        :param pulumi.Input[str] cname_prefix: Prefix to use for the fully qualified DNS name of
               the Environment.
        :param pulumi.Input[str] description: Short description of the Environment
        :param pulumi.Input[str] name: A unique name for this Environment. This name is used
               in the application URL
        :param pulumi.Input[str] platform_arn: The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Elastic Beanstalk [Platform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn)
               to use in deployment
        :param pulumi.Input[str] poll_interval: The time between polling the AWS API to
               check if changes have been applied. Use this to adjust the rate of API calls
               for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
               use the default behavior, which is an exponential backoff
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentSettingArgs']]]] settings: Option settings to configure the new Environment. These
               override specific values that are set as defaults. The format is detailed
               below in Option Settings
        :param pulumi.Input[str] solution_stack_name: A solution stack to base your environment
               off of. Example stacks can be found in the [Amazon API documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A set of tags to apply to the Environment.
        :param pulumi.Input[str] template_name: The name of the Elastic Beanstalk Configuration
               template to use in deployment
        :param pulumi.Input[str] tier: Elastic Beanstalk Environment tier. Valid values are `Worker`
               or `WebServer`. If tier is left blank `WebServer` will be used.
        :param pulumi.Input[str] version: The name of the Elastic Beanstalk Application Version
               to use in deployment.
        :param pulumi.Input[str] wait_for_ready_timeout: The maximum
               [duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
               wait for an Elastic Beanstalk Environment to be in a ready state before timing
               out.
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

            if application is None:
                raise TypeError("Missing required property 'application'")
            __props__['application'] = application
            __props__['cname_prefix'] = cname_prefix
            __props__['description'] = description
            __props__['name'] = name
            __props__['platform_arn'] = platform_arn
            __props__['poll_interval'] = poll_interval
            __props__['settings'] = settings
            __props__['solution_stack_name'] = solution_stack_name
            __props__['tags'] = tags
            __props__['template_name'] = template_name
            __props__['tier'] = tier
            __props__['version'] = version
            __props__['wait_for_ready_timeout'] = wait_for_ready_timeout
            __props__['all_settings'] = None
            __props__['arn'] = None
            __props__['autoscaling_groups'] = None
            __props__['cname'] = None
            __props__['endpoint_url'] = None
            __props__['instances'] = None
            __props__['launch_configurations'] = None
            __props__['load_balancers'] = None
            __props__['queues'] = None
            __props__['triggers'] = None
        super(Environment, __self__).__init__(
            'aws:elasticbeanstalk/environment:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            all_settings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentAllSettingArgs']]]]] = None,
            application: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            autoscaling_groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            cname: Optional[pulumi.Input[str]] = None,
            cname_prefix: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            endpoint_url: Optional[pulumi.Input[str]] = None,
            instances: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            launch_configurations: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            load_balancers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            platform_arn: Optional[pulumi.Input[str]] = None,
            poll_interval: Optional[pulumi.Input[str]] = None,
            queues: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            settings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentSettingArgs']]]]] = None,
            solution_stack_name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            template_name: Optional[pulumi.Input[str]] = None,
            tier: Optional[pulumi.Input[str]] = None,
            triggers: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            version: Optional[pulumi.Input[str]] = None,
            wait_for_ready_timeout: Optional[pulumi.Input[str]] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentAllSettingArgs']]]] all_settings: List of all option settings configured in this Environment. These
               are a combination of default settings and their overrides from `setting` in
               the configuration.
        :param pulumi.Input[str] application: Name of the application that contains the version
               to be deployed
        :param pulumi.Input[List[pulumi.Input[str]]] autoscaling_groups: The autoscaling groups used by this Environment.
        :param pulumi.Input[str] cname: Fully qualified DNS name for this Environment.
        :param pulumi.Input[str] cname_prefix: Prefix to use for the fully qualified DNS name of
               the Environment.
        :param pulumi.Input[str] description: Short description of the Environment
        :param pulumi.Input[str] endpoint_url: The URL to the Load Balancer for this Environment
        :param pulumi.Input[List[pulumi.Input[str]]] instances: Instances used by this Environment.
        :param pulumi.Input[List[pulumi.Input[str]]] launch_configurations: Launch configurations in use by this Environment.
        :param pulumi.Input[List[pulumi.Input[str]]] load_balancers: Elastic load balancers in use by this Environment.
        :param pulumi.Input[str] name: A unique name for this Environment. This name is used
               in the application URL
        :param pulumi.Input[str] platform_arn: The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Elastic Beanstalk [Platform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html#cfn-beanstalk-environment-platformarn)
               to use in deployment
        :param pulumi.Input[str] poll_interval: The time between polling the AWS API to
               check if changes have been applied. Use this to adjust the rate of API calls
               for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
               use the default behavior, which is an exponential backoff
        :param pulumi.Input[List[pulumi.Input[str]]] queues: SQS queues in use by this Environment.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['EnvironmentSettingArgs']]]] settings: Option settings to configure the new Environment. These
               override specific values that are set as defaults. The format is detailed
               below in Option Settings
        :param pulumi.Input[str] solution_stack_name: A solution stack to base your environment
               off of. Example stacks can be found in the [Amazon API documentation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html)
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A set of tags to apply to the Environment.
        :param pulumi.Input[str] template_name: The name of the Elastic Beanstalk Configuration
               template to use in deployment
        :param pulumi.Input[str] tier: Elastic Beanstalk Environment tier. Valid values are `Worker`
               or `WebServer`. If tier is left blank `WebServer` will be used.
        :param pulumi.Input[List[pulumi.Input[str]]] triggers: Autoscaling triggers in use by this Environment.
        :param pulumi.Input[str] version: The name of the Elastic Beanstalk Application Version
               to use in deployment.
        :param pulumi.Input[str] wait_for_ready_timeout: The maximum
               [duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
               wait for an Elastic Beanstalk Environment to be in a ready state before timing
               out.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["all_settings"] = all_settings
        __props__["application"] = application
        __props__["arn"] = arn
        __props__["autoscaling_groups"] = autoscaling_groups
        __props__["cname"] = cname
        __props__["cname_prefix"] = cname_prefix
        __props__["description"] = description
        __props__["endpoint_url"] = endpoint_url
        __props__["instances"] = instances
        __props__["launch_configurations"] = launch_configurations
        __props__["load_balancers"] = load_balancers
        __props__["name"] = name
        __props__["platform_arn"] = platform_arn
        __props__["poll_interval"] = poll_interval
        __props__["queues"] = queues
        __props__["settings"] = settings
        __props__["solution_stack_name"] = solution_stack_name
        __props__["tags"] = tags
        __props__["template_name"] = template_name
        __props__["tier"] = tier
        __props__["triggers"] = triggers
        __props__["version"] = version
        __props__["wait_for_ready_timeout"] = wait_for_ready_timeout
        return Environment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

