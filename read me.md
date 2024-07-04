# All in One Documentation

## Notes:
This document serves as an all in one guide to continue/get started with or replicate the work done by the Nova interns in June/July of 2024.
## Fluree Server Image from Docker:
![Docker Icon](https://www.docker.com/wp-content/uploads/2023/08/logo-guide-logos-1.svg)

### To create a Fluree Server image from Docker:
-  Ensure you have **Docker** installed.
-  Open a Command Line Interface(CLI) such as Command Prompt (Windows) or Terminal (Mac)
-  Adjust and run the following command:
- **docker run --name fluree_server3 -p 58090:8090 fluree/server**
    -  The “-p” command specifies the port the server will use locally.
    -  The text following “–name” is the name of the Docker container pulled from the Fluree server image. This can be changed depending on the user’ preference.
    -  Docker will automatically pull the fluree/server and run it if it is not found on
        your local device.
    -  In your CLI you can type **“docker ps”** this should show the running server.
    - You can now send HTTP requests to the local URL which has been created using port 58090, or another port depending on which one you specified.


## 