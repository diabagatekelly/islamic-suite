pipeline {
  agent any
  
  stages {
    stage('Setup') {
      steps {
        echo 'Setup..'
          dir('packages/tajweed_rules_library') {
            sh 'python -m venv venv && source venv/Scripts/activate'
          }
      }
    }
    stage('Test') {
      steps {
        echo 'Testing..'
        dir('packages/tajweed_rules_library') {
          sh 'python -m unittest -v'
        }
      }
    }
    stage('Test:coverage') {
      steps {
        echo 'Test coverage'
        dir('packages/tajweed_rules_library') {
          sh 'pip install -r requirements.txt && coverage run -m unittest && coverage report --omit=*factory.py,*app.py,*test_*.py,src/*__init__.py,src/*/__init__.py'
        }
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

// def String getEntityArgument() {
//   return sys.argv[3]
// }