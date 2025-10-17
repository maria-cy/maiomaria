# maiomaria (Virtual Diabetes Clinic Triage)

This repository contains an MLOps project for a **virtual diabetes clinic triage**.  
It trains and serves a machine learning model that predicts short-term diabetes progression risk.  
The model and service are built, tested, and released automatically using GitHub Actions.

# Prerequisites
---
- Docker Desktop (Windows/macOS/Linux) – required to run service locally.
- Github Actions (No installation needed) – workflows run automatically in the cloud on push/PR/tag.

# Project structure
---
```
.
├─ .github/
│  └─ workflows/
│     ├─ ci.yml
│     └─ release.yml
├─ app/
│  ├─ evaluate.py
│  └─ main.py
├─ CHANGELOG.md
├─ Dockerfile
├─ README.md
├─ requirements.txt
└─ train.py

```

# Commands
---
(All commands were written using Powershell)
Choose an iteration to use:

Download Iteration 1:
```
$ docker pull ghcr.io/maria-cy/maiomaria:v0.1
```
Download Iteration 2:
```
$ docker pull ghcr.io/maria-cy/maiomaria:v0.2
```

Run command for version 2 (replace “v0.2” with “v0.1” to run iteration 1). Port used is 8000:
```
$ docker run -d -p 8000:8000 ghcr.io/maria-cy/maiomaria:v0.2
```

GET Health:
```
Invoke-RestMethod -Uri http://localhost:8000/health -Method GET
```

POST /Predict
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





