// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Msk
{
    public static class GetConfiguration
    {
        /// <summary>
        /// Get information on an Amazon MSK Configuration.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Aws.Msk.GetConfiguration.InvokeAsync(new Aws.Msk.GetConfigurationArgs
        ///         {
        ///             Name = "example",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// 
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConfigurationResult> InvokeAsync(GetConfigurationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConfigurationResult>("aws:msk/getConfiguration:getConfiguration", args ?? new GetConfigurationArgs(), options.WithVersion());
    }


    public sealed class GetConfigurationArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the configuration.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetConfigurationArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetConfigurationResult
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the configuration.
        /// </summary>
        public readonly string Arn;
        /// <summary>
        /// Description of the configuration.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// List of Apache Kafka versions which can use this configuration.
        /// </summary>
        public readonly ImmutableArray<string> KafkaVersions;
        /// <summary>
        /// Latest revision of the configuration.
        /// </summary>
        public readonly int LatestRevision;
        public readonly string Name;
        /// <summary>
        /// Contents of the server.properties file.
        /// </summary>
        public readonly string ServerProperties;

        [OutputConstructor]
        private GetConfigurationResult(
            string arn,

            string description,

            string id,

            ImmutableArray<string> kafkaVersions,

            int latestRevision,

            string name,

            string serverProperties)
        {
            Arn = arn;
            Description = description;
            Id = id;
            KafkaVersions = kafkaVersions;
            LatestRevision = latestRevision;
            Name = name;
            ServerProperties = serverProperties;
        }
    }
}
