# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models, _


class ResPartner(models.Model):
    """
    Inheriting model 'res.partner' to add the function to send SMS.
    Methods:
        send_sms():
            Opens the Send SMS wizard.
    """
    _inherit = 'res.partner'

    def send_sms(self):
        """
        Function to open Send SMS wizard.
        Returns:
            dict: the action window of 'send.sms'.
        """
        record_ids = self.env.context.get('active_ids')
        numbers = self.env['res.partner'].browse(record_ids).mapped('mobile')
        return {
            'name': _('Send SMS'),
            'type': 'ir.actions.act_window',
            'res_model': 'send.sms',
            'context': {
                'default_sms_to': ','.join([str(numb) for numb in numbers]),
            },
            'view_mode': 'form',
            'target': 'new'
        }
