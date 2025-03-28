#Commands for kubernets

`````
kubectl get pods
kubectl apply -f pod.yaml 
    -f is file system triggers kube-api-server --> entire pod information is saved in etcdgit
    --> scheduler find the available worker node to deploy the pod
    --> api-server will send the instruction to the worker node so that it can pick up the data,
    --> once pod is created in worker node then kubectl communicates back api-server(control plane) that pod is sucessfully created
    --> 


kubectl apply -f svc-local.yaml

`````
