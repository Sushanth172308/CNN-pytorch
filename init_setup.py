#anoter way to setup environment
import os
print('SART')
#echo [$(date)]: "START"
#echo [$(date)]: "creating environment"
os.system('conda create --prefix ./env python=3.7 -y')
#echo [$(date)]: "activate environment"
os.system('source activate ./env')
#echo [$(date)]: "install requirements"
os.system('pip install -r requirements.txt')
#echo [$(date)]: "END"