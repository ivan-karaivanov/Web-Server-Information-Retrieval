# Web Server Information Retrieval Tool

## Overview

The Web Server Information Retrieval Tool is a Python script designed to gather information about web servers specified in a text file ("recon.txt"). It sends HTTP GET requests to the provided URLs, retrieves the server headers, and prints a footprint report for each web server.

## Key Features

- Reads the list of URLs from "recon.txt."
- Sends HTTP GET requests to each URL.
- Retrieves and displays the headers of the server responses.

## Usage

1. Ensure that the "recon.txt" file contains a list of your URLs, each on a new line.
2. Run the script.
3. View the footprint report for each web server.

## Example

```bash
Footprint report for http://google.com Web Server:
Server : nginx
Content-Type : text/html
...

Footprint report for http://facebook.com Web Server:
Server : Apache
Content-Type : application/json
...
Dependencies
requests: Used for making HTTP requests.

## Contributing
Contributions are welcome! If you find issues or have suggestions for improvements, please follow the guidelines in the Contributing document.

## License
This project is licensed under the MIT License.
