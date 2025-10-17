# maiomaria (Virtual Diabetes Clinic Triage)

This repository contains an MLOps project for a **virtual diabetes clinic triage**.  
It trains and serves a machine learning model that predicts short-term diabetes progression risk.  
The model and service are built, tested, and released automatically using GitHub Actions.

# Project structure
```
├─ .github/
│ └─ workflows/ # GitHub Actions workflows
│ ├─ ci.yml # Continuous Integration: lint, test, train, evaluate, upload artifacts
│ └─ release.yml # Release pipeline: retrain, build, smoke test, push image to GHCR, create release
├─ app/
│ ├─ evaluate.py # Script for model evaluation (RMSE, precision, recall)
│ └─ main.py # FastAPI application with /health and /predict endpoints
├─ CHANGELOG.md # Version history with metrics and iteration improvements
├─ Dockerfile # Docker build instructions for the FastAPI service
├─ README.md # Project documentation (this file)
├─ requirements.txt # Pinned dependencies for reproducible builds
└─ train.py # Training script for baseline (v0.1) and improved model (v0.2)
```


#Contents
---
- .github/workflows
    - ci.yml
    - release.yml 
- app
    - evaluate.py 
    - main.py 
- CHANGELOG.md
- Dockerfile
- README.md
- requirements.txt
- train.py

#Commands
---
Choose a version to use:
$ docker pull ghcr.io/maria-cy/maiomaria:v0.1
Download Version 1:
```

```
Download Version 2:
```
$ docker pull ghcr.io/maria-cy/maiomaria:v0.2
```

Run command for version 2 (replace “v0.2” with “v0.1” to run version 1):
```
$ docker run -d -p 8000:8000 ghcr.io/maria-cy/maiomaria:v0.2
```

Post method
```
$body = @{
    age = 0.02
    sex = -0.044
    bmi = 0.06
    bp = -0.03
    s1 = -0.02
    s2 = 0.03
    s3 = -0.02
    s4 = 0.02
    s5 = 0.02
    s6 = -0.001
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:8000/predict -Method POST -ContentType "application/json" -Body $body
```

Get method:
```
Invoke-RestMethod -Uri http://localhost:8000/health -Method GET
```



