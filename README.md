# LocalProxy

LocalProxy is a Python command-line tool for managing and applying proxy configurations. It allows you to set, list, and clear proxy settings, which are stored in a configuration file and can be easily applied to your environment.

## Features

- Set HTTP and HTTPS proxy configurations
- List existing proxy configurations
- Clear all proxy configurations
- Apply proxy settings to the environment in other projects

## Installation

### Prerequisites

- Python 3.8 or higher
- Poetry for package management

### Steps

1. Clone the repository:

```bash
git clone https://github.com/EvensXia/localproxy.git
cd localproxy
```

2. Install the project using Poetry:


```bash
poetry install
```

3. Build the project:

```bash
poetry build
```

4. Install the built wheel file:


```bash
pip install dist/localproxy-0.1.0-py3-none-any.whl
```

## Usage
### Command-Line Interface

- List existing proxy configurations:
```bash
localproxy list
```

- Set a proxy configuration:
```bash
localproxy set <protocol> <address>
```
Example:
```bash
localproxy set http http://localhost:8080
```


- Clear all proxy configurations:
```bash
localproxy clear
```

- Run scripts/code/modules:
```bash
localproxy /path/to/your/script.py
localproxy -c "import requests;print(requests.get('https://www.google.com'))"
localproxy -m your.module
```


- Print CLI help:
```bash
localproxy -h
```

### Using the Proxy in Other Projects


In your other Python projects, you can import and apply the proxy settings as follows:

```python
from localproxy import proxy

proxy.init()

```
This will apply the proxy settings stored in ~/.localproxy/proxy.toml to your environment variables.

### Configuration
Proxy configurations are stored in a TOML file located at ~/.localproxy/proxy.toml. This file is managed automatically by the CLI commands.
