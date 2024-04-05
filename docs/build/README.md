# Build manual

## Pre-requirements
  - Docker installed and running 

## Build manual: 
  - Navigate to the root folder of the repository
  - Run the following command to build the application:
  ```
  docker build -t {your-tag} .
  ```
  - Run the following command to push the image to the registry:
  ```
  docker push {your-tag}
  ```

## The deploy file in the current repository uses an image from Serhii's Kushnir personal repository in DockerHub. 

## For any other explanations and conclusions please refer to [Conclusion](../report/README.md)