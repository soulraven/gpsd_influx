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

DEBUG = False

INFLUXDB_HOST = 'localhost'
INFLUXDB_PORT = '8086'

INFLUXDB_USER = None
INFLUXDB_PASSWORD = None


INFLUXDB_DATABASE = 'gpsd'

#############################
# Global settings           #
#############################

# update interval for each push to influxDB
SCHEDULE_UPDATE_INTERVAL = 30

###########
# LOGGING #
###########

# The callable to use to configure logging
LOGGING_CONFIG = 'logging.config.dictConfig'

# Custom logging configuration.
LOGGING = {}
