# vpc-flow-log-mapper
 CLI application for mapping vpc flow logs

## How to run the project?
```bash
python vpc_flow_log_mapper.py
```

  ### Specify custom input file path, output directory path and custom vpc-flow-log fields
  ```bash
  python vpc_flow_log_mapper.py --input-file-path=static/inputs/sample2.log --output-dir-path=static/outputs/ --fields="dstport protocol packets bytes start end action log-status"
  ```

  ```bash
  python vpc_flow_log_mapper.py --input-file-path=static/inputs/sample1.log --output-dir-path=static/outputs/ --fields="version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status"
  ```

## How to run the project as a python package?

1. Create a virtual env
```bash
python -m venv venv
```

2. Activate the virtual env

    Windows
    ```bash
    venv\Scripts\activate
    ```

    Linux/Mac OS
    ```bash
    source venv/bin/activate
    ```

3. Install the Project using pip
```bash
  pip install -e .
```

4. Run the cli application
```bash
vpc-flow-log-mapper --input-file-path=static/inputs/sample1.log --output-dir-path=static/outputs/ 
```


## Project Structure

The project structure is as follows:
- **`venv/`**: Contains the virtual environment for Python dependencies. This directory is created by running `python -m venv venv`.

- **`src/`**: The source code for the project.
  - **`__init__.py`**: Marks the directory as a Python package.
  - **`main.py`**: The main entry point for the cli application which accepts the cli arguments.
  - **`utils/`**: A utils submodule directory contains various utility function needed in the mapping of VPC flow log files to the required output format.
  - **`models/`**: A models submodule directory has the VPCFLowLog data class which contains all the possible fields in a VPC flow log file as per the [AWS Flow Log Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html).
  - **`services/`**: A services submodule directory contains the service layer code which interacts with various utility function to provide service to end user.
  - **`constant/`**: A constants submodule directory contains the protocol name-number mapping given [here](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).

- **`static/`**: The source code for the project.
  - **`inputs/`**: This directory contains various sample vpc flow log files to test. This directory contains the default sample vpc-flow-log-file. You can add your sample files here or use any other directory by mentioning in the command line argument.
  - **`outputs/`**: This directory is the default output directory. You can use some other directory by specifying in the command line argument
  - **`mapping/`**: The main entry point for the cli application which accepts the cli arguments.

- **`README.md`**: Provides documentation and information about the project.

- **`.gitignore`**: Specifies files and directories to be ignored by Git.

- **`setup.py`**: Specifies project packaging details.

- **`vpc_flow_log_mapper.py`**: The file responsible for starting the project.

## Command Line Arguments

| Command Line Argument | Required/Optional | Default Value | Details |
|----------|----------|----------|----------|
| --input-file-path | Optional | static/inputs/sample1.log | This argument asks for the input file path |
| --output-dir-path | Optional | static/outputs/ | This argument asks for the output directory path |
| --fields | Optional | version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status | The argument asks for the fields in your vpc flow log file in the same order |