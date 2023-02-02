pipeline{
    agent any
    stages{
    stage('Clon Repository'){
        /*Cloning the repository*/
        steps{
            checkout scm
        }

    }

    stage('Build Image'){
        steps{
            sh 'sudo docker build -t streamlit .'

        }
    }
    stage('Run Image'){
        steps{

            sh 'ansible-playbook  ./playbook-for-deployment.yml'

           

        }
    }
    stage('Testing'){
        steps{
            echo 'Process completed and deployed'
        }
    
    }
    }

    
    
    

}
