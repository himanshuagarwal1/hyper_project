
def check_resources(deployment):
    """
    Check if a cluster has sufficient resources for the deployment.
    """
    cluster = deployment.cluster
    if (cluster.available_ram >= deployment.required_ram and 
        cluster.available_cpu >= deployment.required_cpu and 
        cluster.available_gpu >= deployment.required_gpu):
        return True
    return False


def allocate_resources(deployment):
    """
    Allocate resources from the cluster for a new deployment.
    """
    cluster = deployment.cluster
    cluster.available_ram -= deployment.required_ram
    cluster.available_cpu -= deployment.required_cpu
    cluster.available_gpu -= deployment.required_gpu
    cluster.save()





def single_deployment(deployment):
    
    if check_resources(deployment):
        allocate_resources(deployment)
        deployment.status = 'running'
        deployment.save()
    