// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * > **Note:** `aws_alb_target_group` is known as `aws_lb_target_group`. The functionality is identical.
 * 
 * Provides information about a Load Balancer Target Group.
 * 
 * This data source can prove useful when a module accepts an LB Target Group as an
 * input variable and needs to know its attributes. It can also be used to get the ARN of
 * an LB Target Group for use in other resources, given LB Target Group name.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const config = new pulumi.Config();
 * const lbTgArn = config.get("lbTgArn") || "";
 * const lbTgName = config.get("lbTgName") || "";
 * 
 * const test = pulumi.output(aws.lb.getTargetGroup({
 *     arn: lbTgArn,
 *     name: lbTgName,
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lb_target_group.html.markdown.
 */
export function getTargetGroup(args?: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> & GetTargetGroupResult {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetTargetGroupResult> = pulumi.runtime.invoke("aws:lb/getTargetGroup:getTargetGroup", {
        "arn": args.arn,
        "name": args.name,
        "tags": args.tags,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupArgs {
    /**
     * The full ARN of the target group.
     */
    readonly arn?: string;
    /**
     * The unique name of the target group.
     */
    readonly name?: string;
    readonly tags?: {[key: string]: any};
}

/**
 * A collection of values returned by getTargetGroup.
 */
export interface GetTargetGroupResult {
    readonly arn: string;
    readonly arnSuffix: string;
    readonly deregistrationDelay: number;
    readonly healthCheck: { enabled: boolean, healthyThreshold: number, interval: number, matcher: string, path: string, port: string, protocol: string, timeout: number, unhealthyThreshold: number };
    readonly lambdaMultiValueHeadersEnabled: boolean;
    readonly name: string;
    readonly port: number;
    readonly protocol: string;
    readonly proxyProtocolV2: boolean;
    readonly slowStart: number;
    readonly stickiness: { cookieDuration: number, enabled: boolean, type: string };
    readonly tags: {[key: string]: any};
    readonly targetType: string;
    readonly vpcId: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}