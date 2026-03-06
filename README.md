# Smart Duplicate Finder

Smart Duplicate Finder is a simple web application that helps detect duplicate files and similar images.

Sometimes we store the same files multiple times without realizing it. This tool helps identify those duplicates and similar images so users can manage their storage more efficiently.

## Features

- Detect duplicate files of any type using hashing
- Detect visually similar images
- Show similarity percentage for images
- Upload multiple files at once
- Simple and clean web interface

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Pillow
- ImageHash

## How It Works

For general files, the application uses **MD5 hashing** to detect exact duplicate files.

For images, the application uses **perceptual hashing (pHash)** to compare visual similarity between images. This allows the system to detect images that may be resized, compressed, or slightly modified.

## Live Demo

You can try the project here:

https://spoorthi0810.pythonanywhere.com

## Installation

Clone the repository:  https://github.com/bgpspoorthi567/smart-duplicate-finder.git


## Author

**BATTULA GURUPRASAD SPOORTHI**  
B.Tech Computer Science and Engineering  
VIT Amaravati
