pipeline {
    agent any
    environment {
        // Replace with your actual Python path
        PATH = "/usr/bin/python3:$PATH"
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
                sh 'python3 -m test_ui.py' // Replace with your Python test command
            }
        }
    }   
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
