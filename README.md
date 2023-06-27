# FediseerDocker
Docker container for performing fediseer updates



## Using with kubernetes

### fediseer-config.yaml

Kubernetes manifests are provided in [/k8s_manifests](k8s_manifests)

Edit the `fediseer-config` and `fediseer-secrets` and enter the settings for your instance.

Once done, apply the manifests
