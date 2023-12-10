# Website2Book
This program is used for a convert of a HTML into a EBook/EPUB format. It's mainly based on Python 3.11.6 and Shell Script. It uses also Calibre for the convertion into the EPUB format. 

<b>For now It's not native usable for Windows user because of the Shell Scripts.</b>

## How to use
After the installation of all requirements you can execute ```start.sh``` within the root folder of the repository.

```bash
#!/bin/bash
./start.sh
```

After that you need a URL of an chapter your choice. The program generates with this information a list of the chapters for the requests. You can see these generated URLs within ```App/indexURL.txt```. I recommend to look in there if you get back the error code ```404```.

The URL generation is still in progress.


## Requirements
> &GreaterGreater; 3.11.6 Python

### Installation of the base packages
```bash
#!/bin/bash
pip install requests
pip install pathlib
pip install regex
```

### Other
Other requirements like Calibre will be installed locally within the folder `Resources`.

## Important
It's only testes on Arch based Linux systems. The installation could be a bit different on other Linux based systems.

The license excludes Calibre because it is not developed by me and is only integrated into the project. I have no rights on Calibre.