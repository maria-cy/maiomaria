# maiomaria (Virtual Diabetes Clinic Triage)

Version 1:
```
$ docker pull ghcr.io/maria-cy/maiomaria:v0.2
```
Version 2:
```
$ docker pull ghcr.io/maria-cy/maiomaria:v0.1
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
