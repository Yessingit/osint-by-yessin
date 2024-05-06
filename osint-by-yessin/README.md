# OSINT Tool by Yessin (https://github.com/Yessingit)

## Overview

This is a simple OSINT (Open Source Intelligence) tool developed by Yessin. It allows users to perform Google searches and extract relevant links from the search results. The tool provides a colorful and user-friendly interface for conducting OSINT investigations.

## Features

- Perform Google searches with specific queries.
- Extract links from the search results.
- Automatically save search results to text files.
- Clear terminal screen for a clean interface.
- Easy-to-use interface with colorful output.

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Yessingit/osint-by-yessin
    ```

2. Navigate to the project directory:

    ```bash
    cd osint-by-yessin
    ```

3. Give the setup file permissions

    ```bash
    chmod +x setup.sh
    ```

4. Install the required dependencies:

    ```bash
    ./setup.sh
    ```

5. Run the tool:

    ```bash
    python osint-by-yessin.py
    ```

## Usage

1. Run the script `osint-by-yessin.py`.
2. Enter your search query when prompted.
3. Wait for the tool to perform the search and extract links.
4. View the extracted links in the terminal.
5. Press Enter to continue and perform another search, or press Ctrl+C to exit.

## Dependencies

- colorama
- googlesearch-python
- requests
- beautifulsoup4

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with any improvements or features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
