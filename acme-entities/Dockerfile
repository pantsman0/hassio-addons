ARG BUILD_FROM
FROM $BUILD_FROM

# Allow pip to install packages system-wide on Debian
ENV PIP_BREAK_SYSTEM_PACKAGES=1

# setup base
# certbot-dns-multi replaces most individual DNS plugins using lego
# Only legacy plugins are kept for providers not supported by lego: gehirn, eurodns, noris
# Azure and HE is also kept as legacy for backward compatibility (will be removed in future version)
ARG \
    BUILD_ARCH \
    ACME_VERSION \
    CERTBOT_DNS_AZURE_VERSION \
    CERTBOT_DNS_EURODNS_VERSION \
    CERTBOT_DNS_HURRICANE_ELECTRIC_VERSION \
    CERTBOT_DNS_MULTI_VERSION \
    CERTBOT_DNS_NORISNETWORK_VERSION \
    CERTBOT_VERSION \
    CRYPTOGRAPHY_VERSION

RUN \
    set -x \
    && apk add --no-cache \
        ca-certificates \
        openssl \
        libffi \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        cargo \
        golang \
        libffi-dev \
        openssl-dev \
        python3-dev \
        rust \
    && pip3 install --no-cache-dir \
        acme==${ACME_VERSION} \
        certbot==${CERTBOT_VERSION} \
        certbot-dns-azure==${CERTBOT_DNS_AZURE_VERSION} \
        certbot-dns-eurodns==${CERTBOT_DNS_EURODNS_VERSION} \
        certbot-dns-gehirn==${CERTBOT_VERSION} \
        certbot-dns-hurricane-electric==${CERTBOT_DNS_HURRICANE_ELECTRIC_VERSION} \
        certbot-dns-multi==${CERTBOT_DNS_MULTI_VERSION} \
        certbot-dns-norisnetwork==${CERTBOT_DNS_NORISNETWORK_VERSION} \
        cryptography==${CRYPTOGRAPHY_VERSION} \
    && apk del .build-deps \
    && rm -rf /root/.cache

# Copy data
COPY rootfs /
