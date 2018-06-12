// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a [Route53 Delegation Set](https://docs.aws.amazon.com/Route53/latest/APIReference/actions-on-reusable-delegation-sets.html) resource.
type DelegationSet struct {
	s *pulumi.ResourceState
}

// NewDelegationSet registers a new resource with the given unique name, arguments, and options.
func NewDelegationSet(ctx *pulumi.Context,
	name string, args *DelegationSetArgs, opts ...pulumi.ResourceOpt) (*DelegationSet, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["referenceName"] = nil
	} else {
		inputs["referenceName"] = args.ReferenceName
	}
	inputs["nameServers"] = nil
	s, err := ctx.RegisterResource("aws:route53/delegationSet:DelegationSet", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DelegationSet{s: s}, nil
}

// GetDelegationSet gets an existing DelegationSet resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDelegationSet(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DelegationSetState, opts ...pulumi.ResourceOpt) (*DelegationSet, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["nameServers"] = state.NameServers
		inputs["referenceName"] = state.ReferenceName
	}
	s, err := ctx.ReadResource("aws:route53/delegationSet:DelegationSet", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &DelegationSet{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *DelegationSet) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *DelegationSet) ID() *pulumi.IDOutput {
	return r.s.ID
}

// A list of authoritative name servers for the hosted zone
// (effectively a list of NS records).
func (r *DelegationSet) NameServers() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["nameServers"])
}

// This is a reference name used in Caller Reference
// (helpful for identifying single delegation set amongst others)
func (r *DelegationSet) ReferenceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["referenceName"])
}

// Input properties used for looking up and filtering DelegationSet resources.
type DelegationSetState struct {
	// A list of authoritative name servers for the hosted zone
	// (effectively a list of NS records).
	NameServers interface{}
	// This is a reference name used in Caller Reference
	// (helpful for identifying single delegation set amongst others)
	ReferenceName interface{}
}

// The set of arguments for constructing a DelegationSet resource.
type DelegationSetArgs struct {
	// This is a reference name used in Caller Reference
	// (helpful for identifying single delegation set amongst others)
	ReferenceName interface{}
}