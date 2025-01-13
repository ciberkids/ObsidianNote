# Site
https://github.com/black-forest-labs/flux

# Run Locally
```

cd $HOME && git clone https://github.com/black-forest-labs/flux
cd $HOME/flux
python3.10 -m venv .venv
source .venv/bin/activate
pip install -e ".[all]"

```

in my case currently the git repo is cloned here

`~/Documents/projects/personal/github/flux`


https://huggingface.co/black-forest-labs/FLUX.1-schnell

```
python -m venv .venv
source .venv/bin/activate 
pip install --upgrade pip
pip install Cmake

pip install diffusers
pip install transformers
pip install torch
pip install protobuf
pip install accelerate
pip install sentencepiece


.
.
.
deactivate # to exit the venv
```