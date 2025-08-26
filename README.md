# 在终端上远行：
pip install pygame chess

sudo apt install stockfish

sudo apt update

sudo apt install python3-dev python3-pip python3-pygame libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

虚拟环境
python3 -m venv .venv

source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install pygame chess

国际象棋

终端报错：
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    For more information visit http://rptl.io/venv

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
解决

# 1. 安装虚拟环境工具
sudo apt install python3-venv

# 2. 创建虚拟环境
python3 -m venv chess_env

# 3. 激活虚拟环境
source chess_env/bin/activate   # Windows 下是 chess_env\Scripts\activate

# 4. 在虚拟环境里安装
pip install pygame chess
