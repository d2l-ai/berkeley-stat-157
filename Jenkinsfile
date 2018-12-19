stage("Build & Publish") {
  node {
    ws('workspace/berkeley-stat-157') {
      checkout scm
      sh "build.sh"
      sh "upload.sh"
    }
  }
}
