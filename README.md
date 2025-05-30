# README.md

## Project Title: Text Translator Script

A Python script that translates input text into multiple languages using Google Translate Library.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Input Format](#input-format)
  - [Output Format](#output-format)
- [Error Handling](#error-handling)
- [Notes](#notes)

---

## Overview

This script allows users to input text and translates it into multiple languages using Google Translate Library. The supported languages include Spanish, French, German, Hindi, and Tamil.

---

### Prerequisites

To run this script:

1. **Python 3.x**: A Python environment with version 3.x or higher.
2. **Packages**:
   - `googletrans==4.0.0rc1`: To install, use `pip install googletrans==4.0.0rc1`.

---

### Installation

Install the required package:

```bash
pip install googletrans==4.0.0rc1
```

---

### Usage

#### Input Format

- **Text**: A single line of text to translate.
- **Languages**: The script supports translations into:
  - Spanish: `es`
  - French: `fr`
  - German: `de`
  - Hindi: `hi`
  - Tamil: `ta`

#### Example Usage

```bash
python translate-text.py
```

The script will prompt you to enter the text to translate. You can specify the language by selecting from the supported options.

---

### Output Format

When you run the script, it will display a list of translations in the following format:

```
Language (Code): Translated Text
```

For example:
```
Spanish: "The quick brown fox jumps over the lazy dog."
```

---

### Error Handling

- **Input Errors**: If no text is provided or if an unsupported language code is selected, the script will prompt you to enter valid input.

---


### Configuration

If you want to customize the script or add more features, modify the `translate-text.py` file located in the project directory.

---

## Contact Information

For questions, suggestions, or issues with the script:

- [Koushik](mailto:skoushik1998@gmail.com)
- [Project Repository](https://github.com/adalkondan/googletranslatemodel5language)

--- 

This guide helps you understand how to use and modify the text translation script effectively.
