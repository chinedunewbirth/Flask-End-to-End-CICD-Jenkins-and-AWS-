pipeline {
    agent any

    environment {
        APP_DIR = "/home/ubuntu/Flask-jenkins-aws-app"
    }

    stages {
        stage('Clone Repo') {
            steps {
            sshagent(['github-ssh-key']) {
                    git branch: 'main', credentialsId: 'github-ssh-key', url: 'git@github.com:chinedunewbirth/Flask-jenkins-aws-app.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest discover tests || true'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                pkill gunicorn || true
                gunicorn -w 4 -b 0.0.0.0:5000 app:app --daemon
                '''
            }
        }
    }
}
