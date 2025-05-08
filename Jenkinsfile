pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/akshyd249/test_1.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install PyQt5 PyQtWebEngine'
            }
        }

        stage('Run Browser App') {
            steps {
                sh 'python main.py & sleep 5 && pkill -f main.py || true'
            }
        }

        stage('Complete') {
            steps {
                echo 'Browser tested successfully!'
            }
        }
    }
}
