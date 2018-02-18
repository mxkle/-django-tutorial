pipeline {
  agent {
    docker {
      image 'python:3'
      args '-v /django-tutorial/app/:/app -p 5000:5000'
    }
    
  }
  stages {
    stage('Build') {
      steps {
        sh 'python3 myproject/manage.py runserver 0:5000'
      }
    }
  }
}