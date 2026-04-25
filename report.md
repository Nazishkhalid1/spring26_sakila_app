# DevOps Assignment Report
## Student: Nazish Khalid
## Date: April 25, 2026

---

## 1. Git Workflow Analysis

A branching strategy is essential in team environments because it allows multiple 
developers to work simultaneously without interfering with each other's code. 
In this assignment, I used a structured branching model with main, develop, 
feature, and hotfix branches. This ensured that unstable code never reached 
the main branch directly.

Git merge creates a new merge commit that combines two branches, preserving the 
complete history of both branches. Git rebase moves commits from one branch on 
top of another, creating a linear history. I would use merge when working in 
teams to preserve history, and rebase when cleaning up local commits before 
pushing. The risk of rebase is rewriting shared history, which can cause 
conflicts for other developers.

---

## 2. Docker Optimization Justification

I made several key optimizations to the Dockerfile. First, I switched from 
python:3.9 to python:3.9-slim, reducing the image size significantly by 
removing unnecessary system packages. Second, I copied requirements.txt 
BEFORE copying the application code. This leverages Docker layer caching — 
if requirements.txt hasn't changed, Docker reuses the cached pip install layer, 
making subsequent builds much faster.

Third, I combined all pip install commands into one RUN instruction with 
--no-cache-dir flag, reducing the number of layers and image size. Fourth, 
I created a non-root user (appuser) to run the application, following the 
principle of least privilege. If the application is compromised, the attacker 
only gets limited permissions. Fifth, sensitive data like passwords must never 
be hardcoded in a Dockerfile because Docker images can be shared publicly and 
the secrets would be exposed to anyone who pulls the image.

---

## 3. Networking Analysis

Docker's default bridge network allows containers to communicate by IP address 
only — containers cannot reach each other by name. A user-defined bridge network 
enables automatic DNS resolution, meaning containers can reach each other using 
their container names (e.g., ping sakila-db). Docker provides an embedded DNS 
server for user-defined networks that resolves container names to their IP 
addresses automatically. This is why I created the sakila-net network — so the 
Flask app could connect to MySQL using the hostname 'sakila-db' instead of 
a hardcoded IP address.

---

## 4. Docker Compose vs Manual Commands

Docker Compose solves several problems that manual docker run commands cannot. 
It defines the entire application stack in a single file, allowing the whole 
environment to be started with one command (docker compose up). It handles 
service dependencies through depends_on, ensuring MySQL starts before Flask. 
It manages networks and volumes automatically.

The difference between docker compose down and docker compose down -v is 
significant. docker compose down stops and removes containers and networks 
but PRESERVES named volumes — meaning database data survives. docker compose 
down -v removes everything INCLUDING volumes, permanently deleting all data. 
In production, you would never use -v unless you intentionally want to 
wipe the database.

---

## 5. CI/CD Pipeline Design Decisions

I ordered the pipeline jobs as lint → test → build → security-scan deliberately. 
This implements a "fail fast" strategy — if code has style errors (lint), there 
is no point running tests. If tests fail, there is no point building a Docker 
image. Each stage acts as a quality gate, saving compute resources and giving 
developers fast feedback.

The security scan (Trivy) is configured with exit-code 0, meaning it reports 
vulnerabilities but does not block the pipeline. This is intentional — blocking 
on every vulnerability would make deployments impossible since base images 
always have some known CVEs. The report is uploaded as an artifact so the team 
can review it without being blocked. Concurrency grouping cancels in-progress 
runs when a new commit is pushed, preventing wasted resources on outdated code.

---

## 6. Production Readiness Assessment

If this application were deployed to actual production, I would implement the 
following additional practices. First, secrets management using HashiCorp Vault 
or AWS Secrets Manager instead of environment variables, ensuring passwords are 
never stored in plain text. Second, monitoring and observability using tools 
like Prometheus and Grafana to track application metrics, and centralized 
logging with ELK Stack to aggregate logs from all containers. Third, container 
orchestration using Kubernetes to handle automatic scaling, self-healing, and 
zero-downtime deployments. Kubernetes would replace Docker Compose in production, 
providing much more robust service management and load balancing capabilities.

---