import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import torch
import tensorflow as tf



if __name__ == "__main__":
    print("检查环境")
    print(torch.__version__)
    print(torch.version.cuda)
    print(torch.backends.cudnn.version())
    print(tf.__version__)
    print(tf.config.list_physical_devices('GPU'))
