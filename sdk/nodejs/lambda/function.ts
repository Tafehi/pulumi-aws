// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

import {ARN} from "..";

/**
 * ## Import
 *
 * Lambda Functions can be imported using the `function_name`, e.g.
 *
 * ```sh
 *  $ pulumi import aws:lambda/function:Function test_lambda my_test_lambda_function
 * ```
 */
export class Function extends pulumi.CustomResource {
    /**
     * Get an existing Function resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionState, opts?: pulumi.CustomResourceOptions): Function {
        return new Function(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:lambda/function:Function';

    /**
     * Returns true if the given object is an instance of Function.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Function {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Function.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options and `imageUri` cannot be used.
     */
    public readonly code!: pulumi.Output<pulumi.asset.Archive | undefined>;
    /**
     * Amazon Resource Name (ARN) for a Code Signing Configuration.
     */
    public readonly codeSigningConfigArn!: pulumi.Output<string | undefined>;
    /**
     * Nested block to configure the function's *dead letter queue*. See details below.
     */
    public readonly deadLetterConfig!: pulumi.Output<outputs.lambda.FunctionDeadLetterConfig | undefined>;
    /**
     * Description of what your Lambda Function does.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The Lambda environment's configuration settings. Fields documented below.
     */
    public readonly environment!: pulumi.Output<outputs.lambda.FunctionEnvironment | undefined>;
    /**
     * The connection settings for an EFS file system. Fields documented below. Before creating or updating Lambda functions with `fileSystemConfig`, EFS mount targets much be in available lifecycle state. Use `dependsOn` to explicitly declare this dependency. See [Using Amazon EFS with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-efs.html).
     */
    public readonly fileSystemConfig!: pulumi.Output<outputs.lambda.FunctionFileSystemConfig | undefined>;
    /**
     * The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
     */
    public readonly handler!: pulumi.Output<string | undefined>;
    /**
     * The Lambda OCI image configurations. Fields documented below. See [Using container images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html)
     */
    public readonly imageConfig!: pulumi.Output<outputs.lambda.FunctionImageConfig | undefined>;
    /**
     * The ECR image URI containing the function's deployment package. Conflicts with `filename`, `s3Bucket`, `s3Key`, and `s3ObjectVersion`.
     */
    public readonly imageUri!: pulumi.Output<string | undefined>;
    /**
     * The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
     */
    public /*out*/ readonly invokeArn!: pulumi.Output<string>;
    /**
     * (Optional) The ARN for the KMS encryption key.
     */
    public readonly kmsKeyArn!: pulumi.Output<string | undefined>;
    /**
     * The date this resource was last modified.
     */
    public /*out*/ readonly lastModified!: pulumi.Output<string>;
    /**
     * List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
     */
    public readonly layers!: pulumi.Output<string[] | undefined>;
    /**
     * Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    public readonly memorySize!: pulumi.Output<number | undefined>;
    /**
     * A unique name for your Lambda Function.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Lambda deployment package type. Valid values are `Zip` and `Image`. Defaults to `Zip`.
     */
    public readonly packageType!: pulumi.Output<string | undefined>;
    /**
     * Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
     */
    public readonly publish!: pulumi.Output<boolean | undefined>;
    /**
     * The Amazon Resource Name (ARN) identifying your Lambda Function Version
     * (if versioning is enabled via `publish = true`).
     */
    public /*out*/ readonly qualifiedArn!: pulumi.Output<string>;
    /**
     * The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
     */
    public readonly reservedConcurrentExecutions!: pulumi.Output<number | undefined>;
    /**
     * IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
     */
    public readonly role!: pulumi.Output<ARN>;
    /**
     * See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
     */
    public readonly runtime!: pulumi.Output<string | undefined>;
    /**
     * The S3 bucket location containing the function's deployment package. Conflicts with `filename` and `imageUri`. This bucket must reside in the same AWS region where you are creating the Lambda function.
     */
    public readonly s3Bucket!: pulumi.Output<string | undefined>;
    /**
     * The S3 key of an object containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    public readonly s3Key!: pulumi.Output<string | undefined>;
    /**
     * The object version containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    public readonly s3ObjectVersion!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) of a signing job.
     */
    public /*out*/ readonly signingJobArn!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) for a signing profile version.
     */
    public /*out*/ readonly signingProfileVersionArn!: pulumi.Output<string>;
    /**
     * Base64-encoded representation of raw SHA-256 sum of the zip file, provided either via `filename` or `s3_*` parameters.
     */
    public readonly sourceCodeHash!: pulumi.Output<string>;
    /**
     * The size in bytes of the function .zip file.
     */
    public /*out*/ readonly sourceCodeSize!: pulumi.Output<number>;
    /**
     * A map of tags to assign to the object.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    public readonly timeout!: pulumi.Output<number | undefined>;
    public readonly tracingConfig!: pulumi.Output<outputs.lambda.FunctionTracingConfig>;
    /**
     * Latest published version of your Lambda Function.
     */
    public /*out*/ readonly version!: pulumi.Output<string>;
    /**
     * Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
     */
    public readonly vpcConfig!: pulumi.Output<outputs.lambda.FunctionVpcConfig | undefined>;

    /**
     * Create a Function resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FunctionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FunctionArgs | FunctionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FunctionState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["code"] = state ? state.code : undefined;
            inputs["codeSigningConfigArn"] = state ? state.codeSigningConfigArn : undefined;
            inputs["deadLetterConfig"] = state ? state.deadLetterConfig : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["environment"] = state ? state.environment : undefined;
            inputs["fileSystemConfig"] = state ? state.fileSystemConfig : undefined;
            inputs["handler"] = state ? state.handler : undefined;
            inputs["imageConfig"] = state ? state.imageConfig : undefined;
            inputs["imageUri"] = state ? state.imageUri : undefined;
            inputs["invokeArn"] = state ? state.invokeArn : undefined;
            inputs["kmsKeyArn"] = state ? state.kmsKeyArn : undefined;
            inputs["lastModified"] = state ? state.lastModified : undefined;
            inputs["layers"] = state ? state.layers : undefined;
            inputs["memorySize"] = state ? state.memorySize : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["packageType"] = state ? state.packageType : undefined;
            inputs["publish"] = state ? state.publish : undefined;
            inputs["qualifiedArn"] = state ? state.qualifiedArn : undefined;
            inputs["reservedConcurrentExecutions"] = state ? state.reservedConcurrentExecutions : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["runtime"] = state ? state.runtime : undefined;
            inputs["s3Bucket"] = state ? state.s3Bucket : undefined;
            inputs["s3Key"] = state ? state.s3Key : undefined;
            inputs["s3ObjectVersion"] = state ? state.s3ObjectVersion : undefined;
            inputs["signingJobArn"] = state ? state.signingJobArn : undefined;
            inputs["signingProfileVersionArn"] = state ? state.signingProfileVersionArn : undefined;
            inputs["sourceCodeHash"] = state ? state.sourceCodeHash : undefined;
            inputs["sourceCodeSize"] = state ? state.sourceCodeSize : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["timeout"] = state ? state.timeout : undefined;
            inputs["tracingConfig"] = state ? state.tracingConfig : undefined;
            inputs["version"] = state ? state.version : undefined;
            inputs["vpcConfig"] = state ? state.vpcConfig : undefined;
        } else {
            const args = argsOrState as FunctionArgs | undefined;
            if ((!args || args.role === undefined) && !(opts && opts.urn)) {
                throw new Error("Missing required property 'role'");
            }
            inputs["code"] = args ? args.code : undefined;
            inputs["codeSigningConfigArn"] = args ? args.codeSigningConfigArn : undefined;
            inputs["deadLetterConfig"] = args ? args.deadLetterConfig : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["environment"] = args ? args.environment : undefined;
            inputs["fileSystemConfig"] = args ? args.fileSystemConfig : undefined;
            inputs["handler"] = args ? args.handler : undefined;
            inputs["imageConfig"] = args ? args.imageConfig : undefined;
            inputs["imageUri"] = args ? args.imageUri : undefined;
            inputs["kmsKeyArn"] = args ? args.kmsKeyArn : undefined;
            inputs["layers"] = args ? args.layers : undefined;
            inputs["memorySize"] = args ? args.memorySize : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["packageType"] = args ? args.packageType : undefined;
            inputs["publish"] = args ? args.publish : undefined;
            inputs["reservedConcurrentExecutions"] = args ? args.reservedConcurrentExecutions : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["runtime"] = args ? args.runtime : undefined;
            inputs["s3Bucket"] = args ? args.s3Bucket : undefined;
            inputs["s3Key"] = args ? args.s3Key : undefined;
            inputs["s3ObjectVersion"] = args ? args.s3ObjectVersion : undefined;
            inputs["sourceCodeHash"] = args ? args.sourceCodeHash : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["timeout"] = args ? args.timeout : undefined;
            inputs["tracingConfig"] = args ? args.tracingConfig : undefined;
            inputs["vpcConfig"] = args ? args.vpcConfig : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["invokeArn"] = undefined /*out*/;
            inputs["lastModified"] = undefined /*out*/;
            inputs["qualifiedArn"] = undefined /*out*/;
            inputs["signingJobArn"] = undefined /*out*/;
            inputs["signingProfileVersionArn"] = undefined /*out*/;
            inputs["sourceCodeSize"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Function.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Function resources.
 */
export interface FunctionState {
    /**
     * The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options and `imageUri` cannot be used.
     */
    readonly code?: pulumi.Input<pulumi.asset.Archive>;
    /**
     * Amazon Resource Name (ARN) for a Code Signing Configuration.
     */
    readonly codeSigningConfigArn?: pulumi.Input<string>;
    /**
     * Nested block to configure the function's *dead letter queue*. See details below.
     */
    readonly deadLetterConfig?: pulumi.Input<inputs.lambda.FunctionDeadLetterConfig>;
    /**
     * Description of what your Lambda Function does.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The Lambda environment's configuration settings. Fields documented below.
     */
    readonly environment?: pulumi.Input<inputs.lambda.FunctionEnvironment>;
    /**
     * The connection settings for an EFS file system. Fields documented below. Before creating or updating Lambda functions with `fileSystemConfig`, EFS mount targets much be in available lifecycle state. Use `dependsOn` to explicitly declare this dependency. See [Using Amazon EFS with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-efs.html).
     */
    readonly fileSystemConfig?: pulumi.Input<inputs.lambda.FunctionFileSystemConfig>;
    /**
     * The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
     */
    readonly handler?: pulumi.Input<string>;
    /**
     * The Lambda OCI image configurations. Fields documented below. See [Using container images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html)
     */
    readonly imageConfig?: pulumi.Input<inputs.lambda.FunctionImageConfig>;
    /**
     * The ECR image URI containing the function's deployment package. Conflicts with `filename`, `s3Bucket`, `s3Key`, and `s3ObjectVersion`.
     */
    readonly imageUri?: pulumi.Input<string>;
    /**
     * The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws.apigateway.Integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`
     */
    readonly invokeArn?: pulumi.Input<string>;
    /**
     * (Optional) The ARN for the KMS encryption key.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * The date this resource was last modified.
     */
    readonly lastModified?: pulumi.Input<string>;
    /**
     * List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
     */
    readonly layers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    readonly memorySize?: pulumi.Input<number>;
    /**
     * A unique name for your Lambda Function.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The Lambda deployment package type. Valid values are `Zip` and `Image`. Defaults to `Zip`.
     */
    readonly packageType?: pulumi.Input<string>;
    /**
     * Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
     */
    readonly publish?: pulumi.Input<boolean>;
    /**
     * The Amazon Resource Name (ARN) identifying your Lambda Function Version
     * (if versioning is enabled via `publish = true`).
     */
    readonly qualifiedArn?: pulumi.Input<string>;
    /**
     * The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
     */
    readonly reservedConcurrentExecutions?: pulumi.Input<number>;
    /**
     * IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
     */
    readonly role?: pulumi.Input<ARN>;
    /**
     * See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
     */
    readonly runtime?: pulumi.Input<string | enums.lambda.Runtime>;
    /**
     * The S3 bucket location containing the function's deployment package. Conflicts with `filename` and `imageUri`. This bucket must reside in the same AWS region where you are creating the Lambda function.
     */
    readonly s3Bucket?: pulumi.Input<string>;
    /**
     * The S3 key of an object containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    readonly s3Key?: pulumi.Input<string>;
    /**
     * The object version containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    readonly s3ObjectVersion?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) of a signing job.
     */
    readonly signingJobArn?: pulumi.Input<string>;
    /**
     * The Amazon Resource Name (ARN) for a signing profile version.
     */
    readonly signingProfileVersionArn?: pulumi.Input<string>;
    /**
     * Base64-encoded representation of raw SHA-256 sum of the zip file, provided either via `filename` or `s3_*` parameters.
     */
    readonly sourceCodeHash?: pulumi.Input<string>;
    /**
     * The size in bytes of the function .zip file.
     */
    readonly sourceCodeSize?: pulumi.Input<number>;
    /**
     * A map of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    readonly timeout?: pulumi.Input<number>;
    readonly tracingConfig?: pulumi.Input<inputs.lambda.FunctionTracingConfig>;
    /**
     * Latest published version of your Lambda Function.
     */
    readonly version?: pulumi.Input<string>;
    /**
     * Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
     */
    readonly vpcConfig?: pulumi.Input<inputs.lambda.FunctionVpcConfig>;
}

/**
 * The set of arguments for constructing a Function resource.
 */
export interface FunctionArgs {
    /**
     * The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options and `imageUri` cannot be used.
     */
    readonly code?: pulumi.Input<pulumi.asset.Archive>;
    /**
     * Amazon Resource Name (ARN) for a Code Signing Configuration.
     */
    readonly codeSigningConfigArn?: pulumi.Input<string>;
    /**
     * Nested block to configure the function's *dead letter queue*. See details below.
     */
    readonly deadLetterConfig?: pulumi.Input<inputs.lambda.FunctionDeadLetterConfig>;
    /**
     * Description of what your Lambda Function does.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The Lambda environment's configuration settings. Fields documented below.
     */
    readonly environment?: pulumi.Input<inputs.lambda.FunctionEnvironment>;
    /**
     * The connection settings for an EFS file system. Fields documented below. Before creating or updating Lambda functions with `fileSystemConfig`, EFS mount targets much be in available lifecycle state. Use `dependsOn` to explicitly declare this dependency. See [Using Amazon EFS with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/services-efs.html).
     */
    readonly fileSystemConfig?: pulumi.Input<inputs.lambda.FunctionFileSystemConfig>;
    /**
     * The function [entrypoint](https://docs.aws.amazon.com/lambda/latest/dg/walkthrough-custom-events-create-test-function.html) in your code.
     */
    readonly handler?: pulumi.Input<string>;
    /**
     * The Lambda OCI image configurations. Fields documented below. See [Using container images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html)
     */
    readonly imageConfig?: pulumi.Input<inputs.lambda.FunctionImageConfig>;
    /**
     * The ECR image URI containing the function's deployment package. Conflicts with `filename`, `s3Bucket`, `s3Key`, and `s3ObjectVersion`.
     */
    readonly imageUri?: pulumi.Input<string>;
    /**
     * (Optional) The ARN for the KMS encryption key.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)
     */
    readonly layers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    readonly memorySize?: pulumi.Input<number>;
    /**
     * A unique name for your Lambda Function.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The Lambda deployment package type. Valid values are `Zip` and `Image`. Defaults to `Zip`.
     */
    readonly packageType?: pulumi.Input<string>;
    /**
     * Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.
     */
    readonly publish?: pulumi.Input<boolean>;
    /**
     * The amount of reserved concurrent executions for this lambda function. A value of `0` disables lambda from being triggered and `-1` removes any concurrency limitations. Defaults to Unreserved Concurrency Limits `-1`. See [Managing Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html)
     */
    readonly reservedConcurrentExecutions?: pulumi.Input<number>;
    /**
     * IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model](https://docs.aws.amazon.com/lambda/latest/dg/intro-permission-model.html) for more details.
     */
    readonly role: pulumi.Input<ARN>;
    /**
     * See [Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime) for valid values.
     */
    readonly runtime?: pulumi.Input<string | enums.lambda.Runtime>;
    /**
     * The S3 bucket location containing the function's deployment package. Conflicts with `filename` and `imageUri`. This bucket must reside in the same AWS region where you are creating the Lambda function.
     */
    readonly s3Bucket?: pulumi.Input<string>;
    /**
     * The S3 key of an object containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    readonly s3Key?: pulumi.Input<string>;
    /**
     * The object version containing the function's deployment package. Conflicts with `filename` and `imageUri`.
     */
    readonly s3ObjectVersion?: pulumi.Input<string>;
    /**
     * Base64-encoded representation of raw SHA-256 sum of the zip file, provided either via `filename` or `s3_*` parameters.
     */
    readonly sourceCodeHash?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the object.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)
     */
    readonly timeout?: pulumi.Input<number>;
    readonly tracingConfig?: pulumi.Input<inputs.lambda.FunctionTracingConfig>;
    /**
     * Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC](http://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
     */
    readonly vpcConfig?: pulumi.Input<inputs.lambda.FunctionVpcConfig>;
}
