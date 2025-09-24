# Lab 3

## Team Members
- Prital Jariwala
- Lucas Greer

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?
    RESTful APIs are scalable because of they are stateless- each interaction is indepedent, meaning that the server does not have to remember previous interactions. This allows for the server to handle increased traffic. 

Question 2: According to the definition of "resources" provided in the AWS article above, What are the resources the mail server is providing to clients?
    By the definition, the mail server is providing the resources of emails, attachments, files, mailboxes, etc. These resources are accessed by the client by interacting with HTTP methods such as GET, POST, DELETE, etc. 

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
    We do not use the PUT method in our mail server. We could extend our mail server to use this method by allowing the client to update the ID of the email if there is a more effective system of sorting the emails. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!
    The API key is used to authenticate the source from which the request to the server is coming. Without API keys, there is no way to identify whether or not the request is coming from a legitimate source, which would be an area of concern for APIs holding sensitive information. 

    Source: https://cloud.google.com/endpoints/docs/openapi/when-why-api-key