import torch
import demucs.separate
import tkinter as tk
from tkinter import filedialog

# GPUが利用可能かどうかを確認
if not torch.cuda.is_available():
    raise RuntimeError("CUDA is not available. Please check your installation.")

# ルートウィンドウを作成（非表示）
root = tk.Tk()
root.withdraw()

# ファイル選択ダイアログを表示
file_path = filedialog.askopenfilename(
    title="分離したい音源ファイルを選択してください",
    filetypes=[("音声ファイル", "*.mp3 *.wav *.flac *.mp4 *.m4a")]
)

if not file_path:
    print("ファイルが選択されませんでした。")
    exit()

# 使用するモデルの名前
model_name = "htdemucs_ft"

# 出力ディレクトリ
output_dir = "D:\\stac2299\\OneDrive - 公立諏訪東京理科大学\\新しいフォルダー\\separated"

# コマンドラインオプションをリストとして設定
options = [
    file_path,
    "-n", model_name,
    "-o", output_dir,
]

# GPUを使用して分離処理の実行
demucs.separate.main(options)