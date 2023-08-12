# Minikube

### requirements
- **build** section from *docs/podman.md* completed
- installed minikube & kubectl on your system


### setup
```bash
minikube start
kubectl create deployment minikuber-django --image-pull-policy="never" --image=localhost/template-django:latest
kubectl expose deployment minikuber-django --type=NodePort --port=8000
```

### run
```bash
minikube start
kubectl get services minikuber-django # check if app is up
kubectl port-forward service/minikuber-django 8080:8000
```