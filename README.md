# DevOps-Projects
# Microservices-Based Web Application Deployment on Kubernetes
This project demonstrates the deployment of a Spring MVC web application using a Kubernetes-based microservices architecture. The system integrates essential backend services such as a relational database, caching, messaging, and search, deployed and orchestrated across individual pods with inter-service communication enabled through Kubernetes networking.

Project Overview
The application is developed using Java with the Spring MVC framework, employing additional Spring components like Spring Security for authentication and Spring Data JPA for ORM. The front-end is rendered using JSP pages, served via a Tomcat container. The stack is containerized and deployed on Kubernetes, with each major component running in a dedicated pod.

Technologies and Components
Spring MVC – Web application logic

Spring Security – Authentication and authorization

Spring Data JPA – ORM for data persistence

MySQL – Relational database

Memcached – In-memory cache

RabbitMQ – Messaging queue

ElasticSearch – Search and analytics

Apache Tomcat – Servlet container

JSP – Frontend templating

Docker – Containerization

Kubernetes – Container orchestration

Application Architecture
Kubernetes Secrets were used to store database credentials securely.

Persistent Volumes and PVCs were configured for MySQL data storage.

Individual deployments were written for MySQL, Memcached, RabbitMQ, ElasticSearch, and the Spring MVC app.

Internal services enabled communication between components within the cluster.

A Docker image of the Spring application was deployed via Tomcat.

An Ingress resource routed external HTTP traffic to the app.

DNS was configured to point a custom domain to the AWS load balancer backing the Ingress.

Deployment Highlights (From Screenshots)
Cluster initialized using Minikube

Kubernetes manifests applied for all services

Services discovered and listed via kubectl get svc

MySQL pod logs showing successful DB startup and import

Application frontend rendered successfully in browser

ElasticSearch pod in ready state

RabbitMQ initialized and available via admin UI

Memcached in use, with performance benefits confirmed

Application Behavior
Once deployed, the application became externally accessible through a domain name configured to route to the Kubernetes Ingress. All services were actively running in separate pods, with smooth internal communication. RabbitMQ handled background task messaging, Memcached served as an active cache layer, and the Spring application connected to the MySQL database, using ElasticSearch for search functionality.

