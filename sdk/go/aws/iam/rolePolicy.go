// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides an IAM role inline policy.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		testRole, err := iam.NewRole(ctx, "testRole", &iam.RoleArgs{
// 			AssumeRolePolicy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"Version\": \"2012-10-17\",\n", "  \"Statement\": [\n", "    {\n", "      \"Action\": \"sts:AssumeRole\",\n", "      \"Principal\": {\n", "        \"Service\": \"ec2.amazonaws.com\"\n", "      },\n", "      \"Effect\": \"Allow\",\n", "      \"Sid\": \"\"\n", "    }\n", "  ]\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = iam.NewRolePolicy(ctx, "testPolicy", &iam.RolePolicyArgs{
// 			Role:   testRole.ID(),
// 			Policy: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"Version\": \"2012-10-17\",\n", "  \"Statement\": [\n", "    {\n", "      \"Action\": [\n", "        \"ec2:Describe*\"\n", "      ],\n", "      \"Effect\": \"Allow\",\n", "      \"Resource\": \"*\"\n", "    }\n", "  ]\n", "}\n")),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// IAM Role Policies can be imported using the `role_name:role_policy_name`, e.g.
//
// ```sh
//  $ pulumi import aws:iam/rolePolicy:RolePolicy mypolicy role_of_mypolicy_name:mypolicy_name
// ```
type RolePolicy struct {
	pulumi.CustomResourceState

	// The name of the role policy. If omitted, this provider will
	// assign a random, unique name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy pulumi.StringOutput `pulumi:"policy"`
	// The IAM role to attach to the policy.
	Role pulumi.StringOutput `pulumi:"role"`
}

// NewRolePolicy registers a new resource with the given unique name, arguments, and options.
func NewRolePolicy(ctx *pulumi.Context,
	name string, args *RolePolicyArgs, opts ...pulumi.ResourceOption) (*RolePolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	var resource RolePolicy
	err := ctx.RegisterResource("aws:iam/rolePolicy:RolePolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRolePolicy gets an existing RolePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRolePolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RolePolicyState, opts ...pulumi.ResourceOption) (*RolePolicy, error) {
	var resource RolePolicy
	err := ctx.ReadResource("aws:iam/rolePolicy:RolePolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RolePolicy resources.
type rolePolicyState struct {
	// The name of the role policy. If omitted, this provider will
	// assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy *string `pulumi:"policy"`
	// The IAM role to attach to the policy.
	Role *string `pulumi:"role"`
}

type RolePolicyState struct {
	// The name of the role policy. If omitted, this provider will
	// assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The policy document. This is a JSON formatted string.
	Policy pulumi.StringPtrInput
	// The IAM role to attach to the policy.
	Role pulumi.StringPtrInput
}

func (RolePolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*rolePolicyState)(nil)).Elem()
}

type rolePolicyArgs struct {
	// The name of the role policy. If omitted, this provider will
	// assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// The policy document. This is a JSON formatted string.
	Policy interface{} `pulumi:"policy"`
	// The IAM role to attach to the policy.
	Role interface{} `pulumi:"role"`
}

// The set of arguments for constructing a RolePolicy resource.
type RolePolicyArgs struct {
	// The name of the role policy. If omitted, this provider will
	// assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// The policy document. This is a JSON formatted string.
	Policy pulumi.Input
	// The IAM role to attach to the policy.
	Role pulumi.Input
}

func (RolePolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*rolePolicyArgs)(nil)).Elem()
}

type RolePolicyInput interface {
	pulumi.Input

	ToRolePolicyOutput() RolePolicyOutput
	ToRolePolicyOutputWithContext(ctx context.Context) RolePolicyOutput
}

func (RolePolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*RolePolicy)(nil)).Elem()
}

func (i RolePolicy) ToRolePolicyOutput() RolePolicyOutput {
	return i.ToRolePolicyOutputWithContext(context.Background())
}

func (i RolePolicy) ToRolePolicyOutputWithContext(ctx context.Context) RolePolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RolePolicyOutput)
}

type RolePolicyOutput struct {
	*pulumi.OutputState
}

func (RolePolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RolePolicyOutput)(nil)).Elem()
}

func (o RolePolicyOutput) ToRolePolicyOutput() RolePolicyOutput {
	return o
}

func (o RolePolicyOutput) ToRolePolicyOutputWithContext(ctx context.Context) RolePolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RolePolicyOutput{})
}
