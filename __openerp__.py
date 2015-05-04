# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Sale Order / Purchase Order Link',
    'category': 'Sales',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['sale','purchase'],
    'description': """
Sale Order / Purchase Order Link
================================
 * Adds a link between sale orders and purchase orders
 * When a purchase order is created, the module inspects the origin field and sees if it matches the name of a Sale Order. If yes, the PO and SO are linked automatically
   
 """,
    'data': [
        'view/purchase_order.xml',
        'view/sale_order.xml',
    ],
}
