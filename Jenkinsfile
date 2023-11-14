pipeline {
    agent any
    environment {
        // Ensure the PATH includes the directory where Python is installed
        PATH = "/usr/bin:$PATH"
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

        // Run Python Tests
        stage('UI Test') {
            steps {
                        sh 'python -m test_ui'
            }
        }
    }   
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
