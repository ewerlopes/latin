#!/usr/bin/env python
# -*- coding: utf-8 -*-

import latindic

def load_preps(file):
    with open(file, 'r') as fp:
        for line in fp:
            if len(line) == 0: continue
            if line[0] == '#': continue

            fs = line.rstrip().split()
            if len(fs) != 3: continue

            word = fs[0].decode('utf-8')
            dom = fs[1]
            ja = fs[2]
            latindic.register(word, {'pos':'preposition', 'surface':word, 'base':word, 'dominates':dom, 'ja':ja})

def load():
    load_preps('words/prep.def')
