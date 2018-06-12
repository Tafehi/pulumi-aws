# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Broker(pulumi.CustomResource):
    """
    Provides an MQ Broker Resource. This resources also manages users for the broker.
    
    For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).
    
    Changes to an MQ Broker can occur when you change a
    parameter, such as `configuration` or `user`, and are reflected in the next maintenance
    window. Because of this, Terraform may report a difference in its planning
    phase because a modification has not yet taken place. You can use the
    `apply_immediately` flag to instruct the service to apply the change immediately
    (see documentation below).
    
    ~> **Note:** using `apply_immediately` can result in a
    brief downtime as the broker reboots.
    
    ~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, apply_immediately=None, auto_minor_version_upgrade=None, broker_name=None, configuration=None, deployment_mode=None, engine_type=None, engine_version=None, host_instance_type=None, maintenance_window_start_time=None, publicly_accessible=None, security_groups=None, subnet_ids=None, users=None):
        """Create a Broker resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if apply_immediately and not isinstance(apply_immediately, bool):
            raise TypeError('Expected property apply_immediately to be a bool')
        __self__.apply_immediately = apply_immediately
        """
        Specifies whether any broker modifications
        are applied immediately, or during the next maintenance window. Default is `false`.
        """
        __props__['applyImmediately'] = apply_immediately

        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError('Expected property auto_minor_version_upgrade to be a bool')
        __self__.auto_minor_version_upgrade = auto_minor_version_upgrade
        """
        Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
        """
        __props__['autoMinorVersionUpgrade'] = auto_minor_version_upgrade

        if not broker_name:
            raise TypeError('Missing required property broker_name')
        elif not isinstance(broker_name, basestring):
            raise TypeError('Expected property broker_name to be a basestring')
        __self__.broker_name = broker_name
        """
        The name of the broker.
        """
        __props__['brokerName'] = broker_name

        if configuration and not isinstance(configuration, dict):
            raise TypeError('Expected property configuration to be a dict')
        __self__.configuration = configuration
        """
        Configuration of the broker. See below.
        """
        __props__['configuration'] = configuration

        if deployment_mode and not isinstance(deployment_mode, basestring):
            raise TypeError('Expected property deployment_mode to be a basestring')
        __self__.deployment_mode = deployment_mode
        """
        The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
        """
        __props__['deploymentMode'] = deployment_mode

        if not engine_type:
            raise TypeError('Missing required property engine_type')
        elif not isinstance(engine_type, basestring):
            raise TypeError('Expected property engine_type to be a basestring')
        __self__.engine_type = engine_type
        """
        The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
        """
        __props__['engineType'] = engine_type

        if not engine_version:
            raise TypeError('Missing required property engine_version')
        elif not isinstance(engine_version, basestring):
            raise TypeError('Expected property engine_version to be a basestring')
        __self__.engine_version = engine_version
        """
        The version of the broker engine. Currently, Amazon MQ supports only `5.15.0`.
        """
        __props__['engineVersion'] = engine_version

        if not host_instance_type:
            raise TypeError('Missing required property host_instance_type')
        elif not isinstance(host_instance_type, basestring):
            raise TypeError('Expected property host_instance_type to be a basestring')
        __self__.host_instance_type = host_instance_type
        """
        The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`
        """
        __props__['hostInstanceType'] = host_instance_type

        if maintenance_window_start_time and not isinstance(maintenance_window_start_time, dict):
            raise TypeError('Expected property maintenance_window_start_time to be a dict')
        __self__.maintenance_window_start_time = maintenance_window_start_time
        """
        Maintenance window start time. See below.
        """
        __props__['maintenanceWindowStartTime'] = maintenance_window_start_time

        if publicly_accessible and not isinstance(publicly_accessible, bool):
            raise TypeError('Expected property publicly_accessible to be a bool')
        __self__.publicly_accessible = publicly_accessible
        """
        Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.
        """
        __props__['publiclyAccessible'] = publicly_accessible

        if not security_groups:
            raise TypeError('Missing required property security_groups')
        elif not isinstance(security_groups, list):
            raise TypeError('Expected property security_groups to be a list')
        __self__.security_groups = security_groups
        """
        The list of security group IDs assigned to the broker.
        """
        __props__['securityGroups'] = security_groups

        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError('Expected property subnet_ids to be a list')
        __self__.subnet_ids = subnet_ids
        """
        The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
        """
        __props__['subnetIds'] = subnet_ids

        if not users:
            raise TypeError('Missing required property users')
        elif not isinstance(users, list):
            raise TypeError('Expected property users to be a list')
        __self__.users = users
        """
        The list of all ActiveMQ usernames for the specified broker. See below.
        """
        __props__['users'] = users

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN of the broker.
        """
        __self__.instances = pulumi.runtime.UNKNOWN
        """
        A list of information about allocated brokers (both active & standby).
        * `instances.0.console_url` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
        * `instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):
        * `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
        * `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
        * `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
        * `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
        * `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
        """

        super(Broker, __self__).__init__(
            'aws:mq/broker:Broker',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'applyImmediately' in outs:
            self.apply_immediately = outs['applyImmediately']
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'autoMinorVersionUpgrade' in outs:
            self.auto_minor_version_upgrade = outs['autoMinorVersionUpgrade']
        if 'brokerName' in outs:
            self.broker_name = outs['brokerName']
        if 'configuration' in outs:
            self.configuration = outs['configuration']
        if 'deploymentMode' in outs:
            self.deployment_mode = outs['deploymentMode']
        if 'engineType' in outs:
            self.engine_type = outs['engineType']
        if 'engineVersion' in outs:
            self.engine_version = outs['engineVersion']
        if 'hostInstanceType' in outs:
            self.host_instance_type = outs['hostInstanceType']
        if 'instances' in outs:
            self.instances = outs['instances']
        if 'maintenanceWindowStartTime' in outs:
            self.maintenance_window_start_time = outs['maintenanceWindowStartTime']
        if 'publiclyAccessible' in outs:
            self.publicly_accessible = outs['publiclyAccessible']
        if 'securityGroups' in outs:
            self.security_groups = outs['securityGroups']
        if 'subnetIds' in outs:
            self.subnet_ids = outs['subnetIds']
        if 'users' in outs:
            self.users = outs['users']