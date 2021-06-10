#  -*- coding: utf-8 -*-
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

DEBUG = True

INFLUXDB_20v: bool = False

INFLUXDB_HOST: str = 'localhost'
INFLUXDB_PORT: int = 8086

INFLUXDB_USER: str = ''
INFLUXDB_PASSWORD: str = ''

INFLUXDB_TOKEN: str = '' if INFLUXDB_20v else f'{INFLUXDB_USER}:{INFLUXDB_PASSWORD}' \
    if all([INFLUXDB_USER, INFLUXDB_PASSWORD]) else ''

INFLUXDB_ORGANIZATION: str = '-'

INFLUXDB_DATABASE: str = 'ntp_server'
INFLUXDB_RETENTION_POLICY: str = 'autogen'
INFLUXDB_MEASURMENT: str = 'gpsd-python'

INFLUXDB_BUCKET: str = '' if INFLUXDB_20v else f'{INFLUXDB_DATABASE}/{INFLUXDB_RETENTION_POLICY}'

INFLUXDB_SSL: bool = False
INFLUXDB_CERT_PATH: str = ''

INFLUXDB_URL: str = '{}://{}:{}'.format('https' if INFLUXDB_SSL else 'http', INFLUXDB_HOST, INFLUXDB_PORT)

#############################
# Global settings           #
#############################

# update interval for each push to influxDB
SCHEDULE_UPDATE_INTERVAL: int = 30

###########
# LOGGING #
###########

# The callable to use to configure logging
LOGGING_CONFIG = 'logging.config.dictConfig'

# Custom logging configuration.
LOGGING = {}
