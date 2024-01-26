# Copyright (C) 2024 Simone Weiss <simone.weiss@elektrobit.com>
# Released under the MIT license (see COPYING.MIT for the terms)

SUMMARY = "Install scapy script for testing an example firewall"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

DEPENDS = "python3-scapy"

SRC_URI = "file://iptables_test.py"

do_install () {
    install -dm755 ${D}${base_sbindir}
    install -Dm644 ${WORKDIR}/iptables_test.py ${D}${base_sbindir}
}

