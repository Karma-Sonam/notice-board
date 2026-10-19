# CTE412 Practical  

## Software versions
- Windows 11 / WSL2; Docker Desktop 4.x; kind v0.23+; kubectl v1.30+; Kubernetes v1.30 (kind node image)
- Application: Python 3.12 on `python:3.12-alpine`

## Repository Structure
```text
├── README.md
├── cluster/
│   └── kind-cluster.yaml
├── app/
│   ├── app.py
│   └── Dockerfile
├── manifests/
│   ├── base/                  # Namespace, ResourceQuota, LimitRange, monitor pod
│   ├── rolling/               # RollingUpdate & Recreate deployment manifests
│   └── bluegreen/             # Blue/Green deployments, services, and feature flag ConfigMap
├── scripts/
│   └── summarise.sh           # Log analyser script for availability monitor logs
├── evidence/                  # Captured text outputs and logs
└── report/
    └── report.pdf          # Assessed lab report