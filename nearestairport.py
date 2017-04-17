#from GeoBases import GeoBase
#point = (40,-75)
#geo_a = GeoBase(data='airports',verbose=False)
#print(list(geo_a.findClosestFromPoint(point)))
#print()
#geo_a.visualize()

#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Drawing some lines between airports on a map.
"""

from GeoBases import GeoBase

def main():
    """Main function.
    """
    g = GeoBase('ori_por', verbose=False)

    # List of markers displayed
    markers = ['ORY', 'NCE', 'MUC', 'MAD', 'BES']

    # List of lines displayed
    lines = [
        ('ORY', 'NCE'),
        ('ORY', 'MAD'),
        ('ORY', 'MUC'),
        ('ORY', 'TLS')  # note that TLS has no marker
    ]

    g.visualize(output='the_gist',icon_label='name',add_lines=lines)       # do not draw lines from duplicates analysis



main()