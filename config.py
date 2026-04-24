# ============================================================
# Developer: Nazish Khalid
# Date: 2026-04-25
# Description: Updated database host and added timeout setting
#
# Developer: IDK 
# Date: 2026-04-25
# Description: Added health check interval configuration
# Conflict Resolution: Kept sakila-db-server as MYSQL_HOST,
# included both CONNECTION_TIMEOUT and HEALTH_CHECK_INTERVAL
# ============================================================

import os

class Config:
    """Application configuration loaded from environment variables."""
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sakila-db-server')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'admin')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'sakila')
    CONNECTION_TIMEOUT = int(os.environ.get('CONNECTION_TIMEOUT', '30'))
    HEALTH_CHECK_INTERVAL = int(os.environ.get('HEALTH_CHECK_INTERVAL', '10'))