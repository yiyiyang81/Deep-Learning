import sys
sys.path.append('../')
from pycore.tikzeng import *

# Define your architecture
arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # Layer 1: Convolution, BatchNorm, Pooling
    to_Conv("conv1", 512, 16, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2),
    to_Conv("bn1", 512, 16, offset="(0,0,0)", to="(conv1-east)", height=64, depth=64, width=1, caption="BN"),
    to_Pool("pool1", offset="(0,0,0)", to="(bn1-east)"),

    # Connection
    to_connection("conv1", "bn1"),
    to_connection("bn1", "pool1"),

    # Layer 2: Convolution, BatchNorm, Pooling
    to_Conv("conv2", 512, 32, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=4),
    to_Conv("bn2", 512, 32, offset="(0,0,0)", to="(conv2-east)", height=32, depth=32, width=1, caption="BN"),
    to_Pool("pool2", offset="(0,0,0)", to="(bn2-east)"),

    # Connection
    to_connection("pool1", "conv2"),
    to_connection("conv2", "bn2"),
    to_connection("bn2", "pool2"),

    # Layer 3: Convolution, BatchNorm, Pooling
    to_Conv("conv3", 512, 64, offset="(1,0,0)", to="(pool2-east)", height=16, depth=16, width=8),
    to_Conv("bn3", 512, 64, offset="(0,0,0)", to="(conv3-east)", height=16, depth=16, width=1, caption="BN"),
    to_Pool("pool3", offset="(0,0,0)", to="(bn3-east)"),

    # Connection
    to_connection("pool2", "conv3"),
    to_connection("conv3", "bn3"),
    to_connection("bn3", "pool3"),

    # Layer 4: Convolution, BatchNorm, Pooling
    to_Conv("conv4", 512, 128, offset="(1,0,0)", to="(pool3-east)", height=8, depth=8, width=16),
    to_Conv("bn4", 512, 128, offset="(0,0,0)", to="(conv4-east)", height=8, depth=8, width=1, caption="BN"),
    to_Pool("pool4", offset="(0,0,0)", to="(bn4-east)"),

    # Connection
    to_connection("pool3", "conv4"),
    to_connection("conv4", "bn4"),
    to_connection("bn4", "pool4"),

    # Fully Connected Layers represented by a convolution block for visualization
    to_Conv("fc1", 512, 120, offset="(1,0,0)", to="(pool4-east)", height=4, depth=4, width=2, caption="FC1"),
    to_Conv("dropout1", offset="(0.3,0,0)", to="(fc1-east)", caption="Dropout"),
    to_connection("pool4", "fc1"),
    to_connection("fc1", "dropout1"),

    to_Conv("fc2", 512, 84, offset="(0.5,0,0)", to="(dropout1-east)", height=4, depth=4, width=2, caption="FC2"),
    to_Conv("dropout2", offset="(0.3,0,0)", to="(fc2-east)", caption="Dropout"),
    to_connection("dropout1", "fc2"),
    to_connection("fc2", "dropout2"),

    to_Conv("fc3", 512, 10, offset="(0.5,0,0)", to="(fc2-east)", height=4, depth=4, width=2, caption="FC3"),
    to_connection("dropout2", "fc3"),


    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')

if __name__ == '__main__':
    main()
