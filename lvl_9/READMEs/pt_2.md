# TLDR
Phase 2

# Host Requirements
- A computer (`About This Mac` -> macOS Monterey 12.5 / Apple M1 Pro / 16 GB)
- Docker (`docker --version` -> 23.0.3)
- Visual Studio Code (`code -v` -> 1.87.2)
    - Node.js (lts/iron)
        - I'm using: 20.11.1
- gcloud CLI - 470.0.0

## 1 - We are going to leverage `devcontainers`
- mkdir .devcontainer
- add .devcontainer.json
- This config allows you to open a VSCode instance that is plugged into the container environment instead of to our host 

### Reference links
- https://containers.dev/
- https://www.npmjs.com/package/@devcontainers/cli

## 2 - How to launch an instance of VSCode connected to a project folder running in a Docker container
- Shift + CMD + P
    - `Shell Command: Install 'code command in PATH`
- code --list-extensions
    - `ms-vscode-remote.remote-containers`

- First we'll launch our development container using the VSCode "Command Palette"
- Second we'll launch our development container from the command line

## 2a
- Shift + CMD + P
    - `Dev Containers: Reopen in Container`
- Notice how all the 3rd party packages are being recognized now in VSCode
- The 1st time you launch the devcontainer this will take a few minutes but after that your development container will launch quickly
- python src/main.py

## 2b
- add `open-container-folder.js`
- node open-container-folder.js
- python src/main.py

## 3 - Show working debugger in container

### 3a
- Show via the "Command Palette" - "Run and Debug"

### 3b
- And via `debugpy`
- add `debugpy` to requirements.txt
- pip install -r requirements.txt
- add the following to the entry file
```watcher.py
import debugpy

debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()
```
- "Python Debugger: Remote Attach"

## Conclusion

Ok! So that takes care of explaining the development set up we'll be using for the application we will be building. Let's continue developing by integrating FastAPI and LangChain...

## Caveats
- "alpine" Linux containers are not compatible with the Python debugger
- If switching back to the local environment in necessary OR the "devcontainer" stops working for whatever reason
    - You can close the window and reopen the "devcontainer" from your local project folder
    - Shift + CMD + P
        - `Dev Containers: Reopen Folder Locally`

## Honorable Mention
- https://code.visualstudio.com/docs/devcontainers/containers
- https://www.youtube.com/watch?v=p9L7YFqHGk4 (Customize Dev Containers in VS Code with Dockerfiles and Docker Compose)
- https://www.youtube.com/watch?v=b1RavPr_878 (Get Started with Dev Containers in VS Code)
- https://www.youtube.com/watch?v=Fc6TAahZ1Pk (Different Ways to Run Dev Containers: VS Code vs CLI)
- https://github.com/microsoft/vscode-remote-release/issues/2133#issuecomment-782021860 (Node.js script to launch our devcontainer directly in VSCode)