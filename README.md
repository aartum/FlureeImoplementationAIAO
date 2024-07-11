# All-in-One Documentation

## Introduction:
This document serves as an all-in-one guide to continue/get started with or replicate the work done by the Nova interns in June/July of 2024.

### Contents

 1. [Fluree Server Image with Docker](#docker-img)
 2. [Using Postman to Conduct HTTP Requests](#postman)
    2.1 [Creating a Fluree Ledger using Postman](#postman-create)
    2.2 [The AIA ontology in Postman](#aiao-postman)
    2.3 [Example transaction + fluree transaction syntax](#example)
    2.4 [Exporting a Postman transaction](#export)
 3. [RDF in JSON-LD](#rdf-jsonld)
    3.1 [Properties](#props)
    3.2 [Classes and subclasses](#class)


## 1. Fluree Server Image from Docker: {#docker-img}

<p align="center">
    <img src="https://www.docker.com/wp-content/uploads/2023/08/logo-guide-logos-1.svg" />
</p>

### To create a Fluree Server image from Docker:
- Ensure you have **Docker** installed.
- Open a Command Line Interface (CLI) such as Command Prompt (Windows) or Terminal (Mac).
- Adjust and run the following command:

<pre>
<code id="docker-command">docker run -d -p 58090:8090 --name fluree_server3 fluree/server</code>
</pre>

<div style="background-color: #f0f0f0; border-left: 6px solid #1e90ff; padding: 10px; margin-bottom: 10px;">
  <p style="display: flex; align-items: center;">
    <span style="font-size: 20px; margin-right: 10px;">💡</span>
    <span>NOTE:
    The  <tt>docker run</tt>  command given above does not store any changes made to the container itself or the data it contains. This means if we were to run the container and create a fluree ledger and transact data to this ledger, once the container is stopped (either with the  <tt>docker stop</tt>  command or by accident) the ledger and the data it contains will be lost.  When the container is run again in the future all of the transactions will need to be performed again to add the data.  This is useful when new transactions are tested and one does not want each transaction to make permanent changes to a ledger. Once you are done testing the transactions you simply stop the docker container and don't have to worry about manually cleaning up/deleting files on your local computer.
    </span>
  </p>
</div>

The following command allows you to mount a local directory to ```/opt/fluree-server/data``` inside the container so that the data that Fluree writes to disk can be persisted locally, allowing your data state to be persistent beyond the lifetime of the container itself.

<pre>
<code id="docker-command">docker run -p 58090:8090 -v `pwd`/data:/opt/fluree-server/data fluree/server</code>
</pre>

- The ```-d``` command is used to run the docker container in the background ("detached mode") so that the terminal window can still be used to send more prompts.
- The ```-p``` command specifies the port the server will use locally.
- The text following ```–name``` is the name of the Docker container pulled from the Fluree server image. This can be changed depending on the user’s preference. If not specified, Docker will automatically assign a unique name to the container.
- Docker will automatically pull the latest version of the ```fluree/server``` image and run it if it is not found on your local device.
- In your CLI, you can type ```docker ps``` which should show the running ```fluree/server``` container.
- You can now send HTTP requests to the local URL which has been created using port 58090 (or another port, depending on which one you specified). To view the HTTP API endpoint page, visit [https://localhost:58090](https://localhost:58090).
- To stop the container from running, use the command ```docker stop``` followed by either the ```--name``` specified in the ```run``` command above or the container ID, which can be found by running the ```docker ps``` command. Alternatively, the Docker Desktop interface can be used to run/stop containers or manually pull images from Docker Hub.


<pre>
<code id="docker-command">docker ps</code>
</pre>


A useful intro video on Docker can be found [here](https://www.youtube.com/watch?v=pg19Z8LL06w)

## 2. Using [Postman](https://www.postman.com/) to Conduct HTTP Requests {#postman}

<p align="center">
    <img src="https://blog.postman.com/wp-content/uploads/2014/07/logo.png" />
</p>

<div style="background-color: #f0f0f0; border-left: 6px solid #1e90ff; padding: 10px; margin-bottom: 10px;">
  <p style="display: flex; align-items: center;">
    <span style="font-size: 20px; margin-right: 10px;">💡</span>
    <span>NOTE:
    Before starting with Postman, ensure you have a Fluree server up and running.</span>
  </p>
</div>

I recommend going through Fluree's cookbook example and Forking their Postman collection. The cookbook can be found [here](https://next.developers.flur.ee/docs/reference/cookbook/). Click the orange ```Run in Postman``` button, or alternatively you can fork the collection [here](https://www.svgrepo.com/show/354201/postman.svg).

### 2.1 Creating a Fluree Ledger using Postman {#postman-create}

 1. Create a Collection in Postman
 2. In the newly added collection, add a ```Post``` request

<div style="background-color: #f0f0f0; border-left: 6px solid #1e90ff; padding: 10px; margin-bottom: 10px;">
  <p style="display: flex; align-items: center;">
    <span style="font-size: 20px; margin-right: 10px;">💡</span>
    <span>NOTE:
    There are 3 different types of URLs when interacting with the fluree server. This is an example of the URLs, although the port might look different depending on how you assigned it:
        <ol>
            <li>If this is your first request and you do not have an existing Fluree Ledger: <a href="http://localhost:58090/fluree/create">http://localhost:58090/fluree/create</a></li>
            <li>If you wish to conduct insert, update or delete transactions to your existing ledger: <a href="http://localhost:58090/fluree/transact">http://localhost:58090/fluree/transact</a></li>
            <li>If you want to perform queries on your ledger: <a href="http://localhost:58090/fluree/query">http://localhost:58090/fluree/query</a></li>
        </ol>
    </span>
  </p>
</div>

3.  After using the ```/fluree/create/``` URL you can now type the the body of the HTTP request in JSON-LD format. For more examples of RDF syntax in JSON-LD, see [this](#rdf-jsonld) section
4.  After typing the body you can simply hit the ```Send``` button.

## 2.2 The AIA ontology in Postman {#aiao-postman}
I highly recommend going through the aia "cookbook". It is a thorough and complete overview of how to use Fluree and Postman together and also provides all the needed transactions to add the aia ontology to a Fluree Ledger. The cookbook also provides curl transactions for users who are using the terminal.

The aia ontology cookbook can be found [here](https://documenter.getpostman.com/view/36457813/2sA3dyiBBW).

### 2.3 Example: a simple aia-o transaction (Postman + JSON-LD): {#example}

![insert](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/64ee4710-77ab-457e-b45c-5169ebd04223)

#### Explanation

In the example above we add Bob the farmer. He is 53 years old and works with Tom, who is also a farmer. The above transaction could be a ```create``` request if the ledger "ex_ontology" does not exist yet and the URL in the request is a ```/fluree/create``` URL. It could also be a regular ```insert``` transaction if the URL is ```fluree/transact``` and the ledger exists already.


A normal Fluree insert transaction consists of 3 parts:

1. **The "@context" section:** This section consists of a set of prefixes for URLs. Take a look at the example above: the "ex" is a prefix for ```http://example.org```. Now every time we wish to refer to this particular URL, we only have to use ```ex:```.


<div style="background-color: #f0f0f0; border-left: 6px solid #1e90ff; padding: 10px; margin-bottom: 10px;">
  <p style="display: flex; align-items: center;">
    <span style="font-size: 20px; margin-right: 10px;">💡</span>
    <span>NOTE:
    In every transaction you have to provide the context for each prefix you use again. It is not possible to use ```ex:``` in the next transaction without providing the context for the URL again.</span>
  </p>
</div>


2. **Ledger:** Here you simply provide a new name for the ledger you wish to create, or provide the name of an existing ledger on the Fluree Server to insert Bob the farmer to this ledger.

3.  **Insert**: This keyword specifies what you wish to achieve with this transaction. Each entity you insert should be placed after "insert": in between a set of curly brackets {}. If you are adding more than one entity you simply add another set of curly brackets and place a comma after the previous entity.

    - Each entity/node requires an "@id" which can uniquely identify it in this particular ledger. Because there is no other Bob in this entity we simply use the "@id": "Bob". Bob is not found in the example.org vocabulary, thus he does not use the prefix "ex:".

    - We can give each entity properties for example, name, age, marital status, employment status etc., provided the ```example.org``` vocabulary has a property for age, name and worksWith, and also a class for Farmer. We can assign these properties to Bob.


### 2.4 Exporting a Postman request {#export}
It is possible to convert Postman's requests to other formats such as curl, R (using httr), Python, C# etc.

 1. Click on the request
 2. Select the ```</>``` icon on the right side
 3. Select a format from the drop-down list that will appear
 4. Copy and paste the converted request as needed

![Postman_export](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/3f4706e4-b594-4bba-a309-13a18b00139f)

## RDF vocabulary examples in JSON-LD: {#rdf-jsonld}
### 3.1 RDF Properties: {#props}

![rdf_property](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/8856a5f2-e29e-410b-90a6-14e4165b5c45)

- This adds a property "married", which is an RDF property. It also adds the "married" property for Bob.
- Married is not called from a vocabulary and thus is used without a prefix. This also means this property only exists in the ledger.
- Please note the "rdf" and "rdfs" prefixes in the "@context" section.

### 3.2 RDF Classes and Subclasses: {#class}

#### 3.2.1 RDF Classes
![rdf_Class](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/20d692c7-8731-42ab-bb3e-a6d5031657fb)

- The snippet above assumes there is an entity in the example vocabulary "ex: Location". This entity has type "rdfs:Class".

#### 3.2.2 RDF Subclasses
![rdf_SubClass](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/fc1c56bf-0359-45b7-9687-67d7fdf8d7c1)

- The snippet above assumes Country is also an entity from ```example.org``
 - We want to assign a relationship which states it is a subclass of Location in our dataset. Please take a look at how the syntax and declaration for the "rdfs" subclass work in the example above.

#### 3.2.3 Inserting data using the Classes: {#data-in}
![class_dataInsert](https://github.com/aartum/FlureeImplementationAIAO/assets/143713572/57315fd9-efdc-486f-9e37-888187678cda)

- We can simply now add "South-Africa" as an entity which is of type "ex:Country" and then by the rules we provided is a subclass of "ex:Location".


