from ..utils.vpc_flow_log_utils import generate_output_data, read_vpc_flow_logs, load_csv_to_dict_list, validate_vpc_flow_log_mapper_inputs, write_dict_to_csv
import datetime


def map_vpc_flow_logs(fields_str: str, input_file_path: str, output_dir_path: str) -> None:
    try:
        # Input Validation
        validation_result = validate_vpc_flow_log_mapper_inputs(input_file_path, output_dir_path)
        if validation_result[0]:
            # Fetching Inputs
            fields = tuple(x for x in fields_str.split())
            
            #Reading Input Log File
            logs = read_vpc_flow_logs(input_file_path, fields, ' ')
            
            # Fetching Lookup table
            tag_mapping = load_csv_to_dict_list("static/mappings/lookup_mapping_table.csv") 
            
            # Generating Output Data
            output_tag_count, output_port_protocol_comb_count = generate_output_data(tag_mapping, logs)               
            
            # Creating Output Files
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file1_name = f'{timestamp}_output1.csv'
            output_file2_name = f'{timestamp}_output2.csv'
            write_dict_to_csv(output_dir_path + output_file1_name, output_tag_count, ["Tag", "Count"])
            write_dict_to_csv(output_dir_path + output_file2_name, output_port_protocol_comb_count, ["Port", "Protocol", "Count"])
            print("Output files " + output_file1_name + ", "  + output_file2_name + " generated at " + output_dir_path)
        else:
            print(validation_result[1])
    except Exception as e:
        print("Mapping failed because of the following error: " + str(e))
        