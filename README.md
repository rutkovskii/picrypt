# PICRYPT
## Final Project Proposal (ECE 597-NP, Fall 2022)


## Team members:
[Aleksei Rutkovskii](https://github.com/rutkovskii) and [Sohan Show](https://github.com/sohanshow)


## Python 3.8.10

## Set Up (Linux)
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip3 install -r requirements.txt`
4. `pip3 install git+https://github.com/mastnk/imageshuffle`

## Set Up (Windows)
1. `python -m venv venv`
2. `./venv/Scripts/Activate.ps1`
3. `pip install -r requirements.txt`
4. `pip install git+https://github.com/mastnk/imageshuffle`


## How to run the code:
1. In one terminal, run the API from root directory:
```python3 api/run.py``` or ```python api/run.py```

2. In another terminal, run the client from root directory:
```python3 client/main.py``` or ```python client/main.py```

## When done working:
1. `deactivate`


## Problem statement:
In our day to day lives, we always interact with servers to access services. This can be translating texts from one language to another or converting speech to text, doing image processing, or just merely communicating with other people far apart. However, in all these cases above, data might be exposed to the server for a service to be performed. But, with the invention of homomorphic encryption, we can now perform arithmetic operations on encrypted data without the need for it to be decrypted or exposed to the server. This drastically improves privacy protection and helps the user to access services without exposing their raw data. This is what we aim to demonstrate in our project. Our project, PICRYPT, enables users to find the pixel by pixel difference between two images without exposing the real image to the service provider.

## Goals and Motivation:
The idea is to use homomorphic encryption on two images and then send it over to the server (the service provider) which would then perform pixel by pixel subtraction on the two images and return the result back to the client. The client can then decrypt the image and see the result.

The goal of the demo would be to demonstrate that the server is successfully subtracting one image from another one, where both images are homomorphically encrypted. Example of it would be subtracting one image with a moving object from another one with the same background resulting in two versions of the same object a certain distance apart.

## The entire flow would look like this:
Person would upload 2 images of a moving object with the same background Both of them would be Homomorphically Encrypted with client’s secret key Encrypted images would be then send to the server Upon receiving the server would do subtraction of the first encrypted image from the second resulting in a single image Then the new image would send back to the client Client would decrypt the image and see the result of object moving

## Plan for execution:
Create a Proof-of-Concept locally initiating client and server Write script to subtract images and show the output image Apply homomorphic encryption on the original images and do the subtraction on the encrypted images Create Python (Flask) Server on one computer and Client on another computer on the same network to test image exchange between them Develop minimal website locally Host Server on AWS/GCP/Linode server providers, configure the server Integrate website to the server and test the project

## Encryption Library:
https://github.com/mastnk/imageshuffle

Developed by [Masataka Nakagawa](https://github.com/mastnk) 

[Original Project Page by Masataka Nakagawa](http://www.ok.sc.e.titech.ac.jp/~mtanaka/proj/imagescramble/)

Reference:
Masayuki Tanaka, Learnable Image Encryption, IEEE International Conference on Consumer Electronics TAIWAN (ICCE-TW), 2018.