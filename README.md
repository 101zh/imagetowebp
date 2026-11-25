# imagetowebp

A CLI tool that helps you convert images files to the .webp format.

## How to install

1. Install Python version 3.14 or greater from [https://www.python.org/downloads/](https://www.python.org/downloads/) or through the command line
2. Use pip to install pipx and use pipx to install imagetowebp

### Windows

```bash
pip install pipx
python -m pipx ensurepath
python -m pipx install git+https://github.com/101zh/imagetowebp.git
```

### Linux

```bash
# Might need to run `sudo apt update` or `sudo add-apt-repository universe`
sudo apt install pipx
pipx ensurepath
pipx install git+https://github.com/101zh/imagetowebp.git
```

### Mac

1. Also install brew from [https://brew.sh/](https://brew.sh/)

```bash
brew install pipx
pipx ensurepath
pipx install git+https://github.com/101zh/imagetowebp.git
```

## How to Use imagetowebp

1. Use the help command to view all the options

```bash
imagetowebp -h
```

1. If you want to convert a **singular** image into the .webp format, use the following command

```bash
imagetowebp .\path\to\photo.png
```

1. If you want to convert a **directory** of images into the .webp format, use the following command. (Both commands are the same it is just whether you pass in a folder or file)

```bash
imagetowebp .\path\to\photosfolder\
```

1. There are other flags that can be used to alter the how the processing of image files is done, which can be seen by using `imagetowebp -h`

## Project Goal

The goal of this project is create a cli tool that is available from the command line that can convert image files to .webp files.

## MVP Scope

- Make tool installable through pip and available on PATH
- Pass arguments to image processing library
- Create the new .webp file once an image file is processed
- Error handling for invalid files or arguments
- Support for .jpg, .jpeg, .png, and .gif

## Future Plans

- Processing for a directory of files
  - If processing multiple files, use multiple threads
- Support for compression/quality settings
- Support for a wider range of image file types
- Conversion from .webp to other image file types

## Tech Stack

- VS Code
- Python 3.14
  - pillow Library
  - argparse library
- uv Python package and project manager

## Eisenhower Matrix

<table>
    <tbody>
        <tr>
            <th></th>
            <th>Urgent</th>
            <th>Non-Urgent</th>
        </tr>
        <tr>
            <td><strong>Important</strong></td>
            <td>
                <p>Do - (Your MVP)</p>
                <ul>
                    <li>Make tool installable through pip and available on PATH</li>
                    <li>Pass arguments to image processing library</li>
                    <li>Create the new .webp files once processed</li>
                    <li>Error handling for invalid files or arguments</li>
                    <li>Support for .jpg, .jpeg, .png, and .gif</li>
                </ul>
            </td>
            <td>
                <p>Schedule - (For V2.0+)</p>
                <ul>
                    <li>Processing for a directory of files</li>
                    <li>Support for compression/quality settings</li>
                    <li>If processing multiple files, use multiple threads</li>
                    <li>Support for a wider range of image file types</li>
                    <li>Conversion from .webp to other image file types</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td><strong>Non-Important</strong></td>
            <td>
                <p>Delegate - (Use a library)</p>
                <ul>
                    <li>Use library to process image files into the .webp format</li>
                    <li>Use library to handle dependency installation</li>
                    <li>Use library to parse arguments</li>
                </ul>
            </td>
            <td>
                <p>Delete - (Cut it)</p>
                <ul>
                    <li>Make a website, so people can upload files to convert</li>
                    <li>Add a GUI wrapper</li>
                    <li>Have a real-time progress bar</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

## System Diagram

![Flow chart of how the system works](System%20Diagram.drawio.png)
