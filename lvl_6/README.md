# Prerequisites

- A computer (`About This Mac` -> macOS Monterey 12.5 / Apple M1 Pro / 16 GB)
- VSCode (`code -v` -> 1.87.2)
- Docker (`docker --version` -> 23.0.3)
- Node.js (lts/hydrogen)
    - I'm using: 20.11.1

## NEW

- node open-container-workspace.js

## FOR REFERENCE BUT NOT TOO RELEVANT

- docker build -t agent-api-v6 --target=debugger . 
- docker images <!-- to find the IMAGE ID -->
- docker run -p 5678:5678 <IMAGE_ID> ./src/main.py
- ie: docker run -p 5678:5678 9e7d7edafccf ./watcher.py
- pip show urllib3

## Relevant docs to my troubleshooting process

- https://code.visualstudio.com/docs/python/debugging
- https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/debugpy/2024.0.0/vspackage?targetPlatform=alpine-arm64
- https://code.visualstudio.com/docs/devcontainers/create-dev-container
- https://code.visualstudio.com/docs/devcontainers/containers
- https://containers.dev/implementors/json_reference/#image-specific
- https://github.com/microsoft/vscode-remote-try-python/blob/main/.devcontainer/devcontainer.json
- https://github.com/microsoft/vscode-remote-try-node

## Breakthrough!

- "alpine" Linux images are missing libraries needed by the Python `debugpy` debugger
- ie: "slim" Python packages support debugging
- https://www.youtube.com/watch?v=b1RavPr_878 (Get Started with Dev Containers in VS Code)
- https://www.youtube.com/watch?v=Fc6TAahZ1Pk (Different Ways to Run Dev Containers: VS Code vs CLI)
- https://github.com/microsoft/vscode-remote-release/issues/2133#issuecomment-782021860 (Node.js script to launch our devcontainer directly in VSCode)
