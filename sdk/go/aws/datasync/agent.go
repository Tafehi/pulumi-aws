// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package datasync

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an AWS DataSync Agent deployed on premises.
// 
// > **NOTE:** One of `activation_key` or `ip_address` must be provided for resource creation (agent activation). Neither is required for resource import. If using `ip_address`, Terraform must be able to make an HTTP (port 80) GET request to the specified IP address from where it is running. The agent will turn off that HTTP server after activation.
type Agent struct {
	s *pulumi.ResourceState
}

// NewAgent registers a new resource with the given unique name, arguments, and options.
func NewAgent(ctx *pulumi.Context,
	name string, args *AgentArgs, opts ...pulumi.ResourceOpt) (*Agent, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["activationKey"] = nil
		inputs["ipAddress"] = nil
		inputs["name"] = nil
		inputs["tags"] = nil
	} else {
		inputs["activationKey"] = args.ActivationKey
		inputs["ipAddress"] = args.IpAddress
		inputs["name"] = args.Name
		inputs["tags"] = args.Tags
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:datasync/agent:Agent", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Agent{s: s}, nil
}

// GetAgent gets an existing Agent resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAgent(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AgentState, opts ...pulumi.ResourceOpt) (*Agent, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["activationKey"] = state.ActivationKey
		inputs["arn"] = state.Arn
		inputs["ipAddress"] = state.IpAddress
		inputs["name"] = state.Name
		inputs["tags"] = state.Tags
	}
	s, err := ctx.ReadResource("aws:datasync/agent:Agent", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Agent{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Agent) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Agent) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
func (r *Agent) ActivationKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["activationKey"])
}

// Amazon Resource Name (ARN) of the DataSync Agent.
func (r *Agent) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
func (r *Agent) IpAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["ipAddress"])
}

// Name of the DataSync Agent.
func (r *Agent) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Key-value pairs of resource tags to assign to the DataSync Agent.
func (r *Agent) Tags() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["tags"])
}

// Input properties used for looking up and filtering Agent resources.
type AgentState struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
	ActivationKey interface{}
	// Amazon Resource Name (ARN) of the DataSync Agent.
	Arn interface{}
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
	IpAddress interface{}
	// Name of the DataSync Agent.
	Name interface{}
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags interface{}
}

// The set of arguments for constructing a Agent resource.
type AgentArgs struct {
	// DataSync Agent activation key during resource creation. Conflicts with `ip_address`. If an `ip_address` is provided instead, Terraform will retrieve the `activation_key` as part of the resource creation.
	ActivationKey interface{}
	// DataSync Agent IP address to retrieve activation key during resource creation. Conflicts with `activation_key`. DataSync Agent must be accessible on port 80 from where Terraform is running.
	IpAddress interface{}
	// Name of the DataSync Agent.
	Name interface{}
	// Key-value pairs of resource tags to assign to the DataSync Agent.
	Tags interface{}
}