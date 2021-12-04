S3bucket = 'tajweed-app'

pipeline {
  environment {
    prodAcctNum = "709910515242"
  }

  agent any
  
  stages {
    stage('Test remote build') {
      steps {
        echo 'Test remote start..'
        dir('packages/tajweed_rules_library') {
          sh "build 'tajweed-app'"
        }
      }
    }
    stage('Test') {
      when {
        anyOf {
          branch 'main'
          branch 'PR-*'
        }
      }
      steps {
        echo 'Testing..'
        dir('packages/tajweed_rules_library') {
          sh 'python -m unittest -v'
        }
      }
    }
    stage('Test:coverage') {
      when {
        anyOf {
          branch 'main'
        }
      }
      steps {
        echo 'Test coverage'
        dir('packages/tajweed_rules_library') {
          sh 'python -m venv venv && source venv/Scripts/activate && pip install -r requirements.txt && coverage run -m unittest && coverage report --omit=*factory.py,*app.py,*test_*.py,src/*__init__.py,src/*/__init__.py'
        }
      }
    }
    stage('Build') {
      // when {
      //   anyOf {
      //     branch 'main'
      //   }
      // }
      steps {
        echo 'Building entities rules JSON files'
        dir('packages/tajweed_rules_library') {
          script {
            def entity = readFile encoding: 'utf-8', file: 'src/prod_build_entities_list.txt'
            echo(entity)
   
            sh "python -m src.app run_app prod ${entity}"
          }
        }
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