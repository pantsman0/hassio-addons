ARG BUILD_FROM
FROM $BUILD_FROM

# setup base
# certbot-dns-multi replaces most individual DNS plugins using lego
# Only legacy plugins are kept for providers not supported by lego: gehirn, eurodns, noris
# Azure and HE is also kept as legacy for backward compatibility (will be removed in future version)
ARG \
    BUILD_ARCH \
    ACME_VERSION \
    CERTBOT_DNS_AZURE_VERSION \
    CERTBOT_DNS_MULTI_VERSION \
    CERTBOT_VERSION \
    CRYPTOGRAPHY_VERSION

RUN apt update
RUN apt install -y python3.12 virtualenv
RUN virtualenv -p python3.12 /venv
RUN /venv/bin/python -m pip install \
    certbot==${CERTBOT_VERSION}\
    certbot-dns-azure==${CERTBOT_DNS_AZURE_VERSION} \
    certbot-dns-multi==${CERTBOT_DNS_MULTI_VERSION} \
    cryptography==${CRYPTOGRAPHY_VERSION} \
    aiohttp==${AIOHTTP_VERSION}

# Copy data
COPY rootfs /
RUN chmod +x /etc/services.d/acme-entities/run