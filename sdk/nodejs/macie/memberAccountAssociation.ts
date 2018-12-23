// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Associates an AWS account with Amazon Macie as a member account.
 * 
 * > **NOTE:** Before using Amazon Macie for the first time it must be enabled manually. Instructions are [here](https://docs.aws.amazon.com/macie/latest/userguide/macie-setting-up.html#macie-setting-up-enable).
 */
export class MemberAccountAssociation extends pulumi.CustomResource {
    /**
     * Get an existing MemberAccountAssociation resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemberAccountAssociationState, opts?: pulumi.CustomResourceOptions): MemberAccountAssociation {
        return new MemberAccountAssociation(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    public readonly memberAccountId: pulumi.Output<string>;

    /**
     * Create a MemberAccountAssociation resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MemberAccountAssociationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MemberAccountAssociationArgs | MemberAccountAssociationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: MemberAccountAssociationState = argsOrState as MemberAccountAssociationState | undefined;
            inputs["memberAccountId"] = state ? state.memberAccountId : undefined;
        } else {
            const args = argsOrState as MemberAccountAssociationArgs | undefined;
            if (!args || args.memberAccountId === undefined) {
                throw new Error("Missing required property 'memberAccountId'");
            }
            inputs["memberAccountId"] = args ? args.memberAccountId : undefined;
        }
        super("aws:macie/memberAccountAssociation:MemberAccountAssociation", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MemberAccountAssociation resources.
 */
export interface MemberAccountAssociationState {
    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    readonly memberAccountId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MemberAccountAssociation resource.
 */
export interface MemberAccountAssociationArgs {
    /**
     * The ID of the AWS account that you want to associate with Amazon Macie as a member account.
     */
    readonly memberAccountId: pulumi.Input<string>;
}
