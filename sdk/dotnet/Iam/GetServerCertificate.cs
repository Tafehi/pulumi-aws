// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Iam
{
    public static class GetServerCertificate
    {
        /// <summary>
        /// Use this data source to lookup information about IAM Server Certificates.
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
        ///         var my_domain = Output.Create(Aws.Iam.GetServerCertificate.InvokeAsync(new Aws.Iam.GetServerCertificateArgs
        ///         {
        ///             Latest = true,
        ///             NamePrefix = "my-domain.org",
        ///         }));
        ///         var elb = new Aws.Elb.LoadBalancer("elb", new Aws.Elb.LoadBalancerArgs
        ///         {
        ///             Listeners = 
        ///             {
        ///                 new Aws.Elb.Inputs.LoadBalancerListenerArgs
        ///                 {
        ///                     InstancePort = 8000,
        ///                     InstanceProtocol = "https",
        ///                     LbPort = 443,
        ///                     LbProtocol = "https",
        ///                     SslCertificateId = my_domain.Apply(my_domain =&gt; my_domain.Arn),
        ///                 },
        ///             },
        ///         });
        ///     }
        /// 
        /// }
        /// ```
        /// 
        /// {{% /example %}}
        /// {{% /examples %}}
        /// ## Import 
        /// 
        /// The import function will read in certificate body, certificate chain (if it exists), id, name, path, and arn. 
        /// It will not retrieve the private key which is not available through the AWS API.   
        /// </summary>
        public static Task<GetServerCertificateResult> InvokeAsync(GetServerCertificateArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetServerCertificateResult>("aws:iam/getServerCertificate:getServerCertificate", args ?? new GetServerCertificateArgs(), options.WithVersion());
    }


    public sealed class GetServerCertificateArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// sort results by expiration date. returns the certificate with expiration date in furthest in the future.
        /// </summary>
        [Input("latest")]
        public bool? Latest { get; set; }

        /// <summary>
        /// exact name of the cert to lookup
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// prefix of cert to filter by
        /// </summary>
        [Input("namePrefix")]
        public string? NamePrefix { get; set; }

        /// <summary>
        /// prefix of path to filter by
        /// </summary>
        [Input("pathPrefix")]
        public string? PathPrefix { get; set; }

        public GetServerCertificateArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetServerCertificateResult
    {
        public readonly string Arn;
        public readonly string CertificateBody;
        public readonly string CertificateChain;
        public readonly string ExpirationDate;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly bool? Latest;
        public readonly string Name;
        public readonly string? NamePrefix;
        public readonly string Path;
        public readonly string? PathPrefix;
        public readonly string UploadDate;

        [OutputConstructor]
        private GetServerCertificateResult(
            string arn,

            string certificateBody,

            string certificateChain,

            string expirationDate,

            string id,

            bool? latest,

            string name,

            string? namePrefix,

            string path,

            string? pathPrefix,

            string uploadDate)
        {
            Arn = arn;
            CertificateBody = certificateBody;
            CertificateChain = certificateChain;
            ExpirationDate = expirationDate;
            Id = id;
            Latest = latest;
            Name = name;
            NamePrefix = namePrefix;
            Path = path;
            PathPrefix = pathPrefix;
            UploadDate = uploadDate;
        }
    }
}
