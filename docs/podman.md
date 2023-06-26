# Podman

### requirements
- installed podman & podman-compose on your system
- **install** section from *readme.md* completed


### Build
```bash
podman build -t template-django -f Containerfile
```

### Start django in podman
```bash
podman run -p 8080:8000 template-django:latest
```
Try after starting: http://localhost:8080/api/v1/coreapp/

### Start in podman-compose

```bash
podman-compose up -d
```
Try after starting: http://localhost:8000/api/v1/coreapp/