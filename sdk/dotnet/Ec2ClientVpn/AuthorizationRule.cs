// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2ClientVpn
{
    /// <summary>
    /// Provides authorization rules for AWS Client VPN endpoints. For more information on usage, please see the
    /// [AWS Client VPN Administrator's Guide](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var example = new Aws.Ec2ClientVpn.AuthorizationRule("example", new Aws.Ec2ClientVpn.AuthorizationRuleArgs
    ///         {
    ///             AuthorizeAllGroups = true,
    ///             ClientVpnEndpointId = aws_ec2_client_vpn_endpoint.Example.Id,
    ///             TargetNetworkCidr = aws_subnet.Example.Cidr_block,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class AuthorizationRule : Pulumi.CustomResource
    {
        /// <summary>
        /// The ID of the group to which the authorization rule grants access. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Output("accessGroupId")]
        public Output<string?> AccessGroupId { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the authorization rule grants access to all clients. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Output("authorizeAllGroups")]
        public Output<bool?> AuthorizeAllGroups { get; private set; } = null!;

        /// <summary>
        /// The ID of the Client VPN endpoint.
        /// </summary>
        [Output("clientVpnEndpointId")]
        public Output<string> ClientVpnEndpointId { get; private set; } = null!;

        /// <summary>
        /// A brief description of the authorization rule.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.
        /// </summary>
        [Output("targetNetworkCidr")]
        public Output<string> TargetNetworkCidr { get; private set; } = null!;


        /// <summary>
        /// Create a AuthorizationRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AuthorizationRule(string name, AuthorizationRuleArgs args, CustomResourceOptions? options = null)
            : base("aws:ec2clientvpn/authorizationRule:AuthorizationRule", name, args ?? new AuthorizationRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AuthorizationRule(string name, Input<string> id, AuthorizationRuleState? state = null, CustomResourceOptions? options = null)
            : base("aws:ec2clientvpn/authorizationRule:AuthorizationRule", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AuthorizationRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AuthorizationRule Get(string name, Input<string> id, AuthorizationRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new AuthorizationRule(name, id, state, options);
        }
    }

    public sealed class AuthorizationRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the group to which the authorization rule grants access. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Input("accessGroupId")]
        public Input<string>? AccessGroupId { get; set; }

        /// <summary>
        /// Indicates whether the authorization rule grants access to all clients. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Input("authorizeAllGroups")]
        public Input<bool>? AuthorizeAllGroups { get; set; }

        /// <summary>
        /// The ID of the Client VPN endpoint.
        /// </summary>
        [Input("clientVpnEndpointId", required: true)]
        public Input<string> ClientVpnEndpointId { get; set; } = null!;

        /// <summary>
        /// A brief description of the authorization rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.
        /// </summary>
        [Input("targetNetworkCidr", required: true)]
        public Input<string> TargetNetworkCidr { get; set; } = null!;

        public AuthorizationRuleArgs()
        {
        }
    }

    public sealed class AuthorizationRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the group to which the authorization rule grants access. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Input("accessGroupId")]
        public Input<string>? AccessGroupId { get; set; }

        /// <summary>
        /// Indicates whether the authorization rule grants access to all clients. One of `access_group_id` or `authorize_all_groups` must be set.
        /// </summary>
        [Input("authorizeAllGroups")]
        public Input<bool>? AuthorizeAllGroups { get; set; }

        /// <summary>
        /// The ID of the Client VPN endpoint.
        /// </summary>
        [Input("clientVpnEndpointId")]
        public Input<string>? ClientVpnEndpointId { get; set; }

        /// <summary>
        /// A brief description of the authorization rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The IPv4 address range, in CIDR notation, of the network to which the authorization rule applies.
        /// </summary>
        [Input("targetNetworkCidr")]
        public Input<string>? TargetNetworkCidr { get; set; }

        public AuthorizationRuleState()
        {
        }
    }
}
