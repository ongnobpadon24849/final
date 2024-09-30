pipeline {
    agent none

    stages {
        stage('Agent Test Server') {
            agent { label 'VM_master' }

            stages {
                stage("Clone Repository From is_prime On GitLab") {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: "Gitlab_ongnobpadon24849", 
                                                            usernameVariable: "GIT_USERNAME", 
                                                            passwordVariable: "GIT_PASSWORD")]) {
                                if (fileExists('final')) {
                                    dir('final') {
                                        sh "git pull origin main"
                                    }
                                } else {
                                    sh "git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com/softdevthree/final.git"
                                }
                            }
                        }
                    }
                }

                stage("Unit Test") {
                    steps {
                        script {
                            dir('final') {
                                sh '''
                                    . /home/master/my_env/bin/activate
                                    python3 /home/master/workspace/JenkinsAndDeploy/final/functiontest.py
                                    '''
                            }
                        }
                    }
                }
                
                stage("Build Docker Image") {
                    steps {
                        script {
                            dir('api_code') {
                                sh "docker build -t flask-app ."
                            }
                        }
                    }
                }

                stage("Run Docker Container") {
                    steps {
                        script {
                            sh "docker ps -a -q -f name=flask-app | xargs -r docker rm -f"
                            sh "docker run -d --name flask-app -p 5000:5000 flask-app"
                        }
                    }
                }

                stage("Clone Repository From final_robot_test") {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: "Gitlab_ongnobpadon24849", 
                                                            usernameVariable: "GIT_USERNAME", 
                                                            passwordVariable: "GIT_PASSWORD")]) {
                                if (fileExists('final_robot_test')) {
                                    dir('final_robot_test') {
                                        sh "git pull origin main"
                                    }
                                } else {
                                    sh "git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@gitlab.com/softdevthree/final_robot_test.git"
                                }
                            }
                        }
                    }
                }

                stage("Run Robot-Test") {
                    steps {
                        dir('final_robot_test') {
                            script {
                                sh '''
                                    . /home/master/my_env/bin/activate
                                    robot /home/master/workspace/JenkinsAndDeploy/final_robot_test/test_final.robot
                                    '''
                            }
                        }
                    }
                }

                stage('Push Docker Image') {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: "Gitlab_ongnobpadon24849", 
                                                            usernameVariable: "GIT_USERNAME", 
                                                            passwordVariable: "GIT_PASSWORD")]) {
                                sh "docker login -u ${GIT_USERNAME} -p ${GIT_PASSWORD} registry.gitlab.com"
                                sh "docker tag flask-app registry.gitlab.com/softdevthree/final"
                                sh "docker push registry.gitlab.com/softdevthree/final"
                            }
                        }
                    }
                }
            }
        }

        stage('Agent Pre-Prod Server') {
            agent { label 'VM_preprod' }
            
            stages {
                stage("Pull Docker Image") {
                    steps {
                        script {
                            withCredentials([usernamePassword(credentialsId: "Gitlab_ongnobpadon24849", 
                                                            usernameVariable: "GIT_USERNAME", 
                                                            passwordVariable: "GIT_PASSWORD")]) {
                                sh "docker login -u ${GIT_USERNAME} -p ${GIT_PASSWORD} registry.gitlab.com"
                                sh "docker pull registry.gitlab.com/softdevthree/final"
                            }
                        }
                    }
                }

                stage("Run Docker Container") {
                    steps {
                        script {
                            sh "docker ps -a -q -f name=flask-app | xargs -r docker rm -f"
                            sh "docker run -d --name flask-app -p 5000:5000 registry.gitlab.com/softdevthree/final"
                        }
                    }
                }
            }
        }
    }
}