// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Glue resource policy. Only one can exist per region.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/glue"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/iam"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		currentCallerIdentity, err := aws.GetCallerIdentity(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		currentPartition, err := aws.GetPartition(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		currentRegion, err := aws.GetRegion(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		glue_example_policy, err := iam.GetPolicyDocument(ctx, &iam.GetPolicyDocumentArgs{
// 			Statements: []iam.GetPolicyDocumentStatement{
// 				iam.GetPolicyDocumentStatement{
// 					Actions: []string{
// 						"glue:CreateTable",
// 					},
// 					Resources: []string{
// 						fmt.Sprintf("%v%v%v%v%v%v%v", "arn:", currentPartition.Partition, ":glue:", currentRegion.Name, ":", currentCallerIdentity.AccountId, ":*"),
// 					},
// 					Principals: []iam.GetPolicyDocumentStatementPrincipal{
// 						iam.GetPolicyDocumentStatementPrincipal{
// 							Identifiers: []string{
// 								"*",
// 							},
// 							Type: "AWS",
// 						},
// 					},
// 				},
// 			},
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = glue.NewResourcePolicy(ctx, "example", &glue.ResourcePolicyArgs{
// 			Policy: pulumi.String(glue_example_policy.Json),
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
// Glue Resource Policy can be imported using the account ID
//
// ```sh
//  $ pulumi import aws:glue/resourcePolicy:ResourcePolicy Test 12356789012
// ```
type ResourcePolicy struct {
	pulumi.CustomResourceState

	// The policy to be applied to the aws glue data catalog.
	Policy pulumi.StringOutput `pulumi:"policy"`
}

// NewResourcePolicy registers a new resource with the given unique name, arguments, and options.
func NewResourcePolicy(ctx *pulumi.Context,
	name string, args *ResourcePolicyArgs, opts ...pulumi.ResourceOption) (*ResourcePolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	var resource ResourcePolicy
	err := ctx.RegisterResource("aws:glue/resourcePolicy:ResourcePolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourcePolicy gets an existing ResourcePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourcePolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourcePolicyState, opts ...pulumi.ResourceOption) (*ResourcePolicy, error) {
	var resource ResourcePolicy
	err := ctx.ReadResource("aws:glue/resourcePolicy:ResourcePolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourcePolicy resources.
type resourcePolicyState struct {
	// The policy to be applied to the aws glue data catalog.
	Policy *string `pulumi:"policy"`
}

type ResourcePolicyState struct {
	// The policy to be applied to the aws glue data catalog.
	Policy pulumi.StringPtrInput
}

func (ResourcePolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourcePolicyState)(nil)).Elem()
}

type resourcePolicyArgs struct {
	// The policy to be applied to the aws glue data catalog.
	Policy string `pulumi:"policy"`
}

// The set of arguments for constructing a ResourcePolicy resource.
type ResourcePolicyArgs struct {
	// The policy to be applied to the aws glue data catalog.
	Policy pulumi.StringInput
}

func (ResourcePolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourcePolicyArgs)(nil)).Elem()
}

type ResourcePolicyInput interface {
	pulumi.Input

	ToResourcePolicyOutput() ResourcePolicyOutput
	ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput
}

func (ResourcePolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourcePolicy)(nil)).Elem()
}

func (i ResourcePolicy) ToResourcePolicyOutput() ResourcePolicyOutput {
	return i.ToResourcePolicyOutputWithContext(context.Background())
}

func (i ResourcePolicy) ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourcePolicyOutput)
}

type ResourcePolicyOutput struct {
	*pulumi.OutputState
}

func (ResourcePolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourcePolicyOutput)(nil)).Elem()
}

func (o ResourcePolicyOutput) ToResourcePolicyOutput() ResourcePolicyOutput {
	return o
}

func (o ResourcePolicyOutput) ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ResourcePolicyOutput{})
}
