# SQL Database Backup Process

This README file explains the process for backing up the SQL database used in the Django project. \
The SQL server is hosted on DigitalOcean, and the Ubuntu server running the Django project is also hosted on DigitalOcean. \
**However, it's important to note that they are independent of each other.**

## Backup Script

The backup process is automated using a backup script (`backup_script.sh`) that runs on the Ubuntu server. This script connects to the SQL server, dumps the database content, and saves it as a SQL file on the Ubuntu server.

### Script Details

- **Script Name:** `backup_script.sh`
- **Location:** `./backup_script.sh`
- **Frequency:** The script runs daily as a cron job.

## Backup Location

The backup files are stored in a designated directory on the Linux server. The directory structure is as follows:

- `communicado-YYYYMMDDHHMMSS.sql`: Backup file containing the database dump.
- `error.log`: Log file capturing any errors encountered during the backup process.

## Cron Job

A cron job is set up on the Ubuntu server to execute the backup script daily. The cron job is configured to run at midnight (`00:00`) every day.

### Cron Job Details

```cron
0 0 * * * /path/to/backup_script.sh
```

## Linux Server Backup

The Linux server itself is backed-up daily by Digital Ocean.
