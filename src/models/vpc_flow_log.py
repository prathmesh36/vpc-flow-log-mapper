from dataclasses import dataclass
from typing import Optional

@dataclass
class VPCFlowLog:
    version: Optional[int] = None
    account_id: Optional[str] = None
    interface_id: Optional[str] = None
    srcaddr: Optional[str] = None
    dstaddr: Optional[str] = None
    srcport: Optional[int] = None
    dstport: Optional[int] = None
    protocol: Optional[int] = None
    packets: Optional[int] = None
    bytes: Optional[int] = None
    start: Optional[int] = None
    end: Optional[int] = None
    action: Optional[str] = None
    log_status: Optional[str] = None
    vpc_id: Optional[str] = None
    subnet_id: Optional[str] = None
    instance_id: Optional[str] = None
    tcp_flags: Optional[int] = None
    type: Optional[str] = None
    pkt_srcaddr: Optional[str] = None
    pkt_dstaddr: Optional[str] = None
    region: Optional[str] = None
    az_id: Optional[str] = None
    sublocation_type: Optional[str] = None
    sublocation_id: Optional[str] = None
    pkt_src_aws_service: Optional[str] = None
    pkt_dst_aws_service: Optional[str] = None
    flow_direction: Optional[str] = None
    traffic_path: Optional[int] = None
    ecs_cluster_arn: Optional[str] = None
    ecs_cluster_name: Optional[str] = None
    ecs_container_instance_arn: Optional[str] = None
    ecs_container_instance_id: Optional[str] = None
    ecs_container_id: Optional[str] = None
    ecs_second_container_id: Optional[str] = None
    ecs_service_name: Optional[str] = None
    ecs_task_definition_arn: Optional[str] = None
    ecs_task_arn: Optional[str] = None
    ecs_task_id: Optional[str] = None

