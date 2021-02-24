# YOLO fine-tuning on CRC

## Running the training on the cluster

1. Login to CRC front-end machine;
2. Clone darknet and transfer other files to CRC;
3. Start an interactive shell on a cluster with GPU: `qrsh -q gpu -l gpu=1` ;
4. Replace Darknet's `Makefile` for `changes/Makefile.crc` (renaming it);
5. Load modules as follows:

    ```sh
    module load cuda cudnn opencv

    # optionally:
    module save cv2

    # now in the future you can load all modules with:
    # module restore cv2
    ```

Then follow the rest as done in Colab
   + Download the `coco256.zip` and pre-trained weights, replace the remaining files in `changes/`, compile darknet, etc.

## Extras

1. The checkpoints of trained models are saved in `backup/`, or as specified in the `backup` attribute of `data/yolo.data`.

2. Code for a single prediction:

    ```bash
    # ./darknet detect <network> <weights> <input_image>
    ./darknet detect cfg/yolov3.cfg backup/yolov3_200.weights data/dog.jpg
    ```
