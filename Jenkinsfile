pipeline {
  agent any
  
  stages {
    stage('Setup') {
      stages {
        stage('Test') {
          steps {
            echo 'Testing..'
            sh 'python -m unittest -v'
          }
        }
        stage('Test:coverage') {
          steps {
            echo 'Test coverage'
            sh 'coverage run -m unittest && coverage report --omit=*factory.py,*app.py,*test_*.py,src/*__init__.py,src/*/__init__.py'
          }
        }
        stage('Build') {
          steps {
            echo 'Building entities rules JSON files'
            sh 'python -m src.app run_app prod sys.argv[3]'
          }
        }
      }
    }
  }
}