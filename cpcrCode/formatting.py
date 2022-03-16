#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:31:29 2022

@author: bwinsto2
"""
import sys
sys.path.append('/usr/local/connectome_harmonic_core/connectome_harmonic_core')

import input_output as inout
import utility_functions as uts
import test_retest_fxns as t_rt
import numpy as np



#mask every receptor map. you can use uts.mask_medial_wall_vecs (which is in utility_functions insdie the CHAP repo)
    
#for each subject/session, there will be vecs.npy in
#/data/hcp_test_retest/derivatives/chap/ = chap directory
#compare each receptor map with each harmonic (each sub/session has 100)

subs = inout.get_subs('/data/hcp_test_retest/derivatives/chap/')
mask = np.load('/data2/Brian/connectome_harmonics/mask.npy')

maps = {}

for rec in ['5HTT', '5HT2A']: #etc.
    maps[rec] = '64k numpy array LH -> RH'
    
inout.save_pickle(maps,'/usr/local/receptor_maps.pkl')


#ignore below

import os

chap_dir = '/data/HCP_Raw/derivatives/chap'
subs = inout.get_subs(chap_dir)
for sub in subs:
    ses_dir = f'{chap_dir}/sub-{sub}/'
    if os.path.exists(f'{ses_dir}/connectome.npz'):
        os.remove(f'{ses_dir}/connectome.npz')