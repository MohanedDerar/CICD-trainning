from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codeconnections as codeconnections,
)

class PipelineCdkStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeConnections resource called 'CICD_Workshop_Connection'
        SourceConnection = codeconnections.CfnConnection(self, "CICD_Workshop",
                connection_name="CICD_Workshop_Connection",
                provider_type="GitHub",
        )