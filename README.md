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
git clone https://github.com/yourusername/localproxy.git
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
local_proxy list
```

- Set a proxy configuration:
```bash
local_proxy set <protocol> <address>
```
Example:
```bash
local_proxy set http http://localhost:8080
```


- Clear all proxy configurations:
```bash
local_proxy clear
```

### Using the Proxy in Other Projects


In your other Python projects, you can import and apply the proxy settings as follows:

```python
from localproxy import proxy

proxy.init()

```
This will apply the proxy settings stored in ~/.local_proxy/proxy.toml to your environment variables.

### Configuration
Proxy configurations are stored in a TOML file located at ~/.local_proxy/proxy.toml. This file is managed automatically by the CLI commands.
