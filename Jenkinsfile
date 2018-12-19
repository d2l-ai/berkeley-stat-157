stage("Build & Publish") {
  node {
    ws('workspace/berkeley-stat-157') {
      checkout scm
      sh "build/build.sh"
      sh """#!/bin/bash
      set -ex
      if [[ ${env.BRANCH_NAME} == master ]]; then
          conda activate berkeley-stat-157
          build/upload.sh
      fi
      """
    }
  }
}
