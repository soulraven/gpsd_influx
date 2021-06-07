#  -*- coding: utf-8 -*-
#
#              Copyright (C) 2018-2021 ProGeek
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time
import logging
import threading

import schedule

from gpsd_influxdb.conf import settings
from gpsd_influxdb.GpsdPusher import GpsdPusher

log = logging.getLogger('gpsd_logging')
schedule_logger = logging.getLogger('schedule')


def run_threaded(job_func, **kwargs):
    job_thread = threading.Thread(target=job_func, kwargs=kwargs)
    job_thread.daemon = True
    #job_thread.name = kwargs['dns_record']
    job_thread.start()
    job_thread.join()


if __name__ == '__main__':
    log.info("Start the GPSD InfluxDB pusher")

    gpsd_pusher = GpsdPusher()

    schedule.every(settings.SCHEDULE_UPDATE_INTERVAL).seconds.do(lambda: run_threaded(gpsd_pusher.push_data()))

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        log.info('\nKilling all service threads...')
        schedule.clear()
        log.info('Done with all threads!')
        sys.exit(1)
