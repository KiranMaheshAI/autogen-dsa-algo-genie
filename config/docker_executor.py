from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

from config.constant import TIMEOUT, WORK_DIR

def get_docker_executor():
    """
    Function to get the Docker command line code executor.
    This executor will run the code in a Docker container.
    """

    docker_executor = DockerCommandLineCodeExecutor(
        work_dir=WORK_DIR,
        timeout=TIMEOUT,  # Timeout in seconds
    )
    return docker_executor