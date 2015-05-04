# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class purchase_order(osv.Model):      

    _inherit = 'purchase.order'
    
    def create(self, cr, uid, vals, context=None):

        if vals.get('origin', False):

            matching_ids = self.pool.get('sale.order').search(cr, uid, args=[('name','=',vals['origin'])])
            
            if len(matching_ids) == 1:                
                vals['sale_order_ids'] = [(4, matching_ids[0] )]
                            
        return super(purchase_order, self).create(cr, uid, vals, context)
    
         
    _columns = {
        'sale_order_ids': fields.many2many('sale.order', 'po_so_rel', 'po_id', 'so_id', string='Sale Orders'),
    }