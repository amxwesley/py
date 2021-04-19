pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
              //sh 'python -m py_compile sources/add2vals.py sources/calc.py' 
                sh 'python -m py_compile indexes.py'
                sh 'python -m unittest indexes.py'
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}
