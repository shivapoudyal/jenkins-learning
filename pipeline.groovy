pipeline{
    agent any

    tools {
        maven 'maven'
    }

    environment {
        git_tag = getLastGitCommitId()
    }
        stages{
            stage("git checkout"){
                steps{
                    git 'https://github.com/shivapoudyal/java-project'
                }
            }

            stage("maven build"){
                steps{
                    sh "mvn clean package"
                }
            }

            stage("docker build"){
                steps{
                    sh "docker build . -t shivapoudyal/jenkins-ansbile-java-project:${git_tag}"
                }
            }

            stage("docker image to docker hub"){
                steps{

                    withCredentials([string(credentialsId: 'docker-hub-pass', variable: 'dockerHubPasw')]) {
                       sh "docker login -u shivapoudyal -p ${dockerHubPasw}"
                    }

                    sh "docker push shivapoudyal/jenkins-ansbile-java-project:${git_tag}"
                }
            }

            stage("deploying to production server"){
                steps{
                    ansiblePlaybook disableHostKeyChecking: true, extras: "-e git_tag=${git_tag}", installation: 'ansible', inventory: 'inventory.txt', playbook: 'play.yml'
                }
            }
        }    
}

    def getLastGitCommitId(){
        def commitId = sh returnStdout: true, script: 'git rev-parse --short HEAD'
        return commitId
    }