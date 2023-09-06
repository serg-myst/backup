from config import DIRECTORY
import shutil
import zipfile
from zipfile import ZIP_DEFLATED
import os
from datetime import datetime
import logging


def make_archive():
    try:
        direct = os.path.join(DIRECTORY)
        current_dir = os.getcwd()
        backup_date = datetime.now().strftime('%Y_%m_%d')
        backup_catalog = os.path.join(current_dir, backup_date)
        if backup_date not in os.listdir():
            os.mkdir(backup_catalog)
        for file in os.listdir(direct):
            if file.endswith('.log'):
                shutil.move(os.path.join(direct, file), backup_catalog)
                with zipfile.ZipFile(os.path.join(backup_catalog, 'backup.zip'), mode='w',
                                     compression=ZIP_DEFLATED) as z:
                    z.write(os.path.join(backup_catalog, file))
                    os.remove(os.path.join(backup_catalog, file))
    except OSError as err:
        logging.basicConfig(level=logging.INFO, filename='backup_log',
                            format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')
        logger = logging.getLogger('backup')
        logger.error(f'ERROR = {err}')


if __name__ == '__main__':
    make_archive()
