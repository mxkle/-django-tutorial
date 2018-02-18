pipeline {
  agent {
    docker {
      image 'python:3'
      args '-p 5000:5000'
    }
    
  }
  stages {
    stage('Setup') {
      steps {
        dir(path: '/django-tutorial/')
      }
    }
    stage('Build') {
      steps {
        sh 'python3 app/myproject/manage.py runserver 0:5000'
      }
    }
  }
}