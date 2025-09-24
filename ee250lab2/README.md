# Lab 2

## Team Members
- Prital Jariwala
- Lucas Greer

## Lab Question Answers

Answer for Question 1: 

QA.1 - When we added 50% loss to our local environment, we lost 50% of the packets we were sending. This occurred because UDP does not prioritize reliability. Therefore, in a lossy environment, half of the packets are completely missing. 

QA.2 - For TCP protocol, when we added 50% loss to the local environment, the reliability of the transmission did not change, and packets were not lost. 

QA.3 - As mentioned in the response to the previous question, the speed of the transmissions dropped significantly. However, packets were not lost, as TCP establishes a connection and continuously resends the packets until they are received. 

QA.4 - For this lab, I used LLM's to help learn about the lab questions and how to answer them only after finding insufficient information in google searches. 


QC.1 - argc defines the number of command line arguments passed in the command to run the server. *argv[] defines the actual arguments passed in the command line. For example, when we write ./tcp_server 12345, we pass in two arguments in argc, and *argv[] is a pointer array that contains the actual arguments themselves, ./tcp_server and 12345. 

QC.2 - A Unix file descriptor allows for an integer to be assigned to a file, which allows for the operating system to open and interact with that file (depending on the descriptor). A file descriptor table keeps track of all the open/accessible files. Each process run on the operating system has its own file descriptor table, allowing it to keep track of all of its files and the important information for each of them. 

QC.3 - A struct in C is type of data that the user can define to be a collection of multiple different data types in one entity. For example, a struct called student can contain an integer type with the student's ID, a string type with their name, etc. The struct sockaddr_in variables specifically define the information relating to the server and client addresses. The struct sockaddr_in variable contains variables of type int, char, etc (IP address family, port number, nested struct with IP address, and padding for the field). 

QC.4 - The input parameters of socket are the internet domain, the type of connection (TCP, UDP), and the protocol for the given connection type. 

QC.5 - The input parameters of bind() are sockfd, address, and address length, where sockfd is the identifier integer of the socket. The struct address contains all the information about the connection location (port, IP address). The input parameters of listen() are sockfd, which contains all the information about the socket. The other parameter is the backlog integer, which allows for a specific amount of connections to be formed. 

QC.6 - The while(1) is used so that the server can listen continuously for the client while the program is running. However, running a while loop means that only one client can be heard at a time. In order to accept a new client, the program will have to be quit and re run. 

QC.7 - The command fork() works by starting a new "child" process that is identical to the original process in order for multiple clients to be accepted by the server. Additionally, each process is completely independent. 