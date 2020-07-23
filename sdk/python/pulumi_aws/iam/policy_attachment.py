# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['PolicyAttachment']


class PolicyAttachment(pulumi.CustomResource):
    groups: pulumi.Output[Optional[List[str]]] = pulumi.property("groups")
    """
    The group(s) the policy should be applied to
    """

    name: pulumi.Output[str] = pulumi.property("name")
    """
    The name of the attachment. This cannot be an empty string.
    """

    policy_arn: pulumi.Output[str] = pulumi.property("policyArn")
    """
    The ARN of the policy you want to apply
    """

    roles: pulumi.Output[Optional[List[str]]] = pulumi.property("roles")
    """
    The role(s) the policy should be applied to
    """

    users: pulumi.Output[Optional[List[str]]] = pulumi.property("users")
    """
    The user(s) the policy should be applied to
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 policy_arn: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 users: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Attaches a Managed IAM Policy to user(s), role(s), and/or group(s)

        !> **WARNING:** The iam.PolicyAttachment resource creates **exclusive** attachments of IAM policies. Across the entire AWS account, all of the users/roles/groups to which a single policy is attached must be declared by a single iam.PolicyAttachment resource. This means that even any users/roles/groups that have the attached policy via any other mechanism (including other resources managed by this provider) will have that attached policy revoked by this resource. Consider `iam.RolePolicyAttachment`, `iam.UserPolicyAttachment`, or `iam.GroupPolicyAttachment` instead. These resources do not enforce exclusive attachment of an IAM policy.

        > **NOTE:** The usage of this resource conflicts with the `iam.GroupPolicyAttachment`, `iam.RolePolicyAttachment`, and `iam.UserPolicyAttachment` resources and will permanently show a difference if both are defined.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        user = aws.iam.User("user")
        role = aws.iam.Role("role", assume_role_policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Principal": {
                "Service": "ec2.amazonaws.com"
              },
              "Effect": "Allow",
              "Sid": ""
            }
          ]
        }

        \"\"\")
        group = aws.iam.Group("group")
        policy = aws.iam.Policy("policy",
            description="A test policy",
            policy=\"\"\"{
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": [
                "ec2:Describe*"
              ],
              "Effect": "Allow",
              "Resource": "*"
            }
          ]
        }

        \"\"\")
        test_attach = aws.iam.PolicyAttachment("test-attach",
            groups=[group.name],
            policy_arn=policy.arn,
            roles=[role.name],
            users=[user.name])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] groups: The group(s) the policy should be applied to
        :param pulumi.Input[str] name: The name of the attachment. This cannot be an empty string.
        :param pulumi.Input[str] policy_arn: The ARN of the policy you want to apply
        :param pulumi.Input[List[pulumi.Input[str]]] roles: The role(s) the policy should be applied to
        :param pulumi.Input[List[pulumi.Input[str]]] users: The user(s) the policy should be applied to
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

            __props__['groups'] = groups
            __props__['name'] = name
            if policy_arn is None:
                raise TypeError("Missing required property 'policy_arn'")
            __props__['policy_arn'] = policy_arn
            __props__['roles'] = roles
            __props__['users'] = users
        super(PolicyAttachment, __self__).__init__(
            'aws:iam/policyAttachment:PolicyAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            groups: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            policy_arn: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            users: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None) -> 'PolicyAttachment':
        """
        Get an existing PolicyAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] groups: The group(s) the policy should be applied to
        :param pulumi.Input[str] name: The name of the attachment. This cannot be an empty string.
        :param pulumi.Input[str] policy_arn: The ARN of the policy you want to apply
        :param pulumi.Input[List[pulumi.Input[str]]] roles: The role(s) the policy should be applied to
        :param pulumi.Input[List[pulumi.Input[str]]] users: The user(s) the policy should be applied to
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["groups"] = groups
        __props__["name"] = name
        __props__["policy_arn"] = policy_arn
        __props__["roles"] = roles
        __props__["users"] = users
        return PolicyAttachment(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

