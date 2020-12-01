// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.NetworkFirewall.Inputs
{

    public sealed class RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The lower limit of the port range. This must be less than or equal to the `to_port`.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        /// <summary>
        /// The upper limit of the port range. This must be greater than or equal to the `from_port`.
        /// </summary>
        [Input("toPort")]
        public Input<int>? ToPort { get; set; }

        public RuleGroupRuleGroupRulesSourceStatelessRulesAndCustomActionsStatelessRuleRuleDefinitionMatchAttributesDestinationPortArgs()
        {
        }
    }
}