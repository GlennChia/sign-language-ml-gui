# Sign language machine learning GUI

# 1. Table of contents <a name="TOC"></a>

1. [Table of contents](#TOC)
2. [Directory structure](#DS)
3. [Final files and instructions on running them](#INSTRUCTIONS)
4. [References](#REFERENCES)

# 2. Directory structure <a name="DS"></a>

```
src
  |_ static
  |_ templates
    |_ index.html
  |_ utils
    |_ allowed_files.py
  |_ app.py
```

# 3. Final files and instructions on running them <a name="INSTRUCTIONS"></a>

First set up the python environment

1. Create the python enviornment
   ```bash
   python -m venv venv
   ```
2. Activate the environment
   ```bash
   venv\Scripts\activate
   ```
3. Install packages
   ```bash
   pip install -r requirements.txt
   ```
4. To exit environment
   ```bash
   cd src
   flask run
   ```
5. To exit environment
   ```bash
   deactivate
   ```

# 4. References <a name="REFERENCES"></a>

First set up the python environment

[Upload and display image in Flask](https://roytuts.com/upload-and-display-image-using-python-flask/)

- `form` to upload the image
- `flash` to display error and custom messages
- Image added in the `static/uploads` directory

[Play a video using Flask](https://stackoverflow.com/questions/55961665/flask-wont-play-a-video-in-the-html)

- `video` used to display video in `html`
- Actual video added in the `static` directory

# 5. Bug fixes

## 5.1 Installing Torch

Error: torch-1.8.1+cpu-cp38-cp38-win_amd64.whl is not a supported wheel on this platform.

Reference links:

- [Recommends checking whether python is 32 or 64 bits](https://discuss.pytorch.org/t/windows-not-a-supported-wheel-on-this-platform/17108)
  ```bash
  python -c "import struct;print( 8 * struct.calcsize('P'))"
  ```
- [Recommends downloading the .whl file and pip installing it](https://github.com/pytorch/pytorch/issues/10443)

Summary

- Ensure Python 3.8.6, 64-bit is installed
- Visit [PyTorch official website](https://pytorch.org/), configure the machine details, and run the generated command.
