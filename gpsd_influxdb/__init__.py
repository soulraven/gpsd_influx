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

import os

from gpsd_influxdb.conf import settings
from gpsd_influxdb.utils.log import configure_logging
from gpsd_influxdb.utils import version
from gpsd_influxdb.core.exceptions import WrongPyVersion

os.environ.setdefault('GPSD_INFLUXDB_SETTINGS_MODULE', 'gpsd_influxdb.settings')
configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)

if not version.PY36:
    raise WrongPyVersion("🐍 This script requires Python 3.6+")
