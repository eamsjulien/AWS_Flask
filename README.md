# AWS_Flask

Basic backend Flask server to serve results from the [AWS_FaceDetect](https://github.com/eamsjulien/AWS_FaceDetect) project.

## Getting Started

### Prerequisites

- [AWS_FaceDetect](https://github.com/eamsjulien/AWS_FaceDetect)
- Linux >= 4.17.11
- Bash >= 4.4.23
- Python >= 3.7.0
- Flask >= 1.0.2
- Click >= 6.7
- itsdangerous >= 0.24
- Jinja2 >= 2.10
- MarkupSafe >= 1.0
- Werkzeug >= 0.14.1

An interface with a public IP also required if you want to access your results outside your local network. Please ensure that no firewall rules are preventing outbound/inbound traffic on this interface for port 8080.

### Installing

A step by step series of examples that tell you how to get a development env running.

Simply clone the repository and ensure that you're on the **devel** branch.

```bash
git clone https://github.com/eamsjulien/AWS_Flask.git ; cd AWS_Flask ; git checkout origin/devel
```

Choose a username you want to use as the (only) log-in and run:

```bash
sed -i 's/elab/your-username/g' aws/auth.py
```

Create any configuration file in a folder instance located at the root of the AWS_Flask folder, named instance/config.py. You can put your secret key there.

Next, we need to initialize the database, run:

```bash
export FLASK_APP=aws ; flask init-db
```

You can now register your root user, launch the flask server:

```bash
flask run --host=0.0.0.0 --port=8080
```

Go to your browser, type your server IP address with port 8080 and click on Register to register your root user with a password.

Once all set, just ctrl+c your Flask terminal to kill the Flask application and terminate the setup.

### Running

For the normal use, [AWS_FaceDetect](https://github.com/eamsjulien/AWS_FaceDetect) starts the Flask process via the launch.sh command.

You can always issue a:

```bash
export FLASK_APP=aws ; flask run
```

To test things out but you might encounter issue accessing the index page if AWS_FaceDetect process is not running.