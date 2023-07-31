from odoo import fields, models, api

class Student(models.Model):
    _name = "student.student"
    _decsription = "Student"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")
    classes = fields.Char(string="Class Name")