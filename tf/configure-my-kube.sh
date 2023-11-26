#!/usr/bin/env bash

# remove old kube config
rm ~/.kube/config

# update kube config
aws eks --region $(terraform output -raw region) update-kubeconfig \
    --name $(terraform output -raw cluster_name)