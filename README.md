# kuberay-eks

## Provision a k8s cluster (AWS)

### EKS (AWS)

https://developer.hashicorp.com/terraform/tutorials/kubernetes/eks

Provision cluster & configure `kubectl`

* `terraform apply`
* `./configure-my-kube.sh`

### Local k3d 

To create a local Kuberay cluster:
```
k3d cluster create -c ./local/k3d-kuberay.yaml
```

Switch to the `k3d-kuberay` context:
```
kubectx k3d-kuberay
```

To delete the cluster:
```
k3d cluster delete kuberay
```

## Verify cluster

* `kubectl cluster-info`
* `kubectl get nodes`

## Deploy a KubeRay operator

* `skaffold run -p operator`
* Confirm that the operator is running in the `kuberay` namespace: `kubectl get pods -n kuberay`
```
# NAME                                READY   STATUS    RESTARTS   AGE
# kuberay-operator-7fbdbf8c89-pt8bk   1/1     Running   0          27s
```

Helm chart values: https://github.com/ray-project/kuberay/blob/master/helm-chart/kuberay-operator/values.yaml

Sample Ray cluster/job/service configs: https://github.com/ray-project/kuberay/tree/master/ray-operator/config/samples

## Deploy a Ray cluster

* `skaffold run -p cluster`

## Deploy Ray services/apps

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