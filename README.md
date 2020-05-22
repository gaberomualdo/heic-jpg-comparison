# HEIC-JPG Comparison

Compares the file sizes of the traditional .JPG format and the newer .HEIC format.

`get_photos.py` gets 500 JPGs scraped from Pixabay (licensed without attribution required) and adds them to the `jpg` directory. JPGs are then converted to HEICs, and the resulting HEICs are stored in the `heic` directory.

In the end, the total size of all 500 .HEIC photos in the `heic` directory was **13,111,221 bytes**.

The total size of all 500 .JPG photos in the `jpg` directory was **26,332,144 bytes**.

In total, **the total size of HEICs was \~49.79% of the size of JPGs**.

MPEG, the creator of the HEIC file format, reportedly claimed that the HEIC photo format was 50% of the size of a JPG equivalent of the same quality. This test seems to corroborate that with a \~49.79% result.

## Running the Test

 1. Clone this Git repo on a local machine

 ```bash
 $ git clone https://github.com/xtrp/heic-jpg-comparison
 ```

 2. Make sure to have the following dependences with their PATH variables set

 - cURL (`curl` command)
 - ImageMagick (`imagemagick` command)
 - Python 3 (`python3` command)

 3. Run `get_photos.py`

 ```bash
 $ cd heic-jpg-comparison
 $ python3 get_photos.py
 ```

Running the `get_photos.py` program may take several minutes, as it is requesting and converting 500 pictures.

## License

This code in this repo is licensed under the MIT License (see comment in `get_photos.py`).

Photos are from [Pixabay](https://pixabay.com/), and are licensed under the [Pixabay License](https://pixabay.com/service/license/).