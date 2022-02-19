# receptorMaps
Internal repository for Sean Darcy CPCR code 

In terminal, go to working directory and type:
git clone https://github.com/SeanSDarcy2001/receptorMaps

To generate fsLR_32k receptor density maps, fill inputs folder with desired MNI152 maps to convert.

Set directory:

cd receptorMaps

Run script:

python receptorMaps.py

Output written in outputs folder, as two dictionaries corresponding to left and right hemispheres respectively. Keys are the original MNI152 file names and values are the receptor density lists.
