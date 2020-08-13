// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2.Inputs
{

    public sealed class WebAclRuleStatementNotStatementStatementNotStatementGetArgs : Pulumi.ResourceArgs
    {
        [Input("statements", required: true)]
        private InputList<Inputs.WebAclRuleStatementNotStatementStatementNotStatementStatementGetArgs>? _statements;

        /// <summary>
        /// The statement to negate. You can use any statement that can be nested. See Statement above for details.
        /// </summary>
        public InputList<Inputs.WebAclRuleStatementNotStatementStatementNotStatementStatementGetArgs> Statements
        {
            get => _statements ?? (_statements = new InputList<Inputs.WebAclRuleStatementNotStatementStatementNotStatementStatementGetArgs>());
            set => _statements = value;
        }

        public WebAclRuleStatementNotStatementStatementNotStatementGetArgs()
        {
        }
    }
}
