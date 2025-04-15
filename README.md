# regular-language-converter

A visual NFA to DFA converter available online for everyone's purposes. This project provides a backend API and a simple frontend interface to validate strings against a predefined regular expression. It is designed to help users understand and work with regular languages.

## Features
- Validate strings against a complex regular expression.
- Backend powered by Flask with CORS support.
- Simple frontend interface for user interaction.

## Setup and Installation

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd regular-language-converter
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the backend server:
   ```bash
   make start-backend
   ```

4. Open a browser and navigate to `http://127.0.0.1:5000` to access the frontend interface.

## Usage
- Enter a string in the input field on the frontend interface.
- Click the "Validate" button to check if the string matches the predefined regular expression.
- The result will be displayed below the form.

## Development
- To install dependencies manually, run:
  ```bash
  pip install -r requirements.txt
  ```
- To start the backend server without the Makefile, run:
  ```bash
  python Backend/app.py
  ```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
