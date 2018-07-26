# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:58:30 2018

@author: debja
"""

import Algorithmia
input = {
"image": "data://Aheli/b_w/IMG_20180722_203440.jpg" # Set location of your own image
}
client = Algorithmia.client('sim+66IO2gLX7K/HqnWCT3FPMjr1') #insert your own API key
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')
print (algo.pipe(input).result)