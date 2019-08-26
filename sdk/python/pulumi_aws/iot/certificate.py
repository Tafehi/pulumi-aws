# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class Certificate(pulumi.CustomResource):
    active: pulumi.Output[bool]
    """
    Boolean flag to indicate if the certificate should be active
    """
    arn: pulumi.Output[str]
    """
    The ARN of the created certificate.
    """
    certificate_pem: pulumi.Output[str]
    """
    The certificate data, in PEM format.
    """
    csr: pulumi.Output[str]
    """
    The certificate signing request. Review
    [CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
    for more information on generating a certificate from a certificate signing request (CSR).
    If none is specified both the certificate and keys will be generated, review [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html)
    for more information on generating keys and a certificate.
    """
    private_key: pulumi.Output[str]
    """
    When no CSR is provided, the private key.
    """
    public_key: pulumi.Output[str]
    """
    When no CSR is provided, the public key.
    """
    def __init__(__self__, resource_name, opts=None, active=None, csr=None, __props__=None, __name__=None, __opts__=None):
        """
        Creates and manages an AWS IoT certificate.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active
        :param pulumi.Input[str] csr: The certificate signing request. Review
               [CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
               for more information on generating a certificate from a certificate signing request (CSR).
               If none is specified both the certificate and keys will be generated, review [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html)
               for more information on generating keys and a certificate.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if active is None:
                raise TypeError("Missing required property 'active'")
            __props__['active'] = active
            __props__['csr'] = csr
            __props__['arn'] = None
            __props__['certificate_pem'] = None
            __props__['private_key'] = None
            __props__['public_key'] = None
        super(Certificate, __self__).__init__(
            'aws:iot/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, active=None, arn=None, certificate_pem=None, csr=None, private_key=None, public_key=None):
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Boolean flag to indicate if the certificate should be active
        :param pulumi.Input[str] arn: The ARN of the created certificate.
        :param pulumi.Input[str] certificate_pem: The certificate data, in PEM format.
        :param pulumi.Input[str] csr: The certificate signing request. Review
               [CreateCertificateFromCsr](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCertificateFromCsr.html)
               for more information on generating a certificate from a certificate signing request (CSR).
               If none is specified both the certificate and keys will be generated, review [CreateKeysAndCertificate](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateKeysAndCertificate.html)
               for more information on generating keys and a certificate.
        :param pulumi.Input[str] private_key: When no CSR is provided, the private key.
        :param pulumi.Input[str] public_key: When no CSR is provided, the public key.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iot_certificate.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["active"] = active
        __props__["arn"] = arn
        __props__["certificate_pem"] = certificate_pem
        __props__["csr"] = csr
        __props__["private_key"] = private_key
        __props__["public_key"] = public_key
        return Certificate(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

