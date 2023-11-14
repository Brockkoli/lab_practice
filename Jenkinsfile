pipeline {
    agent any
    environment {
        // Replace with your actual Python path
        PATH = "/usr/bin/python:$PATH"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/Brockkoli/lab_practice'
            }
        }

        stage('OWASP DependencyCheck') {
            steps {
                dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'OWASP test'
            }
        }

        // Add a new stage for running Python tests
        stage('Run Python Tests') {
            steps {
                sh 'apk update && apk add python'
                sh 'python -m test_ui' // Replace with your Python test command
            }
        }
    }   
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
