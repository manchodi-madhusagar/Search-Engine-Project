echo [$(date)]: "START"
echo [$(date)]: "create env with python 3.11.7 version"
conda create --predfix ./venvs  python=3.11.7 -y
echo [$(date)]: "activate env"
source activate ./venvs
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "END"