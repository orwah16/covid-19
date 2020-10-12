pipeline {
    agent { docker { image 'python:3.7.6' } }
    stages {
        stage('build') {
            steps {
                sh 'pip3 install flask'
                sh 'pip3 install requests'

            }
        }
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
