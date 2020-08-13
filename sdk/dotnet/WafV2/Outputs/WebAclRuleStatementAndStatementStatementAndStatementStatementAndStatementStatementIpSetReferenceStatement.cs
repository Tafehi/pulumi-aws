// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2.Outputs
{

    [OutputType]
    public sealed class WebAclRuleStatementAndStatementStatementAndStatementStatementAndStatementStatementIpSetReferenceStatement
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the IP Set that this statement references.
        /// </summary>
        public readonly string Arn;

        [OutputConstructor]
        private WebAclRuleStatementAndStatementStatementAndStatementStatementAndStatementStatementIpSetReferenceStatement(string arn)
        {
            Arn = arn;
        }
    }
}
