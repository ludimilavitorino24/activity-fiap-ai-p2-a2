# activity-fiap-ai-p2-a2

## User Guide

### Requirements and dependencies

To use this project effectively, you need:

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **Docker**: Ensure Docker is installed on your system.

### Installation

To install and run the application, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ludimilavitorino24/activity-fiap-ai-p2-a2.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd activity-fiap-ai-p2-a2
    ```
3. **(Optional) Create and activate a virtual environment**:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```
4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
5. **Set environment variables**:
    ```sh
    cp .env.example .env
    ```
    Edit the `.env` file and set the environment variables as needed.

6. **Run Postgers server using Docker Container**
    ```sh
    docker compose up -d
    ```
6. **Populate initial database**:
    ```sh
    python3 src/populate_db.py
    ```

### Usage

Run the following command:

```sh
python src/main.py
```

### Querying

The script, `db_example.py`, demonstrates how to query data from a database, such as animals.

To run this script, follow these steps:

1. Execute the script by running the command `python src/db_example.py`.
2. The script will connect to the database and retrieve animal data based on the provided query.
3. The queried animal data will be displayed in the console.

Note: This script can be used as a reference for querying any type of data from a database.
