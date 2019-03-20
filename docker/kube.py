from kubernetes_py import K8sConfig, K8sContainer, K8sDeployment

# Defaults found in ~/.kube/config
cfg_default = K8sConfig()

container = K8sContainer(name='malmo-me', image='malmo-me:latest')
container.add_port(
    container_port=5901, 
    host_port=5901, 
    name='VNC'
)

container.add_port(
    container_port=6901, 
    host_port=6901, 
    name='noVNC'
)

container.add_port(
    container_port=8888, 
    host_port=8888, 
    name='jupyter-port'
)

deployment = K8sDeployment(
    config=cfg_default, 
    name='malmo-me',
    replicas=1
)
deployment.add_container(container)
deployment.create()