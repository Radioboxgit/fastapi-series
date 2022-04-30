## This is a repo for fastapi example projects and configurations
projects listed are:
-Fast Api File Upload Example

<details><summary>Fast Api File Upload Example Details</summary>
<p>
#FastAPI File Upload Example Project
in this example,a post endpoint is created that receives a file in the form of json.
The json file is then decoded and stored in a deta base .
The post endpoint returns the filename, filetype, the contentType and the first data entry in the uploaded json file.

it will also raise an http exception if the file type is not of the json format.

see the demo [Here](https://fatapi-file-upload-deta-example.deta.dev/)

##How to replicate the process:
- Register a free Deta account by going to [deta.sh](https://web.deta.sh) 
- install deta cli
- Enter into the project directory, create a main.py file and a requirements.txt file so that deta will be able to install the necessary 
requirements for the micro

- open up a terminal and type the command below:
```
deta new --python

```
The command above tells deta that you want to initialize a new python micro.

After creating a new deta micro, deta will create a **.deta** directory inside the project folder

Deploy the project:

``` 
deta deploy 

```

</p>
</details>