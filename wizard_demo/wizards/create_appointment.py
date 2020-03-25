# -*- coding: utf-8 -*-

from odoo import models, fields, _


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'
    _description = 'Create Appointment Wizard'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")


    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
        }
        self.env['hospital.appointment'].create(vals)


        # print("self.patient_id.id",self.patient_id.id)
        # print("self.appointment_date", self.appointment_date)
        # new_appointment=self.env['hospital.appointment'].create(vals)
        # context = dict(self.env.context)
        return {
            'name': _(self.patient_id.id),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'type': 'ir.actions.act_window',
            # 'domain': [('id', 'in', self.mapped('move_line_ids').mapped('move_id').ids)],
            'context': {
                'patient_id': self.patient_id.id,
            }
        }
