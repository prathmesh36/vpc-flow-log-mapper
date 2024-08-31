# vpc-flow-log-mapper
 CLI application for mapping vpc flow logs

## How to run the project?
There are two ways to run the project:
1. Run the python file directly. 
```bash
python vpc_flow_log_mapper.py --input-file-path=static/inputs/sample1.log --output-dir-path=static/outputs/
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

