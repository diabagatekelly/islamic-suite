pipeline {
  agent any

  stages {
    when {
      anyOf {
        branch 'prod'
        branch 'PR-*'
      }
    }
    stage('Setup') {
      steps {
        echo 'Testing..'
        sh 'cd packages/tajweed_rules_library/ && source venv/Scripts/activate'
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


#Build:single:  sh python -m src.app run_app prod ''
#Build:all: sh 

#Coverage: sh 