#!/usr/bin/env python
#   Copyright 2017 Alex Krzos
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import logging

class Strips(object):
    def __init__(self, data):
        """
        Initialize a Hosts object. This is a subset of
        data required by the Quads object.
        """
        self.logger = logging.getLogger("Strip.Strips")
        self.logger.setLevel(logging.DEBUG)
        if 'strips' not in data:
            self.logger.error("data missing required \"Strips\" section.")
            exit(1)

        self.data = data["strips"]

    # return list of strips
    def get(self):
        return sorted(self.data.iterkeys())
