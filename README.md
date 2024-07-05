# All-in-One Documentation

## Notes:
This document serves as an all-in-one guide to continue/get started with or replicate the work done by the Nova interns in June/July of 2024.
## Fluree Server Image from Docker:
![Docker Icon](https://www.docker.com/wp-content/uploads/2023/08/logo-guide-logos-1.svg)

### To create a Fluree Server image from Docker:
- Ensure you have **Docker** installed.
- Open a Command Line Interface (CLI) such as Command Prompt (Windows) or Terminal (Mac).
- Adjust and run the following command:

<pre>
<code id="docker-command">docker run -d -p 58090:8090 --name fluree_server3 fluree/server</code>
</pre>
<button onclick="copyToClipboard()">Copy</button>

<script>
function copyToClipboard() {
    const code = document.getElementById('docker-command').textContent;
    navigator.clipboard.writeText(code).then(() => {
        alert('Command copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}
</script>

- The “-d” command is used to run the docker container in the background ("detached mode") so that the terminal window can still be used to send more prompts.
- The “-p” command specifies the port the server will use locally.
- The text following “–name” is the name of the Docker container pulled from the Fluree server image. This can be changed depending on the user’s preference. If not specified, Docker will automatically assign a unique name to the container.
- Docker will automatically pull the latest version of the fluree/server image and run it if it is not found on your local device.
- In your CLI, you can type **docker ps** which should show the running fluree/server container.
- You can now send HTTP requests to the local URL which has been created using port 58090, or another port depending on which one you specified. To view the HTTP API endpoint page, visit [https://localhost:58090](https://localhost:58090).
- To stop the container from running, use the command **docker stop** followed by either the "--name" specified in the "run" command above or the container ID, which can be found by running the “docker ps” command. Alternatively, the Docker Desktop interface can be used to run/stop containers or manually pull images from Docker Hub.


[A useful intro video on Docker can be found [here](https://www.youtube.com/watch?v=pg19Z8LL06w)]

## The AIA ontology in Postman
I highly recommend going through the aia "cookbook", it is a thorough and complete overview of how to use Fluree and Postman together and also provides all the needed transactions to add the aia ontology to a Fluree Ledger. The cookbook also provides curl transactions for users who are using the Terminal. 

The aia ontology cookbook can be found [here](https://documenter.getpostman.com/view/36457813/2sA3dyiBBW).

## Using Postman to Conduct HTTP Requests
![Postman Icon](https://blog.postman.com/wp-content/uploads/2014/07/logo.png)

Note: Before starting with Postman ensure you have a Fluree server up and running. 

I recommend going through Fluree's cookbook example and Forking their Postman collection, the cookbook can be found [here](https://next.developers.flur.ee/docs/reference/cookbook/). Click the orange "Run in Postman" button, or alternatively you can fork the collection   [here](https://www.svgrepo.com/show/354201/postman.svg).

### Creating a Fluree Ledger using Postman
- Create a Collection in Postman
- In the newly added collection add a "Post" request
- Note there are 3 different types of URLs when interacting with the fluree server, this is an example of how it might look, although the port might look different depending on how you assigned it:
    - If this is your first request and you do not have an existing Fluree Ledger:  http://localhost:58090/fluree/create.
    - If you wish to conduct insert, update or delete transactions to your existing ledger: http://localhost:58090/fluree/transact.
    - If you want to perform queries on your ledger: http://localhost:58090/fluree/query.
- After using the first URL you can now type the the body of the HTTP request in JSON-LD format.
- After typing the body you can simply hit the send button.

### How a simple transaction might look like (Postman + JSON-LD):

![json_ex](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/e4a8febe-3ca8-4164-83c0-9a6f44cf0d12)

### Break Down:

In the example above we add Bob the farmer, he is 53 years old and works with Tom, who is also a farmer. The above transaction could be a create request if the ledger "ex_ontology" does not exist yet and the URL in the request is a /fluree/create URL, it could also be a regular insert transaction provided the URL is fluree/transact and the ledger does exist already.


A normal Fluree insert transaction consists of 3 parts: 

1. **The "@context" section:** This section consists of a set of prefixes for URLs, please take a look at the example above, the "ex" is a prefix for "http://example.org". Now every time we wish to refer to this particular URL, we only have to use "ex:". Note, that in every transaction you have to provide the context for each prefix you use. It is not possible to use "ex:" in the next transaction without providing the context for the URL again. 

2. **Ledger:** Here you simply provide a new name for the ledger you wish to create or you provide the name of an existing ledger on the Fluree Server to insert Bob the farmer to this ledger.

3.  **Insert**: This keyword specifies what you wish to achieve with this transaction. Each entity you insert should be placed after "insert": in between a set of curly brackets {}. If you are adding more than one entity you simply add another set of curly brackets and place a comma after the previous entity. 

    - Each entity/node requires an "@id" which can uniquely identify it in this particular ledger. Because there is no other Bob in this entity we simply use the "@id": "Bob", Bob is not found in the example.org vocabulary, thus he does not use the prefix "ex:".

    - We can give each entity properties for example, name, age, marital status, employment status etc. Provided the example.org vocabulary has a property for age, name and worksWith and also a class for Farmer. We can assign these properties to Bob. 


## RDF vocabulary examples in JSON-LD:
### Adding RDF Properties:

![rdf_property](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/8856a5f2-e29e-410b-90a6-14e4165b5c45)

- This adds a property "married" which is an RDF property. It also adds the married property of Bob. Married is not called from a vocabulary and thus is used without a prefix. This also means this property only exists in the ledger. Please note the "rdf" and "rdfs" prefixes in the "@context" section.


### RDF Classes and Subclasses:

#### RDF Class
![rdf_Class](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/20d692c7-8731-42ab-bb3e-a6d5031657fb)

- The snippet above assumes there is an entity in the example vocabulary "ex: Location", this entity is declared as "rdfs:Class".

#### RDF Subclass
![rdf_SubClass](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/fc1c56bf-0359-45b7-9687-67d7fdf8d7c1)

- The snippet above assumes Country is also an entity of example.org, we want to assign a relationship which states it is a subclass of Location in our dataset. Please take a look at how the syntax and declaration for the "rdfs" subclass works in the example above. 

#### Inserting data using the Classes:
![class_dataInsert](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/57315fd9-efdc-486f-9e37-888187678cda)

- We can simply now add "South-Africa" as an entity which is of type "ex:Country" and then by the rules we provided is a subclass of "ex:Location".

### Exporting a Postman request
It is certainly possible to convert Postman's requests to other formats such as curl, R (using httr), Python, C# etc. 
- This is achieved by clicking on the request and on the right-hand side of the Postman application is a "</>" icon. Click this and on the top left of the newly opened screen is a drop-down list of the various formats Postman can convert a request to:

![Postman_export](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/3f4706e4-b594-4bba-a309-13a18b00139f)

- Simply copy and paste the converted request where needed.


