# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class sale_order(osv.Model):

    _inherit = 'sale.order'
    
    def _prepare_procurement_group(self, cr, uid, order, context=None):
        res = super(sale_order,self)._prepare_procurement_group(cr, uid, order, context)
        return res
    
    
    _columns = {
        'purchase_order_ids': fields.many2many('purchase.order', 'po_so_rel', 'so_id', 'po_id', string='Purchase Orders'),
    }