// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2.Inputs
{

    public sealed class WebAclRuleStatementOrStatementStatementNotStatementStatementOrStatementStatementGeoMatchStatementGetArgs : Pulumi.ResourceArgs
    {
        [Input("countryCodes", required: true)]
        private InputList<string>? _countryCodes;

        /// <summary>
        /// An array of two-character country codes, for example, [ "US", "CN" ], from the alpha-2 country ISO codes of the `ISO 3166` international standard. See the [documentation](https://docs.aws.amazon.com/waf/latest/APIReference/API_GeoMatchStatement.html) for valid values.
        /// </summary>
        public InputList<string> CountryCodes
        {
            get => _countryCodes ?? (_countryCodes = new InputList<string>());
            set => _countryCodes = value;
        }

        public WebAclRuleStatementOrStatementStatementNotStatementStatementOrStatementStatementGeoMatchStatementGetArgs()
        {
        }
    }
}
