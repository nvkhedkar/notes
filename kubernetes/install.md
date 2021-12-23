# Kubernetes installation ubuntu 20.04

[instructions](https://computingforgeeks.com/deploy-kubernetes-cluster-on-ubuntu-with-kubeadm/)

## Turn off swap


## Start cluster
sudo kubeadm init \
  --pod-network-cidr=192.168.1.0/24 \
  --upload-certs \
  --control-plane-endpoint=k8s-cluster.pratham.com