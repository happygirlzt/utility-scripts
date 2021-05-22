#
# Created on Sat May 22 2021
#
# Copyright (c) 2021 happygirlzt
#


import logging
import random
import numpy as np
import torch

def set_logger(log_path):
    """ e.g., logging.info """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Logging to a file
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s', datefmt = '%F %A %T'))
        logger.addHandler(file_handler)

        # Logging to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(message)s'))
        logger.addHandler(stream_handler)
        
def write_file(file_path, content_list):
    
    with open(file_path, 'w') as handler:
        for content in content_list:
            handler.write('%s\n' % content)
            
            
def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True