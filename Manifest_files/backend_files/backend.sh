k create -f secret.yaml -n final
k create -f pvc.yaml -n final
k get pvc -n final
k create -f db-deployment.yaml -n final
k create -f db-service.yaml -n final
k get all -n final
k get pvc -n final