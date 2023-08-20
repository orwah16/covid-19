pipeline {
  agent {dockerfile true}
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'echo "building the repo"'
            sh "docker build ."
            sh "docker run -dp 127.0.0.1:8000:8000 app"
          }
        }
      }
    }
  
    stage('Test') {
      steps {
        sh 'python3 test.py'
        // input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
        //sh "curl localhost:8080/newCasesPeak?country=israel"
        
      }
    }
  }
  
  //   stage('Deploy')
  //   {
  //     steps {
  //       echo "deploying the application"
  //       sh "sudo nohup python3 app.py > log.txt 2>&1 &"
  //     }
  //   }
  // }
  
  post {
        always {
            echo 'The pipeline completed'
            junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
        }
        success {                   
            echo "Flask Application Up and running!!"
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
      }
}