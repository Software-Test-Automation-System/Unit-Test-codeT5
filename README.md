# CodeT5-Small Unit Test Model

This repository contains the implementation of the `CodeT5-Small Unit Test` model. Follow the instructions below to set up and run the model.

## Requirements

- **Docker** installed on your system.
- **Python** (if running locally without Docker).

---

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:
```bash
git clone git@github.com:Software-Test-Automation-System/Unit-Test-codeT5.git
```

Navigate to the project directory:
```bash
cd Unit-Test-codeT5
```

### Step 2: Download the Pretrained Model

Download the pretrained `CodeT5-Small` model from the following link:

[Google Drive - CodeT5-Small Model](https://drive.google.com/drive/folders/1RkWwGUak5Zo_P0cDl7406nNisc5mp6wy)

After downloading, place the model files in the same directory as `app.py`. The folder structure should look like this:

```
codeT5-small/
|-- app.py
|-- model.safetensors
|-- config.json
|-- tokenizer_config.json
|-- other necessary files...
```

---

## Running the Model

### Using Docker

1. **Navigate to the project directory:**
   ```bash
   cd codeT5-small
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t my_model_api .
   ```

