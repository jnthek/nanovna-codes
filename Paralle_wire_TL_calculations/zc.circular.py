# -*- coding: utf-8 -*-


VERSION = 201612


'''
DESCRIPTION
    This is a calculator for designing
    parallel circular conductor transmission lines.


USAGE
    See: http://hamwaves.com/zc.circular/en/index.html


COPYRIGHT
    Copyright (C) 2015-2016  Serge Y. Stroobandt

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


CONTACT
    xdg-open mailto:$(echo c2VyZ2VAc3Ryb29iYW5kdC5jb20K |base64 -d)
'''


### IMPORTS ###

from browser import document
from math import cosh, pi, sqrt


### GLOBALS ###

c_0 = 299792458.0
mu_0 = pi * 4E-7
Z_0 = mu_0 * c_0


### FUNCTIONS ###

def calculate(event):
    
    try:
        Z_c = float(document['Z_c'].value)
        d = float(document['d'].value)
        epsilon_r = float(document['epsilon_r'].value)
        
        D = d * cosh(pi * (Z_c/Z_0) * sqrt(epsilon_r))
        document['D'].value = '%.3f' % D
        
        s = D - d
        document['s'].value = '%.3f' % s
        
    except:
        outputs = ['D', 's']
        for i in range(len(outputs)):
            document[outputs[i]].value = ''


### MAIN ###

document['brython'].style.display = 'initial'
calculate(None)


### EVENT HANDLERS ###

document['Z_c'].bind('focus', calculate)
document['d'].bind('focus', calculate)
document['epsilon_r'].bind('focus', calculate)

document['Z_c'].bind('input', calculate)
document['d'].bind('input', calculate)
document['epsilon_r'].bind('input', calculate)
