# Serial Proxy

Serial Proxy is a Python package that provides a proxy for serial communication with logging capabilities. It wraps the `pyserial` library and adds automatic logging of all serial operations.

## Installation

You can install the Serial Proxy package using pip:

```
pip install serial-proxy
```

## Usage

Here's a basic example of how to use Serial Proxy:

```python
from serial_proxy import SerialProxy

# Create a SerialProxy instance
proxy = SerialProxy('/dev/ttyUSB0', 9600)

# Use it just like you would use a regular Serial object
proxy.write(b'Hello, world!')
response = proxy.readline()
print(response)

# All operations are automatically logged to 'serial_log.json'
```

## Features

- Wraps all common `pyserial` operations
- Automatic logging of all serial operations to a JSON file
- Context manager support for easy resource management

## License

This project is licensed under the MIT License - see the LICENSE file for details.
