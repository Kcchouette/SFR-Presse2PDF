# SFR Presse

Like the name says, the goal is to download a newspaper from the website of SFR-Presse.

## Install it

```
apt-get update && apt-get upgrade
apt-get install build-essential 
apt-get install python
apt-get install python-pip nano
pip install fpdf
pip install pillow
```

Then, download the script `sfr_presse.py`.

## Use it

On the page of the website of your newspaper of sfrpresse (you must to go on the watch page, and using the developper tool, copy in the NETWORK, as XHR ressource, the URL of the file **material.json**)

Then run this script: `python sfr_presse.py http://<url_of_the_file_material.json>/material.json`

## Be careful

1. This script does not remove the jpeg downloaded from the website
2. This script does not work on flash version of the newspaper's reader (all newspaper BEFORE February 2016)
3. This script was tested successfully the 1rst December 2016
4. It uses the HQ version of the image, so the pdf IS NOT LIGHT (~50 MB)
5. Each page of the PDF only contains PICTURES.
