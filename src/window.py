# window.py
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

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import Gio

from .db import Database
from .login import LoginPage

@Gtk.Template(resource_path='/com/github/ffrancoc/StoreHub/gtk/window.ui')
class StorehubWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'StorehubWindow'

    nav_page = Gtk.Template.Child()


    @Gtk.Template.Callback()
    def on_close_window(self, win):
        self.settings_instance.set_int('window-width',  win.get_property('default-width'))
        self.settings_instance.set_int('window-height',  win.get_property('default-height'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings_instance = Gio.Settings(schema_id='com.github.ffrancoc.StoreHub')


        db_host = self.settings_instance.get_string('db-host')
        db_port = self.settings_instance.get_int('db-port')
        db_name = self.settings_instance.get_string('db-name')

        self.db_instance = Database(host=db_host, port=db_port, db=db_name)


        self.login_page = LoginPage(win=self)

        self.nav_page.push(self.login_page)


        self.set_default_size(self.settings_instance.get_int('window-width'), self.settings_instance.get_int('window-height'))
