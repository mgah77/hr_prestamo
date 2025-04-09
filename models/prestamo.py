from odoo import models, fields, api
from odoo.exceptions import ValidationError
import math

class Prestamo(models.Model):
    _name = 'hr.prestamo'
    _description = 'Prestamos a empleados'

    name = fields.Integer(string='index', index=True)
    nombre = fields.Many2one('hr.employee', string='Empleado', required=True) 
    monto = fields.Integer(string='Monto del Prestamo', required=True)
    nro_cuotas = fields.Integer(string='Nro Cuotas', required=True)
    cuota = fields.Integer(string='Cuota', compute='_compute_cuota', store=True)
    restante = fields.Integer(string='Cuotas Restantes')
    saldo = fields.Integer(string='Saldo Restante')
    fecha = fields.Date(string='Fecha de Solicitud')
    activo = fields.Boolean(string='activo', default=False)

    @api.depends('monto', 'nro_cuotas')
    def _compute_cuota(self):
        for record in self:
            if record.monto and record.nro_cuotas:
                # Calcula la cuota y redondea hacia arriba
                record.cuota = math.ceil(record.monto / record.nro_cuotas)
            else:
                record.cuota = 0

    @api.constrains('nro_cuotas')
    def _check_cuota(self):
        for record in self:
            if record.nro_cuotas and record.nro_cuotas <= 0:
                raise ValidationError("El número de cuotas no puede ser 0 o menor.")