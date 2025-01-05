#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
音声分離を行うスクリプト
Demucsを使用して音声トラックを分離します（ドラム、ベース、ボーカル、その他）
"""

import os
import sys
import argparse
from pathlib import Path
import demucs.separate

def create_parser():
    """コマンドライン引数のパーサーを作成"""
    parser = argparse.ArgumentParser(description='音声分離を実行します')
    parser.add_argument('--input', '-i', type=str, help='入力音声ファイルのパス')
    parser.add_argument('--output', '-o', type=str, help='出力ディレクトリのパス')
    parser.add_argument('--model', '-m', type=str, default='htdemucs_ft',
                      help='使用するモデル名 (デフォルト: htdemucs_ft)')
    parser.add_argument('--device', '-d', type=str, default='mps',
                      help='使用するデバイス (デフォルト: mps [Apple Silicon GPU])')
    return parser

def separate_audio(input_path, output_path, model_name='htdemucs_ft', device='mps'):
    """音声分離を実行する関数"""
    try:
        # 入力ファイルの存在確認
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"入力ファイルが見つかりません: {input_path}")

        # 出力ディレクトリの作成
        os.makedirs(output_path, exist_ok=True)

        print(f"処理を開始します...")
        print(f"入力ファイル: {input_path}")
        print(f"出力ディレクトリ: {output_path}")
        print(f"使用モデル: {model_name}")
        print(f"使用デバイス: {device}")

        # Demucsを実行
        demucs.separate.main([
            input_path,          # 入力ファイル
            "-n", model_name,    # モデル名
            "-o", output_path,   # 出力ディレクトリ
            "-d", device        # デバイス
        ])
        
        print("\n処理が完了しました！")
        print(f"分離されたトラックは {output_path} に保存されています")
        return True

    except FileNotFoundError as e:
        print(f"エラー: {str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}", file=sys.stderr)
        print(f"エラーの種類: {type(e).__name__}", file=sys.stderr)
        return False

def main():
    """メイン処理"""
    parser = create_parser()
    args = parser.parse_args()

    # デフォルトのパスを設定
    if args.input is None:
        args.input = os.path.expanduser("~/Music/Downloaded/2009.m4a")
    if args.output is None:
        args.output = os.path.expanduser("~/Downloads/fordj/output")

    # 音声分離を実行
    success = separate_audio(
        input_path=args.input,
        output_path=args.output,
        model_name=args.model,
        device=args.device
    )

    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())