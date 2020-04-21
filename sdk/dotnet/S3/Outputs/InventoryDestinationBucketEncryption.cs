// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.S3.Outputs
{

    [OutputType]
    public sealed class InventoryDestinationBucketEncryption
    {
        /// <summary>
        /// Specifies to use server-side encryption with AWS KMS-managed keys to encrypt the inventory file (documented below).
        /// </summary>
        public readonly Outputs.InventoryDestinationBucketEncryptionSseKms? SseKms;
        /// <summary>
        /// Specifies to use server-side encryption with Amazon S3-managed keys (SSE-S3) to encrypt the inventory file.
        /// </summary>
        public readonly Outputs.InventoryDestinationBucketEncryptionSseS3? SseS3;

        [OutputConstructor]
        private InventoryDestinationBucketEncryption(
            Outputs.InventoryDestinationBucketEncryptionSseKms? sseKms,

            Outputs.InventoryDestinationBucketEncryptionSseS3? sseS3)
        {
            SseKms = sseKms;
            SseS3 = sseS3;
        }
    }
}