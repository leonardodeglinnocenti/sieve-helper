# window.py
#
# Copyright 2023 Leonardo Degl'Innocenti
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw
from gi.repository import Gtk
import copy

@Gtk.Template(resource_path='/com/leonardodeglinnocenti/SieveHelper/window.ui')
class SieveHelperWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'SieveHelperWindow'

    # Connections of UI elements here
    text_entry = Gtk.Template.Child()
    folder_entry = Gtk.Template.Child()
    from_check_button = Gtk.Template.Child()
    to_check_button = Gtk.Template.Child()
    submit_button = Gtk.Template.Child()
    entry_listbox = Gtk.Template.Child()
    folders_listbox = Gtk.Template.Child()
    folder_selection = Gtk.Template.Child()
    folder_submit_button = Gtk.Template.Child()
    folders_string_list = Gtk.Template.Child()

    # Runtime variables
    entries = []
    folders = []

    # The following function finds the position of a folder in a GtkStringList
    def find_string_in_stringlist(stringlist, target):
        for k in range(len(stringlist)):
            if (stringlist.get_string(k) == target):
                return k
        return -1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.submit_button.connect("clicked", self.submit)
        self.folder_submit_button.connect("clicked", self.submit_folder)

    def submit(self, action):
        # TODO: Check if the user enters an empty entry.
        # TODO: Check consistency.
        buffer = self.text_entry.get_buffer()
        text = buffer.get_text()
        entry = Gtk.Entry(text=text)
        # Make the entry expand horizontally
        entry.set_hexpand(True)
        # Create a row to append to the ListBox
        row = Gtk.ListBoxRow()
        # Create a HBox to contain the entry and the delete button
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        delete_button = Gtk.Button(label="Delete")
        delete_button.connect("clicked", self.delete_entry, row)
        # Add folder
        selected_folder = Gtk.DropDown()
        from_check = Gtk.CheckButton(label="From")
        to_check = Gtk.CheckButton(label="To")
        if self.from_check_button.get_active():
            from_check.set_active(True)
        if self.to_check_button.get_active():
            to_check.set_active(True)
        hbox.append(entry)
        hbox.append(selected_folder)
        hbox.append(from_check)
        hbox.append(to_check)
        hbox.append(delete_button)
        row.set_child(hbox)
        self.entry_listbox.insert(row, 0)
        self.entries.append([self.folder_selection.get_selected_item().get_string(), row])
        # Resume initial state
        self.text_entry.set_buffer(Gtk.EntryBuffer())
        self.from_check_button.set_active(False)
        self.to_check_button.set_active(False)

    def delete_entry(self, action, row):
        # TODO: Avoid the first entry to be highlighted after deleting entry.
        self.entry_listbox.remove(row)

    def submit_folder(self, action):
        # TODO: Check if the user enters an empty entry.
        # TODO: Check consistency.
        buffer = self.folder_entry.get_buffer()
        text = buffer.get_text()
        entry = Gtk.Entry(text=text)
        # Make the entry expand horizontally
        entry.set_hexpand(True)
        # Create a row to append to the ListBox
        row = Gtk.ListBoxRow()
        # Add folder to env variable
        self.folders.append(text)
        self.add_folder_to_dropdown(self, text)
        # Create a HBox to contain the entry and the delete button
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        delete_button = Gtk.Button(label="Delete")
        delete_button.connect("clicked", self.delete_folder, row, text)
        hbox.append(entry)
        hbox.append(delete_button)
        row.set_child(hbox)
        self.folders_listbox.insert(row, 0)
        # Resume initial state
        self.folder_entry.set_buffer(Gtk.EntryBuffer())

    def delete_folder(self, action, row, text):
        # TODO: Avoid the first entry to be highlighted after deleting entry.
        self.folders.remove(text)
        self.folders_listbox.remove(row)
        # Delete all entries related to this folder
        for entry in self.entries:
            if entry[0] == text:
                self.delete_entry(action, row=entry[1])
        self.remove_folder_from_dropdown(self, text)

    def add_folder_to_dropdown(self, action, text):
        self.folders_string_list.append(text)

    def remove_folder_from_dropdown(self, action, text):
        position = SieveHelperWindow.find_string_in_stringlist(self.folders_string_list, text)
        self.folders_string_list.remove(position)





