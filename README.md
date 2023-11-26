# kuberay-eks

## Provision an EKS cluster (AWS)

https://developer.hashicorp.com/terraform/tutorials/kubernetes/eks

### Provision cluster & configure `kubectl`

* `terraform apply`
* `./configure-my-kube.sh`

### Verify cluster

* `kubectl cluster-info`
* `kubectl get nodes`

### Deploy a KubeRay operator

* `skaffold run`
* Confirm that the operator is running in the `default` namespace: `kubectl get pods`
```
# NAME                                READY   STATUS    RESTARTS   AGE
# kuberay-operator-7fbdbf8c89-pt8bk   1/1     Running   0          27s
```

## RayJob Quickstart

https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayjob-quick-start.html