# DevOps-Projects
# VPC and Networking Setup
As per the architectural diagram, I started by creating a custom VPC. Inside the VPC, I set up four subnets — two public and two private.

To allow internet access:

I created an Internet Gateway and attached it to the VPC.

I also set up a NAT Gateway, which I connected to the private subnets via the appropriate route tables.

-Bastion Host
I created and tested a bastion host in one of the public subnets. This host served as a secure jump point to access instances inside the private subnets. SSH access to the private instance was routed through this bastion host, and it worked as expected.

-Private Instance and Web Server Setup
Once the networking was in place and the bastion host was working, I launched a web server instance in the private subnet. I set up a sample website on this instance using a free template from Tooplate (or any other template site). The web server was successfully configured and served the content internally.

-Load Balancer
Next, I created an Application Load Balancer in the public subnets. The load balancer was configured to forward HTTP traffic to the instance running in the private subnet. I verified that the load balancer could access and serve the web content from the private instance to users on the internet.

-Key Pair and SSH Access
To SSH into the instance in the private subnet:

I created a new key pair.

I copied the private key to the bastion host.

From there, I was able to SSH into the private instance using the key, demonstrating secure access through the bastion.

This setup ensured a secure, highly available architecture with public access via a load balancer and protected internal resources using private networking and a bastion host.
