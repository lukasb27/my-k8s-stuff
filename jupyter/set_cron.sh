#!/bin/bash
{ crontab -l -u jovyan; echo '*/15 * * * * $(which python3) /home/jovyan/check_git_status.py'; } | crontab -u jovyan -