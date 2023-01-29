pipeline{
    agent any
    stages('Clon Repository'){
        /*Cloning the repository*/
        steps{
            checkout scm
        }

    }

    stages('Build Image'){
        steps{
            sh 'docker build -t streamlit .'

        }
    }
    stages('Run Image'){
        steps{
            sh 'docker run -d -p 8501:8501' --name aswin-streamlit streamlit

        }
    }
    stages('Testing'){
        steps{
            echo 'process completed and deployed'
        }

    }
    }

}
