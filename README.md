# Microservice Flask Project

This project is a microservices architecture-based system using Flask, designed to manage users and their roles. It consists of two separate Flask applications: `roles` and `users`. The system leverages a shared database module for managing database entities and their relationships, which is included as a submodule from the following repository: `https://github.com/omarmohsen179/microservice-models-flask.git`.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them:

- Python 3.8 or newer
- Flask
- Git

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the main project repository:
   ```
   git clone <Your Main Project Repository URL>
   ```
2. Enter the project directory:
   ```
   cd <Your Project Directory>
   ```
3. Clone the submodule for the shared database module:
   ```
   git submodule add https://github.com/omarmohsen179/microservice-models-flask.git path/to/your/directory
   git submodule init
   git submodule update
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Applications

To run the `users` and `roles` applications, navigate to each app's directory and execute the following command:

```
flask run
```

Make sure to configure each application to run on different ports if you are running both on the same machine for development purposes.

## Usage

Provide examples of how to use your project for various tasks, which could include creating new users, assigning roles, etc.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/tags).

## Authors

- **Your Name** - _Initial work_ - [YourUsername](https://github.com/YourUsername)

See also the list of [contributors](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
