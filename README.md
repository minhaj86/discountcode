# How to setup

**Requirements**

Docker


**Database**

Run database with docker like below:

`docker run --name discountcodedb -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=usr -e POSTGRES_DB=discountcodedb -p 5432:5432 -d postgres
`

Get the IP address of postgres container like below:

`docker inspect -f '{{.NetworkSettings.IPAddress }}' discountcodedb
`

**REST API**

Build the API container:

Use docker build to build the docker image for REST container like below:

`docker build -t discountcodeimg .
`

Run the built container and pass the IP of db container from step above:

`docker run -e DBHOST=A.B.C.D --name discountcodeapi discountcodeimg
`

# API Description

There are two different APIs ,

**Generate a discount code**

First one is for submitting request to generate discount code
for a specific brand using the brand ID which is stored in the brand table. As seed data 
7 brand is pre-pushed with sequential IDs. Brand ID and 
number of discount code to be generated is passed as URL parameter as an HTTP POST request using the 
below URL format:

`http://HOST-NAME:5000:/discountcode/brand/generate/<brandid>/<count>
`

For example, to generate 20 discount codes against first brand (setupdb.py script will insert H&M as the first brand as 
part of seed data), submit a POST request with CURL like below:

`curl -v -X POST http://127.0.0.1:5000/discountcode/brand/generate/1/20
`

This call will create 20 discount codes and store it in database with state UNUSED

**Fetch a discount code**

Second one is for fetching a discount code for a specific brand. Brand ID needs to be 
provided as URL parameter against which a valid discount code will be returned 
as JSON payload. URL format is like below:

`http://HOST-NAME:5000:/discountcode/brand/fetch/<brandid>
`

To fetch a discount code against a brand, submit a GET request with CURL like below:

`curl -v  http://127.0.0.1:5000/discountcode/brand/fetch/1
`

A discount code will be returned within JSON payload and it will be marked as DISTRIBUTED in database.

