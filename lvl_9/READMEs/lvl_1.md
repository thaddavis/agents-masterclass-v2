# TLDR
Adding in A.I.

## 1 - Running w/ `docker` command
- add `src/main.py` to get things going
    ```.py
    print('Hey')
    ```
- docker run -v "$PWD":/code python python /code/src/main.py

## 2 - Running w/ `Dockerfile`
- Add `Dockerfile1.dev` ("Select Language Mode" for syntax)
- docker build -f Dockerfile1.dev -t agents-api .
- docker run agents-api

## 3 - Add in Python Packages
- touch requirements.txt
- add `requests` to requirements.txt
- update `src/main.py`
    ```.py
    import requests

    response = requests.get('https://httpbin.org/robots.txt')
    print(response.text)
    ```

### 3a - 1st show the issue
docker run -v "$PWD":/code python python /code/src/main.py (should ERROR X)

### 3a - next show how to download packages and run our code
- Add `Dockerfile2.dev` ("Select Language Mode" for syntax)
- docker build -f Dockerfile2.dev -t agents-api .
- docker run agents-api (should SUCCEED √)

### 3b - next show how to edit and run code
- edit `src/main.py`
    ```.py
    print(response.status_code)
    ```
- docker build -f Dockerfile2.dev -t agents-api .
- docker run agents-api

### 3c - Manually building is ANNOYING! So let's use a file watcher ie: watchfiles
- add `watchfiles` to requirements.txt
- add watcher.py
- docker build -f Dockerfile3.dev -t agents-api .
- docker run -v $(pwd)/src:/code/src agents-api

### 3d - CLIFFHANGER!!!

Notice how our editor is still having issues...

So now let's see how to edit code effectively with containers!
