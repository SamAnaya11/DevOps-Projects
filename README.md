# DevOps-Projects
# Jenkins Pipeline Setup with GitHub Integration
This repository contains a simple Jenkins pipeline setup that I created to test automated builds using GitHub and various Jenkins trigger mechanisms.

What I Did
I started by writing a basic Jenkinsfile and pushing it to the repository. The pipeline is minimal—it only includes a single Build stage that echoes a message. This was mainly to confirm that Jenkins could pull and execute the pipeline correctly.

Jenkinsfile Content:
groovy
Copy
Edit
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Build completed."'
            }
        }
    }
}
After pushing the Jenkinsfile to GitHub, I went into Jenkins and created a new pipeline job. I configured it to use the GitHub repository as the source and set it to pull the Jenkinsfile from SCM. Once that was set up, I ran a manual build to verify that Jenkins was able to load the file and run the pipeline without issues.

Next, I focused on setting up different build triggers to automate the process as much as possible:

I configured a GitHub webhook so that Jenkins would automatically trigger a build every time I pushed new code. This involved adding the Jenkins webhook URL to the repository’s settings under Webhooks.

To make sure the webhook would work reliably, I also checked that the GitHub plugin was installed on Jenkins and that it was properly authenticated to access my repository.

As an alternative trigger, I enabled Poll SCM in Jenkins with a simple schedule (H/5 * * * *) so Jenkins would periodically check for changes, just in case webhooks failed.

I also experimented with Build Periodically, scheduling builds even if there were no changes. This was useful for testing and simulating continuous integration behavior.

Finally, I configured the job to trigger builds remotely using an authentication token. This allowed me to start builds using a simple URL, which could be useful for integrations or external automation.

All these configurations helped me test and understand the different ways Jenkins can be triggered, and how it behaves with a basic pipeline setup connected to GitHub.

Final Notes
At this point, I have a functional Jenkins pipeline that:

Runs a basic build step

Supports GitHub webhook triggers

Can poll the SCM

Can run on a schedule

Can be triggered remotely via API

It’s a clean foundation that I can build on later with more complex pipeline stages like testing, packaging, or deploying.
