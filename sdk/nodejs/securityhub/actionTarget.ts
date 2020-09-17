// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates Security Hub custom action.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const exampleAccount = new aws.securityhub.Account("exampleAccount", {});
 * const exampleActionTarget = new aws.securityhub.ActionTarget("exampleActionTarget", {
 *     identifier: "SendToChat",
 *     description: "This is custom action sends selected findings to chat",
 * }, {
 *     dependsOn: [exampleAccount],
 * });
 * ```
 */
export class ActionTarget extends pulumi.CustomResource {
    /**
     * Get an existing ActionTarget resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ActionTargetState, opts?: pulumi.CustomResourceOptions): ActionTarget {
        return new ActionTarget(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:securityhub/actionTarget:ActionTarget';

    /**
     * Returns true if the given object is an instance of ActionTarget.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ActionTarget {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ActionTarget.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of the Security Hub custom action target.
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The name of the custom action target.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The ID for the custom action target.
     */
    public readonly identifier!: pulumi.Output<string>;
    /**
     * The description for the custom action target.
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a ActionTarget resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ActionTargetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ActionTargetArgs | ActionTargetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ActionTargetState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["identifier"] = state ? state.identifier : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as ActionTargetArgs | undefined;
            if (!args || args.description === undefined) {
                throw new Error("Missing required property 'description'");
            }
            if (!args || args.identifier === undefined) {
                throw new Error("Missing required property 'identifier'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["identifier"] = args ? args.identifier : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(ActionTarget.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ActionTarget resources.
 */
export interface ActionTargetState {
    /**
     * Amazon Resource Name (ARN) of the Security Hub custom action target.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of the custom action target.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The ID for the custom action target.
     */
    readonly identifier?: pulumi.Input<string>;
    /**
     * The description for the custom action target.
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ActionTarget resource.
 */
export interface ActionTargetArgs {
    /**
     * The name of the custom action target.
     */
    readonly description: pulumi.Input<string>;
    /**
     * The ID for the custom action target.
     */
    readonly identifier: pulumi.Input<string>;
    /**
     * The description for the custom action target.
     */
    readonly name?: pulumi.Input<string>;
}
