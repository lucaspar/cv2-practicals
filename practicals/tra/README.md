# Running the training on the cluster

1. Login to CRC front-end machine;
1. Clone darknet and transfer other files to CRC;
1. Start an interactive shell on cluster;
1. Replace Darknet's `Makefile` for the `Makefile.crc` in this folder;
1. Load modules:

    ```sh
    module load cuda cudnn opencv
    module save cv

    # now in the future you can load all modules with:
    # module restore cv
    ```

Then follow the rest as in Colab.
