pipeline {
  agent { dockerfile true }
  stages {
    stage('log version info') {
       steps {
        sh 'mvn --version'
      }
    }
  }
}
