pipeline {
    agent any

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                echo 'Descargando la receta de BurgerCode...'
                checkout scm
            }
        }

        stage('Build (Cocinar)') {
            steps {
                echo 'Cocinando la imagen Docker...'
                sh 'docker build -t burgercode-app .'
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Probando la hamburguesa...'
                // Ejecutamos el test DENTRO del contenedor
                sh 'docker run --rm burgercode-app python test.py'
            }
        }

        stage('Deploy (Entrega)') {
            steps {
                echo 'Desplegando en Producción...'
                sh 'docker rm -f burger-prod || true'
                sh 'docker run -d --name burger-prod -p 5000:5000 burgercode-app'
                echo '¡Hamburguesa servida en http://localhost:5000!'
            }
        }
    }

    // El bloque post va AQUÍ, después de cerrar "stages" pero antes de cerrar "pipeline"
    post {
        always {
            echo 'Limpiando la cocina...'
            sh 'docker image prune -f'
        }
        success {
            echo '🎉 ¡Pipeline completado con éxito!'
        }
        failure {
            echo '🚑 ¡ALERTA! El pipeline ha fallado. Revisar logs.'
        }
    }
}
