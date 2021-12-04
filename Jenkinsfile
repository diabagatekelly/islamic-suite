S3bucket = 'tajweed-app'

pipeline {
  environment {
    prodAcctNum = "709910515242"
  }

  agent any
  
  stages {
    stage('Test') {
      when {
        anyOf {
          branch 'prod'
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
          branch 'prod'
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
      when {
        anyOf {
          branch 'prod'
        }
      }
      steps {
        echo 'Building entities rules JSON files'
        dir('packages/tajweed_rules_library') {
          script {
            def ENTITY = readFile encoding: 'utf-8', file: 'packages/tajweed_rules_library/src/app.py'
            echo(ENTITY)
            // // Variables for input
            // def inputRule

            // // Get the input
            // def userInput = input(
            //   id: 'userInput', message: "Enter '' or rule:",
            //   parameters: [
            //     string(defaultValue: '',
            //       description: 'Rule',
            //       name: 'Config'),
            //   ])

            // // Save to variables. Default to empty string if not found.
            // inputRule = userInput?:''

            // Echo to console
            echo("IQA Sheet Path: ${inputRule}")
            sh "python -m src.app run_app prod ${inputRule}"
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