
# bin to png Image Converter App

  

This simple PyQt5 application allows users to convert binary image files to PNG format. The application provides a graphical user interface (GUI) for selecting input files, converting them, and previewing the results.

  ![App Preview](https://i.imgur.com/ApXBDFd.png)

## Features

  

- Select input file using a file dialog.

- Convert binary image files to PNG format.

- Display a preview of the converted image.

  

## Prerequisites  

Make sure you have Python installed on your system. 

```bash

# Install the dependencies

pip  install  PyQt5  numpy  Pillow

```
## Usage

 1.  Run the `main.py` file to launch the application.
2.  Click the "Browse" button to select a binary image file.
3.  The output file path will be displayed automatically.
4.  Click the "Convert" button to convert the image.
5.  The converted image preview will be displayed.

## Project Structure
-   `main.py`: Main application file.
-   `image_converter.py`: Contains the `ImageConverterApp` class.
-   `image_processing.py`: Contains the image processing functions.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).

Feel free to customize this README to provide more details about your project, such as additional features, known issues, or how others can contribute.