# dialogs.py
#
# Copyright 2024 Francisco Curin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw

class DialogRun(object):

    @staticmethod
    def about():
        dialog = Adw.AboutWindow(transient_for=self.props.active_window,
            application_name='storehub',
            application_icon='com.github.ffrancoc.StoreHub',
            developer_name='Francisco Curin',
            version='0.1.0',
            developers=['Francisco Curin'],
            copyright='© 2024 Francisco Curin')
        return dialog

