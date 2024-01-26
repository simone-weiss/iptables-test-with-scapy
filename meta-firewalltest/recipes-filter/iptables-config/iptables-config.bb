# Copyright (C) 2024 Simone Weiss <simone.weiss@elektrobit.com>
# Released under the MIT license (see COPYING.MIT for the terms)

SUMMARY = "Install iptables script for testing an example firewall"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI = "file://iptables_setup.sh"


do_install () {
    install -dm755 ${D}${base_sbindir}
    install -Dm755 ${WORKDIR}/iptables_setup.sh ${D}${base_sbindir}
}

