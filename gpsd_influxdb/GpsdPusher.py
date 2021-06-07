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

import logging
import socket

from influxdb_client import InfluxDBClient, Point, WriteApi, WriteOptions

from gpsd_influxdb.conf import settings
from gpsd_influxdb.lib.Gpsd import Gpsd

log = logging.getLogger('gpsd_logging')

hostname = socket.gethostname()


class GpsdPusher(object):
    """

    """

    def __init__(self, url=settings.INFLUXDB_URL, token=settings.INFLUXDB_TOKEN, org=settings.INFLUXDB_ORGANIZATION,
                 debug=settings.DEBUG):
        """

        @TODO: Implement the ssl connection parameters and small optimisations
        :param url:
        :param token:
        :param org:
        :param debug:
        """

        self.url = url
        self.token = token
        self.org = org
        self.debug = debug

        self.gpsd = Gpsd()

        self.influxdb_bucket = settings.INFLUXDB_BUCKET

    def build_data(self):
        """Build the dictionary that will be used for pushing data to influxdb.

        :return:
        """
        gpsd = self.gpsd.get_current()

        # build fields dict
        data = {
            "measurement": settings.INFLUXDB_MEASURMENT,
            "tags": {
                "host": hostname
            },
            "fields": {
                'mode': gpsd.mode,
                'sats': gpsd.sats,
                'sats_valid': gpsd.sats_valid,
                'hdop': gpsd.hdop,
                'pdop': gpsd.pdop,
                'vdop': gpsd.vdop,
                'lon': gpsd.lon,
                'lat': gpsd.lat,
                'alt': gpsd.alt,
                'track': gpsd.track,
                'hspeed': gpsd.hspeed,
                'climb': gpsd.climb,
                # Estimated climb error in meters per second. Certainty unknown.
                "epc": gpsd.error['c'],
                # Ground speed uncertainty (meters/second) [eps]
                "eps": gpsd.error['s'],
                # Temporal uncertainty [ept]
                "ept": gpsd.error['t'],
                # Estimated vertical error in meters. Certainty unknown.
                "epv": gpsd.error['v'],
                # Longitude error estimate in meters. Certainty unknown.
                "epx": gpsd.error['x'],
                # Latitude error estimate in meters. Certainty unknown.
                "epy": gpsd.error['y']
            }
        }

        return data

    def push_data(self):
        """

        :return:
        """

        _db_client = InfluxDBClient(url=self.url, token=self.token, org=self.org, debug=self.debug)

        _write_api = _db_client.write_api(write_options=WriteOptions(batch_size=1))
        _write_api.write(bucket=self.influxdb_bucket, record=self.build_data())

        _write_api.close()
        _db_client.close()
