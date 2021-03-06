// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Iot.Outputs
{

    [OutputType]
    public sealed class TopicRuleIotAnalytic
    {
        /// <summary>
        /// Name of AWS IOT Analytics channel.
        /// </summary>
        public readonly string ChannelName;
        /// <summary>
        /// The ARN of the IAM role that grants access.
        /// </summary>
        public readonly string RoleArn;

        [OutputConstructor]
        private TopicRuleIotAnalytic(
            string channelName,

            string roleArn)
        {
            ChannelName = channelName;
            RoleArn = roleArn;
        }
    }
}
