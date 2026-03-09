pipeline {
    // Le decimos a Jenkins que use cualquier agente disponible
    agent any

    stages {
        stage('Checkout (Ingredientes)') {
            steps {
                // Jenkins descarga el código automáticamente aquí
                echo 'Descargando la receta de BurgerCode...'
                checkout scm
            }
        }

        stage('Build (Cocinar)') {
            steps {
                echo 'Cocinando la imagen Docker...'
                // Construimos la imagen y le ponemos la etiqueta "burgercode-app"
                sh 'docker build -t burgercode-app .'
            }
        }

        stage('Test (Control de Calidad)') {
            steps {
                echo 'Probando la hamburguesa...'
                // Ejecutamos el archivo test.py. Si esto falla, el pipeline explota (se detiene).
                sh 'docker run --rm burgercode-app python test.py'
            }
        }

        stage('Deploy (Entrega)') {
            steps {
                echo 'Desplegando en Producción...'
                // 1. Intentamos detener y borrar una versión vieja si existe (el || true evita que de error si no existe)
                sh 'docker rm -f burger-prod || true'
                // 2. Ejecutamos la nueva versión en el puerto 5000
                sh 'docker run -d --name burger-prod -p 5000:5000 burgercode-app'
                echo '¡Hamburguesa servida en http://localhost:5000!'
            }
        }
    }
    pipeline {
    agent any
    stages {
        // ... (tus stages anteriores siguen aquí) ...
    }
    
    // NUEVO BLOQUE: Se ejecuta siempre al terminar, pase lo que pase.
    post {
        always {
            echo 'Limpiando la cocina...'
            // Borra imágenes "sueltas" que ya no se usan para liberar espacio
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
}
