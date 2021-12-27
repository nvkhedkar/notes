# Kubernetes installation ubuntu 20.04

- [instructions](https://computingforgeeks.com/deploy-kubernetes-cluster-on-ubuntu-with-kubeadm/)
- [Setup on virtualbox](https://www.itwonderlab.com/en/ansible-kubernetes-vagrant-tutorial/) - Also has networking info
- [v1beta1 go info](https://pkg.go.dev/k8s.io/kubernetes/cmd/kubeadm/app/apis/kubeadm/v1beta1)

## Manage firewalls
[manage firewalls](https://help.replicated.com/community/t/managing-firewalls-with-ufw-on-kubernetes/230)  
## Turn off swap

```
sudo swapoff -a
```

```
sudo apt install net-tools
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```
```
sudo tee /etc/sysctl.d/k8s.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```
```
sudo sysctl --system
```
```
sudo modprobe overlay ; sudo modprobe br_netfilter
```

```
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt update
```
## Start cluster
```
sudo kubeadm init \
  --pod-network-cidr=192.168.1.0/24 \
  --upload-certs \
  --control-plane-endpoint=k8s-cluster.pratham.com
```

```
sudo kubeadm init --pod-network-cidr=192.168.1.0/24 --upload-certs --control-plane-endpoint=k8s-cluster.pratham.com
```

## temp

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of the control-plane node running the following command on each as root:

  kubeadm join k8s-cluster.pratham.com:6443 --token qsiqsl.jmlni5usb8rqbd6p \
	--discovery-token-ca-cert-hash sha256:6572bc0c143c59d888acd700e8c9d7cf9b328cf2b922a172a3e362177752cea4 \
	--control-plane --certificate-key 434e5eda9bb4e810f7e075088ea31d240768b3f613a1f314ea7fad5c76beb6a1

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
"kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join k8s-cluster.pratham.com:6443 --token qsiqsl.jmlni5usb8rqbd6p \
	--discovery-token-ca-cert-hash sha256:6572bc0c143c59d888acd700e8c9d7cf9b328cf2b922a172a3e362177752cea4 
