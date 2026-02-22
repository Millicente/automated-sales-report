import subprocess
import schedule
import time
import sys
import logging
from datetime import datetime
from pathlib import Path

Path('logs').mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)s  %(message)s',
    handlers=[
        logging.FileHandler('logs/automate_report.log'),
        logging.StreamHandler(sys.stdout),
    ]
)
log = logging.getLogger(__name__)

REPORT_SCRIPT = 'src/generate_report.py'
RUN_TIME      = '08:00'

def run_report():
    log.info('Running sales report...')
    result = subprocess.run(
        [r'env\Scripts\python.exe', REPORT_SCRIPT],
        capture_output=True,
        text=True,
        cwd='.'
    )
    if result.returncode == 0:
        log.info('Report generated successfully.')
        if result.stdout:
            log.info(result.stdout.strip())
    else:
        log.error('Report generation failed.')
        if result.stderr:
            log.error(result.stderr.strip())

def main():
    args = sys.argv[1:]

    if not args:
        run_report()
        return

    if '--daily' in args:
        log.info(f'Scheduled: daily at {RUN_TIME}')
        schedule.every().day.at(RUN_TIME).do(run_report)

    elif '--weekly' in args:
        log.info(f'Scheduled: every Monday at {RUN_TIME}')
        schedule.every().monday.at(RUN_TIME).do(run_report)

    else:
        print("Usage: python src/automate_report.py [--daily | --weekly]")
        sys.exit(1)

    run_report()
    log.info('Scheduler running...')
    while True:
        schedule.run_pending()
        time.sleep(30)

if __name__ == '__main__':
    main()
