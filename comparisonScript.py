#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:31:29 2022

@author: sdarcy2, bwinsto2
"""
import sys
sys.path.append('/usr/local/connectome_harmonic_core/connectome_harmonic_core')

import input_output as inout
import utility_functions as uts
import test_retest_fxns as t_rt
import numpy as np
from pathlib import Path
import json
from cpcrCode import saveData



#mask every receptor map. you can use uts.mask_medial_wall_vecs (which is in utility_functions insdie the CHAP repo)
    
#for each subject/session, there will be vecs.npy in
#/data/hcp_test_retest/derivatives/chap/ = chap directory
#compare each receptor map with each harmonic (each sub/session has 100)

def main() : 
    subs = inout.get_subs('/data/hcp_test_retest/derivatives/chap/')
#mask = np.load('/data2/Brian/connectome_harmonics/mask.npy')

    mapsFile = open('outputs/fsLR32k_beliveau2017maps')
    maps = json.load(mapsFile)
    #maps = np.array(maps)

#mask receptor map medial wall
    maskedMaps = {}
    mask = np.load('inputs/hcp_mask.npy')
    for rec in ['5-HT1A', '5-HT1B', '5-HT2A', '5-HT4', '5-HTT']:
        unMasked = np.array(maps[rec])
        print("Unmasked:", unMasked.shape)
        print("Mask:", mask.shape)
        maskedMaps[rec] = uts.mask_medial_wall_vecs(unMasked, mask)

#get subject vecs and generate comparison
#comparisonDictionary is a nested structure queried by subject, receptor, harmonic
#test or retest?
    comparisonDictionary = {}
    for subjects in subs:
        comparisonDictionary[subjects] = {}
        vectors = np.load('/data/hcp_test_retest/derivatives/chap/sub-' + subjects + '/ses-test/vecs.npy')
        for receptor in maskedMaps :
            comparisonDictionary[subjects][receptor] = {}
            densities = maskedMaps[receptor]
            print(vectors.shape)
            i = 0
            for i in range(vectors.shape[1]):
                print(i, "(should never exceed 100")
                vecs = vectors[:, i]
                print(vecs.shape)
                print(densities.shape)
                comparisonDictionary[subjects][receptor][i] = np.absolute(np.subtract(densities, vecs))
    output_dir = Path("outputs").resolve()
    if not output_dir.exists():
        output_dir.mkdir()

    saver = saveData("comparisons")
    saver.save(comparisonDictionary, output_dir)

if __name__ == "__main()__" :
    main()
main()

#ignore below

#chap_dir = '/data/HCP_Raw/derivatives/chap'
#subs = inout.get_subs(chap_dir)
#for sub in subs:
    #ses_dir = f'{chap_dir}/sub-{sub}/'
    #if os.path.exists(f'{ses_dir}/connectome.npz'):
        #os.remove(f'{ses_dir}/connectome.npz')