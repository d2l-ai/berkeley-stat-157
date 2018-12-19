stage("Build & Publish") {
  node {
    ws('workspace/berkeley-stat-157') {
      checkout scm
      sh "./build.sh"
      sh """#!/bin/bash
      set -ex
      if [[ ${env.BRANCH_NAME} == master ]]; then
          ./upload.sh
      fi
      """
    }
  }
}
