pipeline {
  agent any
  stages {
    stage(checkout) {
      steps {
       echo "hello telugu wolrd"
       }
     } 
   }
}
