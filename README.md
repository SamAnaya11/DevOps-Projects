# DevOps-Projects
# GitOps-Based Infrastructure and Application Deployment on Kubernetes
This project demonstrates a GitOps-driven deployment architecture leveraging GitHub Actions, Terraform, Amazon EKS, Helm, and SonarCloud. It splits responsibilities between two dedicated Git repositories—one for infrastructure as code (IaC) and another for application code—automating changes from code commit to live deployment.

Architecture Overview
The system is structured around two separate Git repositories:

Infrastructure Repository: Contains Terraform code for provisioning cloud infrastructure.

Application Repository: Contains source code, Dockerfile, Kubernetes manifests, and Helm Charts for the application.

Each repository includes a GitHub Actions workflow that automates the detection of changes, validation, and deployment based on Git events and branch policies.


Infrastructure Pipeline (Terraform Git Repository)
The infrastructure codebase uses Terraform to manage AWS resources, particularly the VPC and EKS cluster. It follows a multi-branch workflow strategy, utilizing both stage and main branches to control testing and production deployment flows.

Changes pushed to the stage branch trigger validation-only workflows, including terraform validate and terraform plan.

Once validated, changes are merged into the main branch through a pull request, which must be approved by a maintainer.

Upon merge, the GitHub Actions workflow applies the Terraform plan from the main branch directly to the AWS environment.

Backend state management is configured using an S3 bucket, defined via secrets.

The EKS cluster kubeconfig is retrieved post-deployment, and an NGINX ingress controller is installed if the cluster is provisioned successfully.


Application Pipeline (App Code Repository)
The application repository includes source code, Dockerfile, and Kubernetes Helm Charts. It supports a complete CI/CD workflow from build to deployment.

Code is analyzed using Checkstyle and SonarCloud for static code quality checks.

On successful validation, a Docker image is built and pushed to Amazon ECR.

Helm Charts are used to define and deploy the Kubernetes application, dynamically referencing the newly created Docker image tag.

The same tag used during the build is automatically passed into Helm, ensuring the Kubernetes deployment uses the correct image version.

The deployment targets the EKS cluster previously provisioned via Terraform.


Workflow Highlights
Two Repositories: Clear separation of concerns between infrastructure and application logic.

Branch Strategy: stage for validation, main for actual deployments.

Approval Gate: Pull request-based control over production infrastructure changes.

Terraform Automation: End-to-end IaC validation and application through GitHub Actions.

Static Code Analysis: Integration with SonarCloud ensures quality before deployment.

Containerization: Dockerized application images managed through ECR.

Helm Deployment: Parameterized Helm charts streamline Kubernetes deployments.

Dynamic Versioning: Image tags passed automatically to match deployed versions.


Key Components and Tools
GitHub Actions – CI/CD workflows for infrastructure and application

Terraform – Infrastructure provisioning (AWS VPC, EKS)

Amazon EKS – Kubernetes cluster hosting the application

Amazon ECR – Container registry for application images

SonarCloud – Static code analysis and quality gate enforcement

Helm – Kubernetes deployment manager

Docker – Application containerization

NGINX Ingress – Load balancing and routing for application traffic


