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

## CHALLENGE

vscode-remote://attached-container+<CONTAINER_ID><PATH_IN_CONTAINER_TO_OPEN>

ie: code --folder-uri vscode-remote://attached-container+ca95e31618d6a73d3fffbffedad6715d1f9675a3581c449f9ba581e6da8fb9e7/usr/src/app

code --folder-uri vscode-remote://attached-container+ca95e31618d6a73d3fffbffedad6715d1f9675a3581c449f9ba581e6da8fb9e7/usr/src/app