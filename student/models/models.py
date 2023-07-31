# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo import fields, models, api

class Student(models.Model):
    _name = "student.student"
    _decsription = "Student"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")
    classes = fields.Char(string="Class Name")



# class student(models.Model):
#     _name = 'student.student'
#     _description = 'student.student'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
