This README file provides instructions on how to set up a Python virtual environment for the project.

# Instructions to set up the virtual environment:

1. Open your terminal or command prompt.
2. Navigate to the project directory where this README file is located.
3. Run the following command to create a virtual environment named 'venv':
    ```
    py -m venv venv
    ```
    This command uses the `venv` module to create a virtual environment in the current directory.

4. Once the virtual environment is created, you can activate it using the following command:
    - On Windows:
      ```
      .\venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```
      source venv/bin/activate
      ```

5. After activating the virtual environment, you can install the required dependencies for your project using `pip`:
    ```
    pip install -r requirements.txt
    ```

6. Execute the pytest command to run tests and generate a report:
    ```
    pytest --html=reports/index.html
    ```

7. To deactivate the virtual environment, simply run:
    ```
    deactivate
    ```

Make sure to activate the virtual environment whenever you work on this project to ensure that you are using the correct dependencies.