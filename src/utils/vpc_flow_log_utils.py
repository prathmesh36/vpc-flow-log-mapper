from typing import List, Tuple
import inspect
from ..models.vpc_flow_log import VPCFlowLog
import csv
import os
from pathlib import Path
from ..constants import vpc_flow_log_constants
from typing import List, Optional
from collections import defaultdict


def get_protocol_name(protocol_number: int) -> str:
    return vpc_flow_log_constants.protocol_mapping.get(protocol_number, "Unknown Protocol")


def handle_hypen_data(data: dict) -> dict:
    return {k.replace('-', '_'): v for k, v in data.items()}

def map_vpc_flow_log_line(log_line: str, field_format: Tuple[str], delimiter: str = ' ') -> VPCFlowLog:
    try:
        log_values = log_line.split(delimiter)
        if len(field_format) == len(log_values):
            log_data = {field: value for field, value in zip(field_format, log_values)}
            int_fields = get_int_fields(VPCFlowLog)
            for field in int_fields:
                if field in log_data and log_data[field].isdigit():
                    log_data[field] = int(log_data[field])
            log_data_hypen_handled = handle_hypen_data(log_data)
            return VPCFlowLog(**log_data_hypen_handled)
        else:
            raise Exception("no. of given fields and the no. of fields in log file do not match")
    except Exception as e:
        print("Mapping the VPC flow log lines failed for the following reason: " + str(e))
        raise e

def read_vpc_flow_logs(file_path: str, field_format: Tuple[str], delimiter: str = ' ') -> List[VPCFlowLog]:
    try:
        vpc_flow_logs = []
        
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = map_vpc_flow_log_line(line.strip(), field_format, delimiter)
                vpc_flow_logs.append(log_entry)
        
        return vpc_flow_logs
    except Exception as e:
        print("Reading the VPC flow log file failed for the following reason: " + str(e))
        raise e

def get_int_fields(cls) -> List[str]:
    try:
        int_fields = []
        constructor_signature = inspect.signature(cls.__init__)
        
        for param_name, param in constructor_signature.parameters.items():
            if param.annotation == int or param.annotation == Optional[int]:
                int_fields.append(param_name)
        
        return int_fields
    except Exception as e:
        print("Getting Integer fields for the class failed for the following reason: " + str(e))
        raise e

def load_csv_to_dict_list(filename: str) -> dict:
    try:
        data = []
        
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            for row in reader:
                if len(row) == len(header):
                    data.append(dict(zip(header, row)))
        return create_tag_mapper(data)
    except Exception as e:
        print("Loading CSV data to dictionary list failed for the following reason: " + str(e))
        raise e

def create_tag_mapper(data: List[dict]) -> dict:
    try:
        mapper = {}
        for record in data:
            mapper[(record["dstport"], record["protocol"])] = record["tag"]
        return mapper
    except Exception as e:
        print("Creating lookup table dictionary failed for the following reason: " + str(e))
        raise e

def generate_output_data(tag_mapping: dict, logs: List[VPCFlowLog]):
    output_tag_count = defaultdict(int)
    output_port_protocol_comb_count = defaultdict(int)
    for log in logs:
        tag = tag_mapping.get((str(log.dstport), get_protocol_name(log.protocol)))
        output_port_protocol_comb_count[(str(log.dstport), get_protocol_name(log.protocol))] += 1
        if tag:
            output_tag_count[tag] += 1
        else:
            output_tag_count["Untagged"] += 1
    return output_tag_count, output_port_protocol_comb_count

def write_dict_to_csv(file_path: str, data: dict, header: List[str]):
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
        
            for key, value in data.items():
                if isinstance(key, tuple):
                    key_columns = list(key)
                else:
                    key_columns = [key]
                
                writer.writerow(key_columns + [value])
    except Exception as e:
        print("Writing output to CSV file failed for the following reason: " + str(e))
        raise e
            
def validate_vpc_flow_log_mapper_inputs(input_file_path: str, output_dir_path: str) -> Tuple:
    try:
        output_dir_path_validation = os.path.exists(output_dir_path) 
        input_file = Path(input_file_path)
        input_file_path_validation = input_file.is_file()
        if output_dir_path_validation and input_file_path_validation:
            return (True, "Validation Successful")
        else:
            if not input_file_path_validation and not output_dir_path_validation:
                return (False, "Input file path --input-file-path & Output directory path --output-dir-path does not exist")
            elif not input_file_path_validation:
                return (False, "Input file path --input-file-path does not exist")
            else:
                return (False, "Output directory path --output-dir-path does not exist")
    except Exception as e:
        print("Validation for vpc-flow-log-mapper failed for the following reason: " + str(e))
        raise e