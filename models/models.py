# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ModuleName(models.Model):
    _inherit = 'stock.picking'



    @api.model
    def valida_entrega(self):
        pendientes=self.search([("state","in",['assigned','confirmed'])],limit=100)
        for p in pendientes:
            move=self.env['stock.move'].search([('picking_id','=',p.id)])
            for m in move:                
                values={
                            'reserved_availability':m.product_uom_qty
                        }
                m.sudo().write(values)
                move_line=self.env['stock.move.line'].search([('move_id','=',m.id)])
                domain = [
                                ("product_id", "=", m.product_id.id),
                                ("quantity", ">", 0),
                                ('location_id','=',p.location_id.id)
                            ]                
                if not move_line:
                    domain = [
                                ("product_id", "=", m.product_id.id),
                                ("quantity", ">", 0),
                                ('location_id','=',p.location_id.id)
                            ]
                    lote=self.env['stock.quant'].search(domain,order="in_date",limit=1)                       
                    vals={
                            'picking_id':p.id,
                            'move_id':m.id,
                            'product_id':m.product_id.id,
                            'product_uom_id':m.product_uom.id,
                            #'product_uom_qty':m.product_uom_qty,
                            #'product_qty':m.product_uom_qty,
                            'qty_done':m.product_uom_qty,
                            'location_id':m.location_id.id,
                            'location_dest_id':m.location_dest_id.id,
                            'lot_id':lote.lot_id.id,
                        }
                    move_line.sudo().create(vals)
                    move_line=self.env['stock.move.line'].search([('move_id','=',m.id)])                    
                else:
                    lote=self.env['stock.quant'].search(domain,order="in_date",limit=1)                       
                    vals={
                        'qty_done':m.product_uom_qty,
                        'lot_id':lote.lot_id.id
                    }
                    move_line.sudo().write(vals)
            p.button_validate()
