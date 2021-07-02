# ## Structure des data_batch
# Ce sont des dictionnaires:
# ```
# {
#     'batch_label': numero du batch
#     'labels': liste des labels
#     'data': liste des pixels des images
#     'filenames': liste des noms des images
# }
# ```

import os
from PIL import Image

def __unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def __extract_batch(batch, extraction_path, label_names):
    labels      = batch[bytes('labels', encoding='utf-8')]
    filenames   = batch[bytes('filenames', encoding='utf-8')]
    img_list    = batch[bytes('data', encoding='utf-8')]

    for possible_label in set(labels):
        os.makedirs(extraction_path + os.sep + label_names[possible_label], exist_ok=True)

    for i in range(len(labels)):
        Image.fromarray(
            img_list[i].reshape((3, 1024)).T.reshape((32,32,3))
        ).save(extraction_path + os.sep + label_names[labels[i]] + os.sep + filenames[i].decode('utf-8'))

def get_meta_information(batch_meta: str) -> tuple:
    meta_dict = __unpickle(batch_meta)
    label_names = meta_dict[bytes('label_names', encoding='utf-8')]
    label_names = [ label.decode('utf-8') for label in label_names ]
    num_cases   = meta_dict[bytes('num_cases_per_batch', encoding='utf-8')]
    num_pixels  = meta_dict[bytes('num_vis', encoding='utf-8')]
    return (label_names, num_cases, num_pixels)

def extract_cifar_10(cifar_path, extraction_path):

    cifar_list = os.listdir(cifar_path)
    data_list = []
    for file in cifar_list:
        if file.startswith('data_batch'):
            data_dict = __unpickle(cifar_path + os.sep + file)
            data_list.append(data_dict)

    # Recupération d'informations sur les batchs
    label_names, _, _ = get_meta_information(cifar_path + os.sep + 'batches.meta')

    for batch in data_list:
        __extract_batch(batch, extraction_path + os.sep + 'train', label_names)

    # Traitement des données de test
    test_batch = __unpickle(cifar_path + os.sep + 'test_batch')
    __extract_batch(test_batch, extraction_path + os.sep + 'test', label_names)

    return label_names


