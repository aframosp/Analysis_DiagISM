#!/usr/bin/env python
# coding: utf-8
# pylint: disable=no-member
""" Code describing the telescope that help to calculate the sensitivies """

import numpy as np

import astropy.units as u
import astropy.constants as ct
from astropy.table import Table

# Constants
ANT_DIAMETER = 2 * u.m
RADIUS = ANT_DIAMETER/2
AREA = np.pi * RADIUS**2
APER_EFF = 0.8
AEFF = APER_EFF * AREA

class LuminEstimator:
    """Class to estimate the sensitivities and luminosities for the LETO-like telescope"""
    def __init__(self):
        """Create the basic data info"""
        self.createtable()

    def createtable(self):
        """Create the table with the information of the receivers"""
        data_rows = np.array([
                              ['CI [608]', 609.3],
                              ['CI [370]', 370.6],
                              ['NII [205]', 205.30],
                              ['CII [158]', 157.68],
                              ['OI [145]', 145.53],
                              ['NII [122]', 121.8],
                              ['OH [119]', 119],
                              ['OI [63]', 63.18]])  # This should be 63.18

        all_data = Table(data=data_rows, names=(
            ['Species', 'Wavelength']), dtype=['str', 'f8'])
        all_data['Wavelength'] *= u.micron
        all_data['Frequency'] = (all_data['Wavelength']).to(
            u.GHz, equivalencies=u.spectral())
        all_data['Quantum Noise'] = (
            ct.h*all_data['Frequency'] / ct.k_B).to(u.K)
        # Input
        all_data['Expected DSB TN'] = [
            40, 130, 400, 390, 400, 410, 344, 460] * u.K
        all_data['QN'] = all_data['Expected DSB TN'] / all_data['Quantum Noise']
        all_data['G_FR'] = 0.86
        all_data['T_RF'] = 50 * u.K
        all_data['G_Mix'] = [-1, -2, -4.9, -5.5, -6.5, -7.2, -6, -6] * u.db
        all_data['G_mix'] = 10**(all_data['G_Mix']/10)
        all_data['T_IF'] = 5 * u.K
        all_data['Expected Tsys'] = ((1/all_data['G_FR']-1)*all_data['T_RF'] +
                                     all_data['Expected DSB TN']/all_data['G_FR'] +
                                     all_data['T_IF']/(all_data['G_FR']*all_data['G_mix'])) * 1.05 * u.K
        all_data['Beam solid angle'] = (
            all_data['Wavelength']**2 * u.micron/AEFF).decompose() * u.sr
        all_data['Range'] = [8, 16, 16, 16, 16, 16, 16, 8] * u.GHz
        all_data['BW'] = [18, 269.85, 483.67, 633.77, 689.48, 817.23, 18, 18] * u.MHz
        self.table = all_data

    def estimate_flux(self, linew, intt, npol):
        """Estimate the flux from the input data"""
        if len(intt) == 1:
            self.table['Sensitivity DT'] = (
                npol*self.table['Expected Tsys']/np.sqrt(2*self.table['BW']*intt[0])).to(u.K)
            self.table['Channel'] = (self.table['BW'].value * self.table['BW'].unit *
                                     self.table['Wavelength']).to(u.km/u.s)
            self.table['Min Bright'] = (((2*ct.k_B*self.table['Sensitivity DT']) / (self.table['Wavelength']**2
                                                                                    * u.micron)).to(u.W * u.m**-2 * u.Hz**-1)) / u.sr
            self.table['Min Bright2'] = (
                self.table['Min Bright']*linew*self.table['Frequency']/(ct.c)).to(u.W * u.m**-2 / u.sr)
            self.table['Flux Density'] = self.table['Beam solid angle'] * \
                self.table['Min Bright'] * self.table['Min Bright'].unit
            self.table['Flux'] = (self.table['Flux Density'] * self.table['BW']
                                  * self.table['BW'].unit).to(u.W/u.m**2)
        else:
            for ind_intt in intt:
                self.table['Sensitivity DT'] = (
                    npol*self.table['Expected Tsys']/np.sqrt(2*self.table['BW']*ind_intt)).to(u.K)
                self.table['Channel'] = (self.table['BW'].value * self.table['BW'].unit *
                                         self.table['Wavelength']).to(u.km/u.s)
                self.table['Min Bright'] = (((2*ct.k_B*self.table['Sensitivity DT']) / (self.table['Wavelength']**2
                                                                                        * u.micron)).to(u.W * u.m**-2 * u.Hz**-1)) / u.sr
                self.table['Min Bright2'] = (
                    self.table['Min Bright']*linew*self.table['Frequency']/(ct.c)).to(u.W * u.m**-2 / u.sr)
                self.table['Flux Density'] = self.table['Beam solid angle'] * \
                    self.table['Min Bright'] * self.table['Min Bright'].unit
                name_flux = 'Flux %.0fh'%ind_intt.to(u.h).value
                self.table[name_flux] = (self.table['Flux Density'] * self.table['BW']
                                         * self.table['BW'].unit).to(u.W/u.m**2)


    def retrive_lum(self, distance):
        """Distance should be in Mpc"""
        if distance < 115*u.Mpc:
            distance = 115*u.Mpc
        luminosities = []
        for col in self.table.colnames:
            if col.startswith('Flux'):
                if col.endswith('h') or col.endswith('x'):
                    luminosities.append(np.log10((4*np.pi*((distance)**2) *
                                                  (self.table[col])).to(u.solLum).value))
        return luminosities
