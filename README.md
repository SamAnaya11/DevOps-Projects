# DevOps-Projects
# AWS CI/CD Project
For this project, I set up a CI/CD pipeline using AWS services to automate the build and deployment process.

I started by migrating our Git repositories from GitHub to Bitbucket. Once everything was in Bitbucket, I configured AWS CodePipeline to monitor those repositories for any new commits.

Whenever I push new code to Bitbucket, CodePipeline automatically picks up the changes. It then triggers a build using AWS CodeBuild. I set up CodeBuild to function like a Jenkins server — it pulls the source code, builds it, and outputs an artifact (like a ZIP or JAR file).

Since there’s no default option in CodeBuild to deploy directly to Elastic Beanstalk, I used CodePipeline to handle the deployment step as well. After the build completes, CodePipeline takes the artifact and deploys it to an Elastic Beanstalk environment.

In summary:

I moved our code from GitHub to Bitbucket.

I set up CodePipeline to detect commits in Bitbucket.

CodePipeline triggers CodeBuild, which builds the application.

Finally, CodePipeline deploys the build to AWS Elastic Beanstalk.

This setup gave me a fully automated deployment pipeline, streamlining the release process and removing the need for manual builds or deployments.
