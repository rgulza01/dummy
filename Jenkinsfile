pipeline{
  agent any
  environment{
      DATABASE_URI = credentials('DATABASE_URI')
      SECRET_KEY = credentials('SECRET_KEY')
  }
  stages{
    stage('setup'){
      steps{
        sh 'export DATABASE_URI=${DATABASE_URI}'
        sh 'export SECRET_KEY=${SECRET_KEY}'
        sh "sudo apt install python3-venv -y"
        sh "sudo apt install python3-pip -y"
        sh "python3 -m venv venv"
        sh ". venv/bin/activate"
        sh "pip3 install -r requirements.txt"
      }
    }
    stage('docker swarm'){
      steps{
        //   check syntax for tags 
        sh "docker-compose build"
        sh "docker push radiagulzan/feature_1_image"
        sh "docker stack deploy --compose-file docker-compose.yaml stack_name"
      }
    }
  }
}