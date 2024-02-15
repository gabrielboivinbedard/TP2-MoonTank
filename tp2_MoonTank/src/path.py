import os
import sys

project_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
print(project_dir)
src_path = os.path.join(project_dir, 'src')
print(src_path)
asset_path = os.path.join(project_dir, 'assets')
print(asset_path)
sounds_path = os.path.join(project_dir, 'sounds')
print(sounds_path)

sys.path.append(src_path)
sys.path.append(asset_path)
sys.path.append(sounds_path)