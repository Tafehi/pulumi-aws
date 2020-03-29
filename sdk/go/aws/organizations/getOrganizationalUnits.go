// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package organizations

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Get all direct child organizational units under a parent organizational unit. This only provides immediate children, not all children.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/organizations_organizational_units.html.markdown.
func GetOrganizationalUnits(ctx *pulumi.Context, args *GetOrganizationalUnitsArgs, opts ...pulumi.InvokeOption) (*GetOrganizationalUnitsResult, error) {
	var rv GetOrganizationalUnitsResult
	err := ctx.Invoke("aws:organizations/getOrganizationalUnits:getOrganizationalUnits", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getOrganizationalUnits.
type GetOrganizationalUnitsArgs struct {
	// The parent ID of the organizational unit.
	ParentId string `pulumi:"parentId"`
}

// A collection of values returned by getOrganizationalUnits.
type GetOrganizationalUnitsResult struct {
	// List of child organizational units, which have the following attributes:
	Childrens []GetOrganizationalUnitsChildren `pulumi:"childrens"`
	// id is the provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	ParentId string `pulumi:"parentId"`
}