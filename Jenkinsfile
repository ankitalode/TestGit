pipeline{
    agent any
stages{
    stage('validation'){
        step{
	    sh 'python3 --version'
	}
    }
    stage('execute'){
        steps{
	sh 'ls -ltr'
	sh 'python3 test.py'   
	}
    }
    stage('post action'){
       steps{
          sh 'echo job completed'
       }
    }
}
}
