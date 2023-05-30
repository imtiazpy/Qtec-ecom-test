# ecom-filter-test

Short project description.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Running with Docker](#running-with-docker)
  - [Running without Docker](#running-without-docker)

## Prerequisites

Before running the project, make sure you have the following installed on your machine:

- Python 3.9
- Pipenv
- (Optional) Docker and Docker Compose

## Getting Started

Follow the instructions below to get the project up and running.

### Running with Docker

1. Install Docker and Docker Compose on your machine. You can download Docker Desktop from the official Docker website: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. Clone the project repository:
git clone https://github.com/your-username/project.git 

3. Navigate to the project's root directory: cd project

4. Build the Docker image and start the containers: docker-compose up

This command will build the Docker image and create the necessary containers for the project. It will also start the Django development server.

5. Open your web browser and access the project at [http://localhost:8000](http://localhost:8000).

6. (Optional) To populate the database with initial data, open another terminal or command prompt and run the following commands. You must strictly follow the order in which these commands are executed:

- Categories and Brands:

  ```
  docker-compose run web python manage.py loaddata categories_brands.json
  ```

- Sellers:

  ```
  docker-compose run web python manage.py loaddata sellers.json
  ```

- Products:

  ```
  docker-compose run web python manage.py loaddata products.json
  ```

These commands will execute the respective `loaddata` commands within the Docker container and populate the database.

### Running without Docker

1. Clone the project repository: git clone https://github.com/your-username/project.git

2. Navigate to the project's root directory: cd project

3. Create a virtual environment and activate it: pipenv shell

4. Install project dependencies: pipenv install

5. Set up the Environment Variables:

   - Create a `.env` file in the project's root directory.
   
   - Copy the contents of `env.example` into the newly created `.env` file.
   
   - Generate a secret key using any online Django Secret Key generator. or

   - You can run this command: 
   
     ```
     python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
   - Replace the value of `SECRET_KEY` with the newly generated secret key in the `.env` file. (no space between between variable, = and value)
   
     ```
     SECRET_KEY=your_secret_key_here
     ```

6. Apply the database migrations: python manage.py migrate

6. (Optional) Populate the database with initial data, You must strictly follow the order in which these commands are executed:

- Categories and Brands:

  ```
  python manage.py loaddata categories_brands.json
  ```

- Sellers:

  ```
  python manage.py loaddata sellers.json
  ```

- Products:

  ```
  python manage.py loaddata products.json
  ```

These commands will load the fixture data into the database.

7. Start the Django development server: python manage.py runserver

8. Open your web browser and access the project at [http://localhost:8000](http://localhost:8000).

9. To stop the Django development server, press `Ctrl + C` in the terminal or command prompt.





