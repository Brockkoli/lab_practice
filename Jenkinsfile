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

        // Run Python UI Tests
        stage('UI Test') {
          agent {
            docker {
                image 'python:3.8-slim'
                args '-u root:root'  // Use root to install packages
            }
          }
          steps {
            sh '''
                apt-get update
                apt-get install -y firefox-esr  // Install Firefox ESR
                wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz
                tar -xvzf geckodriver-v0.29.0-linux64.tar.gz
                mv geckodriver /usr/local/bin/
                pip install selenium

                python -m test_ui
            '''
          }
        }
    }   
    post {
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
