# -*- mode: python; coding: utf-8; -*-
# Copyright (C) 2010 Kenny Meyer <knny.myer@gmail.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""
The Start Next Timer dialog

When a timer ended and the auto_start option was disabled this dialog shows up.
"""

from gettext import gettext as _
import gtk

class StartNextTimerDialog(object):
    def __init__(self, glade_file_name, header_text, body_text):
        # TODO: Include next_timer in body_text
        self._dialog = gtk.Dialog(
            _("Start Next Timer"),
            None,
            gtk.DIALOG_DESTROY_WITH_PARENT,
            (_("_Don't start next timer"), gtk.RESPONSE_CLOSE,
             _("_Start next timer"), gtk.RESPONSE_YES))
        self._dialog.props.border_width = 6
        self._dialog.props.has_separator = False
        self._dialog.props.resizable = False
        self._dialog.vbox.props.spacing = 12
        self._dialog.set_default_response(gtk.RESPONSE_YES)

        hbox = gtk.HBox(False, 0)
        hbox.props.spacing = 12
        hbox.props.border_width = 6
        
        image = gtk.image_new_from_stock(gtk.STOCK_DIALOG_QUESTION, gtk.ICON_SIZE_DIALOG)
        image.props.yalign = 0.0
        
        label = gtk.Label('<span weight="bold" size="larger">%s</span>\n\n%s' % (header_text, body_text))
        label.props.use_markup = True
        label.props.wrap = True
        label.props.yalign = 0.0
        
        hbox.pack_start(image, False, False, 0)
        hbox.pack_start(label, False, False, 0)
        self._dialog.vbox.pack_start(hbox, False, False, 0)
        
        hbox.show_all()

    def get_response(self):
        dialog_result = self._dialog.run()
        self._dialog.hide()
        if dialog_result == gtk.RESPONSE_YES:
            return True
        else:
            return False

