// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package acm

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This resource represents a successful validation of an ACM certificate in concert
// with other resources.
// 
// Most commonly, this resource is used together with `aws_route53_record` and
// `aws_acm_certificate` to request a DNS validated certificate,
// deploy the required validation records and wait for validation to complete.
// 
// > **WARNING:** This resource implements a part of the validation workflow. It does not represent a real-world entity in AWS, therefore changing or deleting this resource on its own has no immediate effect.
// 
type CertificateValidation struct {
	s *pulumi.ResourceState
}

// NewCertificateValidation registers a new resource with the given unique name, arguments, and options.
func NewCertificateValidation(ctx *pulumi.Context,
	name string, args *CertificateValidationArgs, opts ...pulumi.ResourceOpt) (*CertificateValidation, error) {
	if args == nil || args.CertificateArn == nil {
		return nil, errors.New("missing required argument 'CertificateArn'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["certificateArn"] = nil
		inputs["validationRecordFqdns"] = nil
	} else {
		inputs["certificateArn"] = args.CertificateArn
		inputs["validationRecordFqdns"] = args.ValidationRecordFqdns
	}
	s, err := ctx.RegisterResource("aws:acm/certificateValidation:CertificateValidation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &CertificateValidation{s: s}, nil
}

// GetCertificateValidation gets an existing CertificateValidation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificateValidation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *CertificateValidationState, opts ...pulumi.ResourceOpt) (*CertificateValidation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["certificateArn"] = state.CertificateArn
		inputs["validationRecordFqdns"] = state.ValidationRecordFqdns
	}
	s, err := ctx.ReadResource("aws:acm/certificateValidation:CertificateValidation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &CertificateValidation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *CertificateValidation) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *CertificateValidation) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the certificate that is being validated.
func (r *CertificateValidation) CertificateArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateArn"])
}

// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
func (r *CertificateValidation) ValidationRecordFqdns() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["validationRecordFqdns"])
}

// Input properties used for looking up and filtering CertificateValidation resources.
type CertificateValidationState struct {
	// The ARN of the certificate that is being validated.
	CertificateArn interface{}
	// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
	ValidationRecordFqdns interface{}
}

// The set of arguments for constructing a CertificateValidation resource.
type CertificateValidationArgs struct {
	// The ARN of the certificate that is being validated.
	CertificateArn interface{}
	// List of FQDNs that implement the validation. Only valid for DNS validation method ACM certificates. If this is set, the resource can implement additional sanity checks and has an explicit dependency on the resource that is implementing the validation
	ValidationRecordFqdns interface{}
}
