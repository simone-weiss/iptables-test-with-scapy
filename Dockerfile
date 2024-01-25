FROM ubuntu:20.04

# install dependencies

# install tools needed for generated firewall tests
RUN apt update && \
  DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt upgrade -y && \
  DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt install -y python3 python3-pip \
    sudo iproute2 iptables ethtool

# create work folder and user
RUN useradd -r -u 1000 -g users -G sudo user && \
  mkdir -p /firewall_test && \
  chown -R user /firewall_test
RUN pip install scapy

ADD iptables_test.py /firewall_test/
ADD iptables_setup.sh /firewall_test/

WORKDIR /firewall_test/
RUN sudo chmod +x iptables_setup.sh
USER user

 
CMD ./iptables_setup.sh && python3 iptables_test.py

