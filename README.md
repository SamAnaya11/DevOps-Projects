# Terraform AWS Setup
This project sets up basic AWS infrastructure using Terraform. It includes provider configuration, key pair creation, and a security group with custom ingress and egress rules.

What This Project Does
Initializes AWS as the cloud provider.

Sets the AWS region.

Creates an EC2 key pair using a public key.

Configures a security group (dove-sg) with specific rules for SSH, HTTP, and unrestricted outbound access.

File Structure
provider.tf
Defines the AWS provider and specifies the region for resource deployment.

keypair.tf

Creates an EC2 key pair.

Uses a public key generated via the ssh-keygen command.

The content of the generated public key is included in this file.

security-group.tf (assumed name based on context)

Creates a security group named dove-sg.

Includes the following rules:

Ingress:

TCP port 22 (SSH) allowed from your IP.

TCP port 80 (HTTP) allowed from anywhere.

Egress:

All traffic allowed for both IPv4 and IPv6.
