# Podman

### requirements
- installed docker on your system
- docker.service is up
- **install** section from *readme.md* completed


### Build
```bash
docker build . --tag template-django
```

### Start django in podman
```bash
docker run -p 8080:8000 template-django:latest
```
Try after starting: http://localhost:8080/api/v1/coreapp/

