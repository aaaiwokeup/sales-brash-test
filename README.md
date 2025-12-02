# Docker
### 1. Build Docker Image
```bash
docker build -t sales-brush-test .
```

### 2. Run Docker Container with arguments
```bash
docker run sales-brush-test --start-date 2025-06-04 --end-date 2025-06-04
```

Pass arguments --start-date or -s and --end-date or -e in ISO format YYYY-MM-DD

# Locally
### Create virtual environmet
```bash
python -m venv venv
```
### Run script
Linux
```bash
source venv/Scripts/activate
```
Windows
```bash
.\venv\Scripts\activate
```

### Run script
```bash
python run.py --start-date 2025-06-04 --end-date 2025-06-04
```
or
### Run scheduler
```bash
python scheduler.py --start-date 2025-06-04 --end-date 2025-06-04
```
Pass arguments --start-date or -s and --end-date or -e in ISO format YYYY-MM-DD