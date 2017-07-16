#!/usr/bin/env python
# coding: utf-8

import argparse
from Bio import SeqIO
import numpy as np

def get_number_sequences(input, file_format):
    current = input.tell()
    input.seek(0)
    c = 0
    for _ in SeqIO.parse(input, file_format):
        c += 1
    input.seek(current)
    return c

def sample(input, output, file_format='fasta', number_sequences=1, seed=None):
    number_sequences_in_file = get_number_sequences(input, file_format)
    if seed is not None:
        np.random.seed(seed)
    sampled_ids = np.random.permutation(number_sequences_in_file)
    selected_ids_i = 0
    for i, record in enumerate(SeqIO.parse(input, file_format)):
        if sampled_ids[i] <  number_sequences:
            SeqIO.write(record, output, file_format)

def create_arg_parser() :
    parser = argparse.ArgumentParser(description='This script samples sequences from file.')
    parser.add_argument('--input', '-i', type=str, help='input file path')
    parser.add_argument('--output', '-o', type=str, help='output file path')
    parser.add_argument('--file_format', '-f', type=str, default='fasta', help='file format')
    parser.add_argument('--number_sequences', '-n', type=int, default=1, help='number of sampled sequences')
    parser.add_argument('--seed', '-s', type=int, default=None, help='random seed')
    return parser

if __name__ == '__main__':
    parser = create_arg_parser()
    args = parser.parse_args()
    with open(args.input) as input, open(args.output) as output :
        sample(input, output, args.file_format, args.number_sequences, args.seed)