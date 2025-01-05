from spleeter.separator import Separator

if __name__ == '__main__':
    # separator = Separator("spleeter:2stems") # 2つに分離
    separator = Separator("spleeter:4stems") # 4つに分離
    # separator = Separator("spleeter:5stems") # 5つに分離

    input_file = "./audio_files/goodbye.wav"

    separator.separate_to_file(input_file, "/Users/stac2299/Library/CloudStorage/OneDrive-公立諏訪東京理科大学/新しいフォルダー/output-python)