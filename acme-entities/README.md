# Home Assistant App: Acme Entities

This is a fork of the Let's Encrypt addon for Home Assistant, with the main script rewritten in Python and some extra features added.

Let's Encrypt is a certificate authority that provides free X.509 certificates for Transport Layer Security encryption via an automated process designed to eliminate the hitherto complex process of manual creation, validation, signing, installation, and renewal of certificates for secure websites.

![Supports aarch64 Architecture][aarch64-shield] ![Supports amd64 Architecture][amd64-shield]

Setting up Letsencrypt allows you to use validated certificates for your webpages and web-interfaces, with this addon you can request and renew certificates for multiple domains and expose them as entities for automations.
It requires you to own the domain you are requesting the certificate for, or at least have some way of validating your ACME challenge.

The generated certificate can be used within others addons, and are stored in the `/ssl` directory. Be careful not to overwrite these files with other addons, or especially to overwrite the server certificate by using the default TLS certificate name.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
