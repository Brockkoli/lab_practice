pipeline {
	agent any
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
	
                stage('UI Test') {
                        steps {
                            sh 'chmod 777 test_ui.py'  
                            sh 'python test_ui.py'  // Run the Selenium test script
                        }
                }

        }	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}
