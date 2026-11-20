pipeline {
    agent any

    environment {
        APP_NAME = 'ev3-securedev'
    }

    stages {
        stage('Build') {
            steps {
                bat 'docker build -t %APP_NAME% .'
            }
        }

        stage('Test') {
            steps {
                bat 'docker run --rm %APP_NAME% python -m py_compile app.py'
            }
        }

        stage('Security Review (SonarQube)') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        bat "\"${scannerHome}\\bin\\sonar-scanner.bat\" -Dsonar.projectKey=ev3-securedev -Dsonar.sources=."
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f flask-app %APP_NAME% 2>nul || exit 0'
                bat 'docker run -d --name %APP_NAME% -p 5000:5000 %APP_NAME%'
            }
        }
    }
}