# RE-DACT

## Project Setup Instructions

To contribute to this project, follow the steps below to set up the project on your local machine:

### 1. Fork the Repository

1. Go to the [RE-DACT GitHub repository](https://github.com/SIH-VIT-24/RE-DACT) and click the "Fork" button in the top-right corner.
2. This will create a copy of the repository under your GitHub account.

### 2. Clone the Forked Repository

1. Open a terminal on your local machine.
2. Run the following command to clone your forked repository:

    ```bash
    git clone https://github.com/<your-username>/RE-DACT.git
    ```
    Replace `<your-username>` with your GitHub username.

3. Navigate to the project directory:

    ```bash
    cd RE-DACT
    ```

### 3. Set Up a Virtual Environment

To manage project dependencies, create a virtual environment:

1. Ensure you have Python 3 installed. You can check your Python version by running:

    ```bash
    python3 --version
    ```

2. Create a virtual environment by running:

    ```bash
    python3 -m venv env
    ```

    Or if `python3` doesn't work, you can try:

    ```bash
    python -m venv env
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source env/bin/activate
        ```

    If the activation command doesn't work on Windows, you might need to change the execution policy:

    - Run PowerShell as an administrator or your IDE shell.
    - Execute the following command:

        ```powershell
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
        ```

    - Press the key for "Yes to All" and then rerun the `.env\Scripts\activate` command in your VS Code terminal.

### 4. Install Dependencies

Once the virtual environment is activated, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 5. Run the Application

To run the application locally, use the following command:

    flask run

And then open localhost:5000 on your web browser.
