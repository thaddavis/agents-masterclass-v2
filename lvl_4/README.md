# Prerequisites

VSCode extensions

- @ext:ms-vscode-remote.remote-containers etc.

# How to run this

- docker build -t agent-api-v4 .
- docker run -d -v $(pwd)/src:/usr/src/app/src agent-api-v4
- SHIFT + CMD + P -> `Dev Containers: Attach to Running Container...`
- IN THE CONTAINER
    - Navigate to project location in the container
    - Install desired VSCode extensions into the new VSCode instance...
        - @ext:ms-python.vscode-pylance etc.
        - @ext:ms-python.python

# Experimenting with attaching to the container via a CLI command

- docker inspect

- 