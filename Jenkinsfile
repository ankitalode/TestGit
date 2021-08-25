pipeline {
  agent { docker { image 'mvn_3.8:latest' } }
  stages {
    stage('log version info') {
       steps {
        sh 'mvn --version'
      }
    }
  }
}
