
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub code downloaded successfully!'
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage started!'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing application!'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage started!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
