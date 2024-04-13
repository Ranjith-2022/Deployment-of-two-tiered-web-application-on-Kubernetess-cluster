k create -f secret-for-sqldb.yaml -n final
k create -f pvc-for-sqldb.yaml -n final
k get pvc -n final