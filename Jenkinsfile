pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
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