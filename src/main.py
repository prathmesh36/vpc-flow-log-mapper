import argparse
from .services import vpc_flow_log_mapper

def main():
    parser = argparse.ArgumentParser(description="The program maps the VPC flow logs and generates the mapping results.")
    parser.add_argument('--input-file-path', type=str, default="static/inputs/sample1.log", help="Input file containing VPC flow logs.")
    parser.add_argument('--output-dir-path', type=str, default="static/outputs/", help="The directory path where the output files would be saved.")
    parser.add_argument('--fields', type=str, default="version account-id interface-id srcaddr dstaddr srcport dstport protocol packets bytes start end action log-status", help="--fields argument captures the format of the VPC flow logs, specifically, the name and the order of the fields in the input VPC flow logs")
    args = parser.parse_args()
    vpc_flow_log_mapper.map_vpc_flow_logs(args.fields, args.input_file_path, args.output_dir_path)
    
if __name__ == "__main__":
    main()