// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";
import * as lumirt from "@lumi/lumirt";

import {RestApi} from "./restApi";

export class BasePathMapping extends lumi.NamedResource implements BasePathMappingArgs {
    public readonly restApi: RestApi;
    public readonly basePath?: string;
    public readonly domainName: string;
    public readonly stageName?: string;

    constructor(name: string, args: BasePathMappingArgs) {
        super(name);
        if (lumirt.defaultIfComputed(args.restApi, "") === undefined) {
            throw new Error("Property argument 'restApi' is required, but was missing");
        }
        this.restApi = args.restApi;
        this.basePath = args.basePath;
        if (lumirt.defaultIfComputed(args.domainName, "") === undefined) {
            throw new Error("Property argument 'domainName' is required, but was missing");
        }
        this.domainName = args.domainName;
        this.stageName = args.stageName;
    }
}

export interface BasePathMappingArgs {
    readonly restApi: RestApi;
    readonly basePath?: string;
    readonly domainName: string;
    readonly stageName?: string;
}

