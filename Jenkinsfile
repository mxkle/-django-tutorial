pipeline {
  agent {
    docker {
      image 'python:3'
      args '-v /app:/app -p 5000:5000'
    }

  }
  stages {
    stage('build') {
      steps {
        sh 'pip install --no-cache-dir -r app/requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python3 app/myproject/manage.py test'
      }
    }
    stage('run') {
      steps {
        sh 'python3 app/myproject/manage.py runserver 0:5000'
      }
    }
  }
}
