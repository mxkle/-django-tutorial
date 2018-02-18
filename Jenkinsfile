pipeline {
  agent {
    docker {
      image 'python:3'
      args '-v /app/:/app -p 5000:5000'
    }
    
  }
  stages {
    stage('Setup') {
      steps {
        dir(path: '/django-tutorial/') {
          pwd(tmp: true)
        }
        
      }
    }
    stage('Build') {
      steps {
        sh 'python3 myproject/manage.py runserver 0:5000'
      }
    }
  }
}