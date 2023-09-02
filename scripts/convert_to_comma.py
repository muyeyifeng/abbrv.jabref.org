#!/usr/bin/env python3

"""
Python script to replace semicolons (;) with commas (,) in the given list of CSV files, 
and then save the processed content to new output files. 

The name of each output file is generated by appending _comma to the original file name.

"""

import csv


def convert_semicolon_to_comma(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile, delimiter=';')
        data = list(csv_reader)

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)
        csv_writer.writerows(data)


import_order = [
    'journals/journal_abbreviations_acs.csv',
    'journals/journal_abbreviations_ams.csv',
    'journals/journal_abbreviations_general.csv',
    'journals/journal_abbreviations_geology_physics.csv',
    'journals/journal_abbreviations_ieee.csv',
    'journals/journal_abbreviations_lifescience.csv',
    'journals/journal_abbreviations_mathematics.csv',
    'journals/journal_abbreviations_mechanical.csv',
    'journals/journal_abbreviations_meteorology.csv',
    'journals/journal_abbreviations_sociology.csv',
    'journals/journal_abbreviations_webofscience-dots.csv',
    'journals/journal_abbreviations_entrez.csv',
    'journals/journal_abbreviations_medicus.csv',
    'journals/journal_abbreviations_webofscience-dotless.csv',
    'journals/journal_abbreviations_aea.csv',
    'journals/journal_abbreviations_annee-philologique.csv',
    'journals/journal_abbreviations_astronomy.csv',
    'journals/journal_abbreviations_dainst.csv',
    'journals/journal_abbreviations_geology_physics_variations.csv',
    'journals/journal_abbreviations_ieee_strings.csv'
]

for input_file in import_order:
    output_file = input_file.replace('.csv', '_comma.csv')
    convert_semicolon_to_comma(input_file, output_file)
    print(f"Convert `;` to `,` for {output_file}")
