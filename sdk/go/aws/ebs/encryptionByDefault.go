// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ebs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage whether default EBS encryption is enabled for your AWS account in the current AWS region. To manage the default KMS key for the region, see the `ebs.DefaultKmsKey` resource.
//
// > **NOTE:** Removing this resource disables default EBS encryption.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ebs"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := ebs.NewEncryptionByDefault(ctx, "example", &ebs.EncryptionByDefaultArgs{
// 			Enabled: pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type EncryptionByDefault struct {
	pulumi.CustomResourceState

	// Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
}

// NewEncryptionByDefault registers a new resource with the given unique name, arguments, and options.
func NewEncryptionByDefault(ctx *pulumi.Context,
	name string, args *EncryptionByDefaultArgs, opts ...pulumi.ResourceOption) (*EncryptionByDefault, error) {
	if args == nil {
		args = &EncryptionByDefaultArgs{}
	}

	var resource EncryptionByDefault
	err := ctx.RegisterResource("aws:ebs/encryptionByDefault:EncryptionByDefault", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEncryptionByDefault gets an existing EncryptionByDefault resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEncryptionByDefault(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EncryptionByDefaultState, opts ...pulumi.ResourceOption) (*EncryptionByDefault, error) {
	var resource EncryptionByDefault
	err := ctx.ReadResource("aws:ebs/encryptionByDefault:EncryptionByDefault", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EncryptionByDefault resources.
type encryptionByDefaultState struct {
	// Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
}

type EncryptionByDefaultState struct {
	// Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
}

func (EncryptionByDefaultState) ElementType() reflect.Type {
	return reflect.TypeOf((*encryptionByDefaultState)(nil)).Elem()
}

type encryptionByDefaultArgs struct {
	// Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.
	Enabled *bool `pulumi:"enabled"`
}

// The set of arguments for constructing a EncryptionByDefault resource.
type EncryptionByDefaultArgs struct {
	// Whether or not default EBS encryption is enabled. Valid values are `true` or `false`. Defaults to `true`.
	Enabled pulumi.BoolPtrInput
}

func (EncryptionByDefaultArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*encryptionByDefaultArgs)(nil)).Elem()
}

type EncryptionByDefaultInput interface {
	pulumi.Input

	ToEncryptionByDefaultOutput() EncryptionByDefaultOutput
	ToEncryptionByDefaultOutputWithContext(ctx context.Context) EncryptionByDefaultOutput
}

func (EncryptionByDefault) ElementType() reflect.Type {
	return reflect.TypeOf((*EncryptionByDefault)(nil)).Elem()
}

func (i EncryptionByDefault) ToEncryptionByDefaultOutput() EncryptionByDefaultOutput {
	return i.ToEncryptionByDefaultOutputWithContext(context.Background())
}

func (i EncryptionByDefault) ToEncryptionByDefaultOutputWithContext(ctx context.Context) EncryptionByDefaultOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EncryptionByDefaultOutput)
}

type EncryptionByDefaultOutput struct {
	*pulumi.OutputState
}

func (EncryptionByDefaultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EncryptionByDefaultOutput)(nil)).Elem()
}

func (o EncryptionByDefaultOutput) ToEncryptionByDefaultOutput() EncryptionByDefaultOutput {
	return o
}

func (o EncryptionByDefaultOutput) ToEncryptionByDefaultOutputWithContext(ctx context.Context) EncryptionByDefaultOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EncryptionByDefaultOutput{})
}
