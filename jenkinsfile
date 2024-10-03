pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app'
        APP_NAME = 'PythonApp'
    }

    stages {

        // Stage 1: Checkout the Code
        stage('Checkout') {
            steps {
                echo 'Checking out the code from Git...'
                checkout scm
            }
        }

        // Stage 2: Build Docker Image
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} .
                '''
            }
        }

        // Stage 3: Run Unit Tests inside Docker
        stage('Test') {
            steps {
                echo 'Running tests inside Docker container...'
                sh '''
                    docker run --rm ${DOCKER_IMAGE}:${BUILD_NUMBER} pytest tests/
                '''
            }
        }

        // Stage 4: Run the Application in a Docker Container
        stage('Run Application') {
            steps {
                echo 'Running the Docker container...'
                sh '''
                    docker run -d --name ${APP_NAME}_${BUILD_NUMBER} ${DOCKER_IMAGE}:${BUILD_NUMBER}
                '''
            }
        }

    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
            sh 'docker ps -a'
        }
    }
}
