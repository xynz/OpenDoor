#! /usr/bin/env python

""" OWASP OpenDoor launcher """

#    OpenDoor Web Directory Scanner
#    Copyright (C) 2017  Stanislav Menshov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Development Team: Stanislav Menshov
#

try:
    import urllib3
    import threadpool
    import linereader
    import colorama
    import coloredlogs
    import termcolor
    import logging
    import tabulate

except ImportError:
    exit("""\t\t[!] Several dependencies wasn't installed!
                Please run sudo pip install -r requirements.txt """)

if __name__ == "__main__":

    from src import Controller , SrcError

    try:

        bootstrap = Controller()
        bootstrap.run()
    except SrcError as e:
        exit(e.message)

