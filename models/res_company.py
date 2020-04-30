# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    is_declaration_activite_formation = fields.Char("Numéro de déclaration d'activité de formation")
    is_capital                        = fields.Char("Capital de la société", help="ex : SAS au capital de 5000€")
    is_retard_paiement                = fields.Text("Retard de paiement")
    is_condition_escompte             = fields.Text("Conditions d'escompte")
    is_modalite_reglement             = fields.Text("Modalité de règlement")
