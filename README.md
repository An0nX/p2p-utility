# P2P Utility

## Overview

P2P Utility is a FastAPI-based application that provides functionalities for command execution, filesystem access, and video streaming. This application is designed to be easily extensible and configurable, suitable for various P2P network operations.

## Features

- **Command Execution**: Execute system commands via API calls.
- **Filesystem Access**: Upload, download, list, and delete files and directories.
- **Video Streaming**: Stream video data efficiently over the network.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/An0nX/p2p-utility.git
   cd p2p-utility
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   uvicorn app.__main__:app --host 0.0.0.0 --port 8000
   ```

## Configuration

The application configuration is managed via environment variables. You can set these variables in a `.env` file:

- `APP_NAME`: Name of the application.
- `VERSION`: Version of the application.
- `DESCRIPTION`: Description of the application.
- `HOST`: Host address to run the application.
- `PORT`: Port number for the application.

## API Endpoints

### Command Execution

- **POST /cmd/**: Execute a system command.

### Filesystem Access

- **GET /fs/list**: List directory contents.
- **POST /fs/upload**: Upload a file.
- **GET /fs/download**: Download a file.
- **DELETE /fs/delete**: Delete a file or directory.

### Video Streaming

- **POST /stream/**: Stream video data.

## Testing

To run the test suite, use the following command:

```bash
pytest
```

## Contributing

Contributions are welcome! Please create a pull request or file an issue for any bugs or feature requests.