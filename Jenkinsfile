pipeline {
  agent any
  
  stages {
    dir('packages/tajweed_rules_library') {
      stage('Setup') {
        steps {
          echo 'Setup..'
            sh 'python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt'
        }
      }
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
      // stage('Push to') {
      //   steps {
      //     echo 'Deploying....'
      //   }
      // }
    }
  }
}

// def String getEntityArgument() {
//   return sys.argv[3]
// }