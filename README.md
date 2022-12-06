# PICRYPT
## Final Project Proposal (ECE 597-NP, Fall 2022)

(By: Aleksei Rutkovskii and Sohan Show)

## Team members:
Aleksei Rutkovskii and Sohan Show

## Problem statement:
In our day to day lives, we always interact with servers to access services. This can be translating texts from one language to another or converting speech to text, doing image processing, or just merely communicating with other people far apart. However, in all these cases above, data might be exposed to the server for a service to be performed. But, with the invention of homomorphic encryption, we can now perform arithmetic operations on encrypted data without the need for it to be decrypted or exposed to the server. This drastically improves privacy protection and helps the user to access services without exposing their raw data. This is what we aim to demonstrate in our project. Our project, PICRYPT, enables users to find the pixel by pixel difference between two images without exposing the real image to the service provider.

## Goals and Motivation:
The idea is to use homomorphic encryption on two images and then send it over to the server (the service provider) which would then perform pixel by pixel subtraction on the two images and return the result back to the client. The client can then decrypt the image and see the result.

The goal of the demo would be to demonstrate that the server is successfully subtracting one image from another one, where both images are homomorphically encrypted. Example of it would be subtracting one image with a moving object from another one with the same background resulting in two versions of the same object a certain distance apart.

## The entire flow would look like this:
Person would upload 2 images of a moving object with the same background Both of them would be Homomorphically Encrypted with client’s secret key Encrypted images would be then send to the server Upon receiving the server would do subtraction of the first encrypted image from the second resulting in a single image Then the new image would send back to the client Client would decrypt the image and see the result of object moving

## Plan for execution:
Create a Proof-of-Concept locally initiating client and server Write script to subtract images and show the output image Apply homomorphic encryption on the original images and do the subtraction on the encrypted images Create Python (Flask) Server on one computer and Client on another computer on the same network to test image exchange between them Develop minimal website locally Host Server on AWS/GCP/Linode server providers, configure the server Integrate website to the server and test the project

## Milestones:
Nov - 09 - 2022: We test out homomorphic encryption on two simple images locally.

Nov - 16 - 2022: We create a local server and test out the pixel by pixel subtraction done on the homomorphic encrypted images and later decrypt it to see if the results match what we desire it to be.

Nov - 23 - 2022: We build out a client - server model. And try to send the images to the server and perform the services and get back a desired result.

Nov - 28 - 2022: Feature testing and debugging if required.

Dec - 05 - 2022: Feature freeze and deployment.

Dec - 06 - 2022 / Dec - 08 - 2022: Demo Day


## How to run the code:
In one terminal, run the API from root directory:
```python3 api/run.py```

In another terminal, run the client from root directory:
```python3 client/main.py```