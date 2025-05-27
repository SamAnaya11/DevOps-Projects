# Vagrant Multi-VM Environment (CentOS Stream 9)

This project sets up a simple multi-VM development environment using Vagrant and VirtualBox. It provisions three CentOS Stream 9 virtual machines with private networking for local development and testing.

##  Included Virtual Machines

1. **scriptbox**
   - **IP Address:** 192.168.10.12
   - **Hostname:** `scriptbox`
   - **RAM:** 1024 MB
   - **Box:** `eurolinux-vagrant/centos-stream-9`

2. **web01**
   - **IP Address:** 192.168.10.13
   - **Hostname:** `web01`
   - **Box:** `eurolinux-vagrant/centos-stream-9`

3. **web02**
   - **IP Address:** 192.168.10.14
   - **Hostname:** `web02`
   - **Box:** `eurolinux-vagrant/centos-stream-9`
