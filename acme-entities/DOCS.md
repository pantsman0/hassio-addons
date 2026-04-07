# Home Assistant App: Acme Entities

## Installation

Follow these steps to get the app (formerly known as add-on) installed on your system:

1. In Home Assistant, go to **Settings** > **Apps** > **Install app**.
2. Find the "Acme Entities" app and click it.
3. Click on the "INSTALL" button.

## How to use

The Acme Entities app can be configured via the app interface.
The configuration via YAML is also possible, see the examples below.

Navigate in your Home Assistant frontend to the apps overview page at
**Settings** > **Apps**, and pick the **Acme Entities** app. On the top,
pick the **Configuration** page.

Provide the DNS authenticators, and the certificates to issue. Additionally, provide the
e-mail address used for the registration, and path values for **Priv Key File**
and **Certificate File** on each certificate.

As this is intended for generating certificates for multiple domains and different machines, only the DNS challenge is supported.

### DNS providers

<!-- Developer note: please add a new plugin alphabetically into all lists -->

<details>
  <summary>Supported DNS providers</summary>

```txt
dns-lego (generic, supports any lego DNS provider)
dns-azure
dns-bunny
dns-cloudflare
dns-cloudns
dns-desec
dns-digitalocean
dns-directadmin
dns-dnsimple
dns-dnsmadeeasy
dns-domainoffensive
dns-dreamhost
dns-duckdns
dns-dynu
dns-easydns
dns-eurodns
dns-gandi
dns-gehirn
dns-godaddy
dns-google
dns-he
dns-hetzner
dns-infomaniak
dns-inwx
dns-ionos
dns-joker
dns-linode
dns-loopia
dns-luadns
dns-mijn-host
dns-namecheap
dns-netcup
dns-njalla
dns-noris
dns-nsone
dns-ovh
dns-plesk
dns-porkbun
dns-rfc2136
dns-route53
dns-sakuracloud
dns-simply
dns-transip
dns-websupport
```

</details>

<details>
  <summary>In addition add the fields according to the credentials required by your DNS provider:</summary>

```yaml
propagation_seconds: 60
lego_env: []
lego_provider: ''
aws_access_key_id: ''
aws_region: ''
aws_secret_access_key: ''
azure_config: ''
bunny_api_key: ''
cloudflare_api_key: ''
cloudflare_api_token: ''
cloudflare_email: ''
cloudns_auth_id: ''
cloudns_auth_password: ''
cloudns_sub_auth_id: ''
desec_token: ''
digitalocean_token: ''
directadmin_password: ''
directadmin_url: ''
directadmin_username: ''
dns_multi_nameservers: ''
dnsimple_token: ''
dnsmadeeasy_api_key: ''
dnsmadeeasy_secret_key: ''
domainoffensive_token: ''
dreamhost_api_key: ''
duckdns_token: ''
dynu_auth_token: ''
easydns_endpoint: ''
easydns_key: ''
easydns_token: ''
eurodns_apiKey: ''
eurodns_applicationId: ''
gandi_api_key: ''
gandi_token: ''
gehirn_api_secret: ''
gehirn_api_token: ''
godaddy_key: ''
godaddy_secret: ''
google_creds: ''
he_pass: ''
he_user: ''
hetzner_api_token: ''
infomaniak_api_token: ''
inwx_password: ''
inwx_shared_secret: ''
inwx_username: ''
ionos_prefix: ''
ionos_secret: ''
joker_password: ''
joker_username: ''
linode_key: ''
linode_version: ''
loopia_password: ''
loopia_user: ''
luadns_email: ''
luadns_token: ''
mijn_host_api_key: ''
namecheap_api_key: ''
namecheap_username: ''
netcup_api_key: ''
netcup_api_password: ''
netcup_customer_id: ''
njalla_token: ''
noris_token: ''
nsone_api_key: ''
ovh_application_key: ''
ovh_application_secret: ''
ovh_consumer_key: ''
ovh_endpoint: ''
plesk_api_url: ''
plesk_password: ''
plesk_username: ''
porkbun_key: ''
porkbun_secret: ''
rfc2136_algorithm: ''
rfc2136_name: ''
rfc2136_port: ''
rfc2136_secret: ''
rfc2136_server: ''
rfc2136_sign_query: false
sakuracloud_api_secret: ''
sakuracloud_api_token: ''
simply_account_name: ''
simply_api_key: ''
transip_api_key: ''
transip_username: ''
websupport_identifier: ''
websupport_secret_key: ''
```

</details>

### Split DNS and custom nameservers

If cert renewal fails with an error like `failed to find zone <domain>: zone could not be found`,
your local DNS is returning a different SOA than your DNS provider manages. This occurs
in split DNS setups where a local DNS server handles a zone that is also hosted publicly, or where
the local resolver returns a different SOA response than the public authoritative server.

Set `dns_multi_nameservers` to a comma-separated list of public DNS servers to use for zone
determination and CNAME resolution. Port is optional and defaults to 53.

```yaml
dns_multi_nameservers: '1.1.1.1,8.8.8.8'
```

### Configure certificate files

The certificate files will be available within the "ssl" share after successful
request of the certificates.

By default, other apps are referring to the correct path of the certificates.
You can in addition find the files via the **Samba** app within the "ssl" share.

For example, to use the certificates provided by this app to enable TLS on
Home Assistant in the default paths, add the following lines to Home
Assistant's main configuration file, `configuration.yaml`:

```yaml
# TLS with letsencrypt app
http:
  server_port: 443
  ssl_certificate: /ssl/fullchain.pem
  ssl_key: /ssl/privkey.pem
```

### Create & renew certificates

TODO