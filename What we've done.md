# What has been done during June/July of 2024:

## Fluree

- The interns created a Fluree server on their local devices using the Fluree Server image from Docker Hub.
- The aia ontology has been converted from turtle format to JSON-LD (JavaScript Object Notation for Linked Data).
  - JSON-LD is one of Fluree's most well-documented notations to interact with a Fluree ledger and there is a lot of source material. We also found it easier to understand and read than the alternatives. 
- Played around with how properties from the aia ontology as well as different external ontologies can be leveraged through queries.


## Postman

- We have created a Postman workspace to allow collaboration and coordination on handling HTTP requests to the Fluree Server. Postman allows you to enter the body and header section of an HTTP request. As well as easily convert the request to other formats such as curl. 
- Created an aia-o cookbook in Postman that contains some important HTTP requests for adding the ontology to Fluree, this can be found [here](https://documenter.getpostman.com/view/36457813/2sA3dyiBBW).


## What needs to be done:
- Get the aia ontology ledger on the Digital Ocean droplet.  This can be done either by packaging a container that contains the ledger and running this container on the droplet server.  Alternatively, a fluree/server image can be pulled to the droplet itself and then using curl commands the ledger can be created and populated.

- Make sure all updates made to the ontology (whether on hyperledger or in the .owl file) are reflected in the fluree ledger creation transactions.

- Work on improving the security of the ledger by restricting access through API keys (only people with the keys can make certain changes/see certain information).

- Work on improving the integrity of the ledger by utilising SHACL definitions to make sure data entered follows the correct structure/ is of the correct types.

- Getting started with the Gold Standard Projects and creating new entities and relationships for these documents. 
