// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a AWS Transfer Server resource.
 * 
 * 
 * ```hcl
 * resource "aws_iam_role" "foo" {
 * 	name = "tf-test-transfer-server-iam-role"
 *   
 * 	assume_role_policy = <<EOF
 * {
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 		"Effect": "Allow",
 * 		"Principal": {
 * 			"Service": "transfer.amazonaws.com"
 * 		},
 * 		"Action": "sts:AssumeRole"
 * 		}
 * 	]
 * }
 * EOF
 * }
 * 
 * resource "aws_iam_role_policy" "foo" {
 * 	name = "tf-test-transfer-server-iam-policy-%s"
 * 	role = "${aws_iam_role.foo.id}"
 * 	policy = <<POLICY
 * {
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 		"Sid": "AllowFullAccesstoCloudWatchLogs",
 * 		"Effect": "Allow",
 * 		"Action": [
 * 			"logs:*"
 * 		],
 * 		"Resource": "*"
 * 		}
 * 	]
 * }
 * POLICY
 * }
 * 
 * 
 * resource "aws_transfer_server" "foo" {
 *   identity_provider_type = "SERVICE_MANAGED"
 *   logging_role = "${aws_iam_role.foo.arn}"
 * 
 *   tags {
 * 	NAME   = "tf-acc-test-transfer-server"
 * 	ENV    = "test"
 *   }
 * }
 * ```
 */
export class Server extends pulumi.CustomResource {
    /**
     * Get an existing Server resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerState, opts?: pulumi.CustomResourceOptions): Server {
        return new Server(name, <any>state, { ...opts, id: id });
    }

    /**
     * Amazon Resource Name (ARN) of Transfer Server
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
     */
    public /*out*/ readonly endpoint: pulumi.Output<string>;
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    public readonly forceDestroy: pulumi.Output<boolean | undefined>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    public readonly identityProviderType: pulumi.Output<string | undefined>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
     */
    public readonly invocationRole: pulumi.Output<string | undefined>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    public readonly loggingRole: pulumi.Output<string | undefined>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
     */
    public readonly url: pulumi.Output<string | undefined>;

    /**
     * Create a Server resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerArgs | ServerState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ServerState = argsOrState as ServerState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["endpoint"] = state ? state.endpoint : undefined;
            inputs["forceDestroy"] = state ? state.forceDestroy : undefined;
            inputs["identityProviderType"] = state ? state.identityProviderType : undefined;
            inputs["invocationRole"] = state ? state.invocationRole : undefined;
            inputs["loggingRole"] = state ? state.loggingRole : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["url"] = state ? state.url : undefined;
        } else {
            const args = argsOrState as ServerArgs | undefined;
            inputs["forceDestroy"] = args ? args.forceDestroy : undefined;
            inputs["identityProviderType"] = args ? args.identityProviderType : undefined;
            inputs["invocationRole"] = args ? args.invocationRole : undefined;
            inputs["loggingRole"] = args ? args.loggingRole : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["url"] = args ? args.url : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["endpoint"] = undefined /*out*/;
        }
        super("aws:transfer/server:Server", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Server resources.
 */
export interface ServerState {
    /**
     * Amazon Resource Name (ARN) of Transfer Server
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The endpoint of the Transfer Server (e.g. `s-12345678.server.transfer.REGION.amazonaws.com`)
     */
    readonly endpoint?: pulumi.Input<string>;
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    readonly identityProviderType?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
     */
    readonly invocationRole?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    readonly loggingRole?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
     */
    readonly url?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Server resource.
 */
export interface ServerArgs {
    /**
     * A boolean that indicates all users associated with the server should be deleted so that the Server can be destroyed without error. The default value is `false`.
     */
    readonly forceDestroy?: pulumi.Input<boolean>;
    /**
     * The mode of authentication enabled for this service. The default value is `SERVICE_MANAGED`, which allows you to store and access SFTP user credentials within the service. `API_GATEWAY` indicates that user authentication requires a call to an API Gateway endpoint URL provided by you to integrate an identity provider of your choice.
     */
    readonly identityProviderType?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of the IAM role used to authenticate the user account with an `identity_provider_type` of `API_GATEWAY`.
     */
    readonly invocationRole?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to write your SFTP users’ activity to your Amazon CloudWatch logs for monitoring and auditing purposes.
     */
    readonly loggingRole?: pulumi.Input<string>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: any}>;
    /**
     * - URL of the service endpoint used to authenticate users with an `identity_provider_type` of `API_GATEWAY`.
     */
    readonly url?: pulumi.Input<string>;
}
