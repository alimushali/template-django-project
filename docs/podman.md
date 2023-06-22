# Quickstart

## Building 

```bash
podman build -t template-django -f Containerfile
```


## Start
```bash
podman run -p 8080:8000 template-django:latest
```