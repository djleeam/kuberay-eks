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

* `skaffold run -p operator`
* Confirm that the operator is running in the `default` namespace: `kubectl get pods`
```
# NAME                                READY   STATUS    RESTARTS   AGE
# kuberay-operator-7fbdbf8c89-pt8bk   1/1     Running   0          27s
```

Sample configs: https://github.com/ray-project/kuberay/tree/master/ray-operator/config/samples

## RayServe Examples

Run `skaffold run -p serve` to deploy models

### Mobilenet App

Port forward to mobilenet head node

```
kubectl port-forward $(kubectl get pod --selector=ray.io/node-type=head --output=json | jq -r '.items[] | select(.metadata.name | startswith("rayservice-mobilenet")) | .metadata.name') 8000:8000
```

Make a test request to the mobilenet app
```
. ./venv/bin/activate
python apps/mobilenet/mobilenet_req.py
```

## RayJob Examples

https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayjob-quick-start.html