# =============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
# =============================================================================


import math

from gui.builtinGraphs.base import SmoothPointGetter


class Time2SpeedGetter(SmoothPointGetter):

    def _getCommonData(self, miscParams, fit, tgt):
        return {
            'maxSpeed': fit.ship.getModifiedItemAttr('maxVelocity'),
            'mass': fit.ship.getModifiedItemAttr('mass'),
            'agility': fit.ship.getModifiedItemAttr('agility')}

    def _calculatePoint(self, x, miscParams, fit, tgt, commonData):
        maxSpeed = commonData['maxSpeed']
        mass = commonData['mass']
        agility = commonData['agility']
        # https://wiki.eveuniversity.org/Acceleration#Mathematics_and_formulae
        y = maxSpeed * (1 - math.exp((-x * 1000000) / (agility * mass)))
        return y


class Time2DistanceGetter(SmoothPointGetter):

    def _getCommonData(self, miscParams, fit, tgt):
        return {
            'maxSpeed': fit.ship.getModifiedItemAttr('maxVelocity'),
            'mass': fit.ship.getModifiedItemAttr('mass'),
            'agility': fit.ship.getModifiedItemAttr('agility')}

    def _calculatePoint(self, x, miscParams, fit, tgt, commonData):
        maxSpeed = commonData['maxSpeed']
        mass = commonData['mass']
        agility = commonData['agility']
        # Definite integral of:
        # https://wiki.eveuniversity.org/Acceleration#Mathematics_and_formulae
        distance_t = maxSpeed * x + (maxSpeed * agility * mass * math.exp((-x * 1000000) / (agility * mass)) / 1000000)
        distance_0 = maxSpeed * 0 + (maxSpeed * agility * mass * math.exp((-0 * 1000000) / (agility * mass)) / 1000000)
        y = distance_t - distance_0
        return y
