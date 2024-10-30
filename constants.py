import numpy as np

GAMMA_PARAMS = {'shape': 2, 'scale': 0.05}
OBJECT_RESIZE_BOUNDS = (0.7, 1.3)
TEXTURE_RESIZE_BOUNDS = (0.5, 2)

MVTEC = {

    'hazelnut': {
        'type': 'object',
        'background_brightness': 20,
        'brightness_threshold': 20,
        'patch_size_bounds': np.array([[0.03, 0.35], [0.03, 0.35]]),
        't_object': 0.7,   
        't_overlap': 0.25,
        'intensity_logistic_params': (1/12, 24), 
        'scale': (0.7, 0.13),
        'n_patch_max': 1,
    },

    'metal_nut': {
        'type': 'object',
        'background_brightness': 20,
        'brightness_threshold': 20,
        'patch_size_bounds': np.array([[0.06, 0.80], [0.06, 0.80]]),
        't_object': 0.5,   
        'intensity_logistic_params': (1/3, 7), 
        'n_patch_max': 1,
         't_overlap': 0.25,
    },

    'leather': {
        'type': 'texture',
        'background_brightness': 1,
        'brightness_threshold': 1,
        'patch_size_bounds': np.array([[0.06, 0.80], [0.06, 0.80]]),
        't_overlap': 0.25,
        't_object': 0.5,
        'intensity_logistic_params': (1/3, 7), 
        'n_patch_max': 1,
    },
    

    'carpet': {
        'type': 'texture',
        'background_brightness': 1,
        'brightness_threshold': 1,
        'patch_size_bounds': np.array([[0.06, 0.80], [0.06, 0.80]]),
        'intensity_logistic_params': (1/3, 7),
        't_object': 0.5,
        't_overlap': 0.25,
        'n_patch_max': 1,
    },


}
