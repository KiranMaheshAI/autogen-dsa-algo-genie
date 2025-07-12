async def start_docker_container(docker):
    print("Starting a Docker container...")
    await docker.start()

async def stop_docker_container(docker):
    print("Stopping the Docker container...")
    await docker.stop()
    print("Docker container stopped.")