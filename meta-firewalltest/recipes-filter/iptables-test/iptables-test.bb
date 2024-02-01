# Copyright (C) 2024 Simone Weiss <simone.weiss@elektrobit.com>
# Released under the MIT license (see COPYING.MIT for the terms)

SUMMARY = "Install scapy script for testing an example firewall"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

RDEPENDS:${PN} = "python3-core python3-scapy"

SRC_URI = "file://send_egress.py \
           file://sniff_ingress.py \
          "

do_install () {
    install -dm755 ${D}${base_sbindir}
    install -Dm755 ${WORKDIR}/send_egress.py ${D}${base_sbindir}
    install -Dm755 ${WORKDIR}/sniff_ingress.py ${D}${base_sbindir}
}

