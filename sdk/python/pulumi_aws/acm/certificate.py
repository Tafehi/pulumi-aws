# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Certificate']


class Certificate(pulumi.CustomResource):
    arn: pulumi.Output[str] = pulumi.property("arn")
    """
    The ARN of the certificate
    """

    certificate_authority_arn: pulumi.Output[Optional[str]] = pulumi.property("certificateAuthorityArn")
    """
    ARN of an ACMPCA
    """

    certificate_body: pulumi.Output[Optional[str]] = pulumi.property("certificateBody")
    """
    The certificate's PEM-formatted public key
    """

    certificate_chain: pulumi.Output[Optional[str]] = pulumi.property("certificateChain")
    """
    The certificate's PEM-formatted chain
    * Creating a private CA issued certificate
    """

    domain_name: pulumi.Output[str] = pulumi.property("domainName")
    """
    A domain name for which the certificate should be issued
    """

    domain_validation_options: pulumi.Output[List['outputs.CertificateDomainValidationOption']] = pulumi.property("domainValidationOptions")
    """
    A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if `DNS`-validation was used.
    """

    options: pulumi.Output[Optional['outputs.CertificateOptions']] = pulumi.property("options")
    """
    Configuration block used to set certificate options. Detailed below.
    * Importing an existing certificate
    """

    private_key: pulumi.Output[Optional[str]] = pulumi.property("privateKey")
    """
    The certificate's PEM-formatted private key
    """

    status: pulumi.Output[str] = pulumi.property("status")
    """
    Status of the certificate.
    """

    subject_alternative_names: pulumi.Output[List[str]] = pulumi.property("subjectAlternativeNames")
    """
    A list of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) to trigger recreation.
    """

    tags: pulumi.Output[Optional[Mapping[str, str]]] = pulumi.property("tags")
    """
    A map of tags to assign to the resource.
    """

    validation_emails: pulumi.Output[List[str]] = pulumi.property("validationEmails")
    """
    A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.
    """

    validation_method: pulumi.Output[str] = pulumi.property("validationMethod")
    """
    Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into the provider.
    """

    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_authority_arn: Optional[pulumi.Input[str]] = None,
                 certificate_body: Optional[pulumi.Input[str]] = None,
                 certificate_chain: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 options: Optional[pulumi.Input[pulumi.InputType['CertificateOptionsArgs']]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 subject_alternative_names: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 validation_method: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The ACM certificate resource allows requesting and management of certificates
        from the Amazon Certificate Manager.

        It deals with requesting certificates and managing their attributes and life-cycle.
        This resource does not deal with validation of a certificate but can provide inputs
        for other resources implementing the validation. It does not wait for a certificate to be issued.
        Use a `acm.CertificateValidation` resource for this.

        Most commonly, this resource is used together with `route53.Record` and
        `acm.CertificateValidation` to request a DNS validated certificate,
        deploy the required validation records and wait for validation to complete.

        Domain validation through E-Mail is also supported but should be avoided as it requires a manual step outside
        of this provider.

        It's recommended to specify `create_before_destroy = true` in a [lifecycle](https://www.terraform.io/docs/configuration/resources.html#lifecycle) block to replace a certificate
        which is currently in use (eg, by `lb.Listener`).

        ## Example Usage
        ### Certificate creation

        ```python
        import pulumi
        import pulumi_aws as aws

        cert = aws.acm.Certificate("cert",
            domain_name="example.com",
            tags={
                "Environment": "test",
            },
            validation_method="DNS")
        ```
        ### Importing an existing certificate

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_tls as tls

        example_private_key = tls.PrivateKey("examplePrivateKey", algorithm="RSA")
        example_self_signed_cert = tls.SelfSignedCert("exampleSelfSignedCert",
            allowed_uses=[
                "key_encipherment",
                "digital_signature",
                "server_auth",
            ],
            key_algorithm="RSA",
            private_key_pem=example_private_key.private_key_pem,
            subjects=[{
                "commonName": "example.com",
                "organization": "ACME Examples, Inc",
            }],
            validity_period_hours=12)
        cert = aws.acm.Certificate("cert",
            certificate_body=example_self_signed_cert.cert_pem,
            private_key=example_private_key.private_key_pem)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_authority_arn: ARN of an ACMPCA
        :param pulumi.Input[str] certificate_body: The certificate's PEM-formatted public key
        :param pulumi.Input[str] certificate_chain: The certificate's PEM-formatted chain
               * Creating a private CA issued certificate
        :param pulumi.Input[str] domain_name: A domain name for which the certificate should be issued
        :param pulumi.Input[pulumi.InputType['CertificateOptionsArgs']] options: Configuration block used to set certificate options. Detailed below.
               * Importing an existing certificate
        :param pulumi.Input[str] private_key: The certificate's PEM-formatted private key
        :param pulumi.Input[List[pulumi.Input[str]]] subject_alternative_names: A list of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) to trigger recreation.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[str] validation_method: Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into the provider.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['certificate_authority_arn'] = certificate_authority_arn
            __props__['certificate_body'] = certificate_body
            __props__['certificate_chain'] = certificate_chain
            __props__['domain_name'] = domain_name
            __props__['options'] = options
            __props__['private_key'] = private_key
            __props__['subject_alternative_names'] = subject_alternative_names
            __props__['tags'] = tags
            __props__['validation_method'] = validation_method
            __props__['arn'] = None
            __props__['domain_validation_options'] = None
            __props__['status'] = None
            __props__['validation_emails'] = None
        super(Certificate, __self__).__init__(
            'aws:acm/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: str,
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            certificate_authority_arn: Optional[pulumi.Input[str]] = None,
            certificate_body: Optional[pulumi.Input[str]] = None,
            certificate_chain: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            domain_validation_options: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['CertificateDomainValidationOptionArgs']]]]] = None,
            options: Optional[pulumi.Input[pulumi.InputType['CertificateOptionsArgs']]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            subject_alternative_names: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            validation_emails: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            validation_method: Optional[pulumi.Input[str]] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the certificate
        :param pulumi.Input[str] certificate_authority_arn: ARN of an ACMPCA
        :param pulumi.Input[str] certificate_body: The certificate's PEM-formatted public key
        :param pulumi.Input[str] certificate_chain: The certificate's PEM-formatted chain
               * Creating a private CA issued certificate
        :param pulumi.Input[str] domain_name: A domain name for which the certificate should be issued
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['CertificateDomainValidationOptionArgs']]]] domain_validation_options: A list of attributes to feed into other resources to complete certificate validation. Can have more than one element, e.g. if SANs are defined. Only set if `DNS`-validation was used.
        :param pulumi.Input[pulumi.InputType['CertificateOptionsArgs']] options: Configuration block used to set certificate options. Detailed below.
               * Importing an existing certificate
        :param pulumi.Input[str] private_key: The certificate's PEM-formatted private key
        :param pulumi.Input[str] status: Status of the certificate.
        :param pulumi.Input[List[pulumi.Input[str]]] subject_alternative_names: A list of domains that should be SANs in the issued certificate. To remove all elements of a previously configured list, set this value equal to an empty list (`[]`) to trigger recreation.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] validation_emails: A list of addresses that received a validation E-Mail. Only set if `EMAIL`-validation was used.
        :param pulumi.Input[str] validation_method: Which method to use for validation. `DNS` or `EMAIL` are valid, `NONE` can be used for certificates that were imported into ACM and then into the provider.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["certificate_authority_arn"] = certificate_authority_arn
        __props__["certificate_body"] = certificate_body
        __props__["certificate_chain"] = certificate_chain
        __props__["domain_name"] = domain_name
        __props__["domain_validation_options"] = domain_validation_options
        __props__["options"] = options
        __props__["private_key"] = private_key
        __props__["status"] = status
        __props__["subject_alternative_names"] = subject_alternative_names
        __props__["tags"] = tags
        __props__["validation_emails"] = validation_emails
        __props__["validation_method"] = validation_method
        return Certificate(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

