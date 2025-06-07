# DevOps-Projects
# AWS CI/CD Project
In this project, we're setting up a CI/CD pipeline using AWS services to automate the deployment process.

The source code for our applications is currently on GitHub, but we're migrating everything over to Bitbucket. Once the code is in Bitbucket, we’ll use AWS CodePipeline to detect any new commits.

When there's a new commit in the Bitbucket repository, CodePipeline will kick off the process. It starts by pulling the latest code from Bitbucket and then triggering a build job in AWS CodeBuild. CodeBuild works kind of like Jenkins — it fetches the code, builds it, and produces an artifact (like a ZIP or JAR file).

After the build is complete, we want to deploy the artifact to AWS Elastic Beanstalk. However, there’s no direct option in CodeBuild to deploy to Beanstalk. That’s why we’re using CodePipeline — it connects everything together.

So, to summarize:

We have our Git repositories in Bitbucket.

CodePipeline watches those repos for changes.

On a new commit, it triggers CodeBuild to build the source into an artifact.

Finally, CodePipeline deploys that artifact to AWS Elastic Beanstalk.
