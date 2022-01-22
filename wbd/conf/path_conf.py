import os


# =========文件夹路径配置============
# project/wbd/conf文件夹路径 (当前文件夹)
CONF_DIR_PATH = os.path.abspath(os.path.dirname(__file__))

# project/wbd 文件夹路径
WBD_DIR_PATH = os.path.abspath(os.path.dirname(CONF_DIR_PATH))

# project/ 文件夹路径
PROJECT_DIR_PATH = os.path.abspath(os.path.dirname(WBD_DIR_PATH))

# 存放gifts 文件夹路径
GIFTS_DIR_PATH = PROJECT_DIR_PATH + "/gifs"

# =========文件路径配置============
