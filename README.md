# FediseerDocker
Docker container for performing fediseer updates



## Using with kubernetes

### fediseer-config.yaml
``` yaml title="fediseer-config.yaml"
apiVersion: v1
kind: ConfigMap
metadata:
  name: fediseer-config
  namespace: lemmy
data:
  FEDISEER_MIN_ENDORSEMENTS: "0"
  FEDISEER_ENABLE_BLACKLIST: "true"
  FEDISEER_ENABLE_WHITELIST: "false"

  # If there's this many registered users per local post+comments, this site will be considered suspicious
  ACTIVITY_SUSPICION: "20"

  # If there's this many registered users per active monthly user, this site will be considered suspicious
  MONTHLY_ACTIVITY_SUSPICION: "500"
```

