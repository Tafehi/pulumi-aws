// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a CloudWatch Log Group resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/cloudwatch"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := cloudwatch.NewLogGroup(ctx, "yada", &cloudwatch.LogGroupArgs{
// 			Tags: pulumi.StringMap{
// 				"Application": pulumi.String("serviceA"),
// 				"Environment": pulumi.String("production"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type LogGroup struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) specifying the log group. Any `:*` suffix added by the API, denoting all CloudWatch Log Streams under the CloudWatch Log Group, is removed for greater compatibility with other AWS services that do not accept the suffix.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// The name of the log group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringOutput `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrOutput `pulumi:"namePrefix"`
	// Specifies the number of days
	// you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
	// If you select 0, the events in the log group are always retained and never expire.
	RetentionInDays pulumi.IntPtrOutput `pulumi:"retentionInDays"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewLogGroup registers a new resource with the given unique name, arguments, and options.
func NewLogGroup(ctx *pulumi.Context,
	name string, args *LogGroupArgs, opts ...pulumi.ResourceOption) (*LogGroup, error) {
	if args == nil {
		args = &LogGroupArgs{}
	}
	var resource LogGroup
	err := ctx.RegisterResource("aws:cloudwatch/logGroup:LogGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogGroup gets an existing LogGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogGroupState, opts ...pulumi.ResourceOption) (*LogGroup, error) {
	var resource LogGroup
	err := ctx.ReadResource("aws:cloudwatch/logGroup:LogGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogGroup resources.
type logGroupState struct {
	// The Amazon Resource Name (ARN) specifying the log group. Any `:*` suffix added by the API, denoting all CloudWatch Log Streams under the CloudWatch Log Group, is removed for greater compatibility with other AWS services that do not accept the suffix.
	Arn *string `pulumi:"arn"`
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// The name of the log group. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// Specifies the number of days
	// you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
	// If you select 0, the events in the log group are always retained and never expire.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type LogGroupState struct {
	// The Amazon Resource Name (ARN) specifying the log group. Any `:*` suffix added by the API, denoting all CloudWatch Log Streams under the CloudWatch Log Group, is removed for greater compatibility with other AWS services that do not accept the suffix.
	Arn pulumi.StringPtrInput
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId pulumi.StringPtrInput
	// The name of the log group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// Specifies the number of days
	// you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
	// If you select 0, the events in the log group are always retained and never expire.
	RetentionInDays pulumi.IntPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (LogGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*logGroupState)(nil)).Elem()
}

type logGroupArgs struct {
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// The name of the log group. If omitted, this provider will assign a random, unique name.
	Name *string `pulumi:"name"`
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix *string `pulumi:"namePrefix"`
	// Specifies the number of days
	// you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
	// If you select 0, the events in the log group are always retained and never expire.
	RetentionInDays *int `pulumi:"retentionInDays"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a LogGroup resource.
type LogGroupArgs struct {
	// The ARN of the KMS Key to use when encrypting log data. Please note, after the AWS KMS CMK is disassociated from the log group,
	// AWS CloudWatch Logs stops encrypting newly ingested data for the log group. All previously ingested data remains encrypted, and AWS CloudWatch Logs requires
	// permissions for the CMK whenever the encrypted data is requested.
	KmsKeyId pulumi.StringPtrInput
	// The name of the log group. If omitted, this provider will assign a random, unique name.
	Name pulumi.StringPtrInput
	// Creates a unique name beginning with the specified prefix. Conflicts with `name`.
	NamePrefix pulumi.StringPtrInput
	// Specifies the number of days
	// you want to retain log events in the specified log group.  Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 3653, and 0.
	// If you select 0, the events in the log group are always retained and never expire.
	RetentionInDays pulumi.IntPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (LogGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logGroupArgs)(nil)).Elem()
}
