import parser
import librosa
import soundfile as sf
import argparse

parser = argparse.ArgumentParser(description="Resample audio file to 16000Hz")
parser.add_argument("-i", "--input", type=str, required=True, help="input audio file")
parser.add_argument("-o", "--output", type=str, required=True, help="output audio file")


def resample(input_file, output_file, sr=16000):
    """Resample audio file to 16000Hz

    Args:
        input_file (str): input audio file
        output_file (str): output audio file
        sr (int, optional): sample rate. Defaults to 16000.
    """

    y, sr_orig = librosa.load(input_file, sr=None)
    y_16k = librosa.resample(y, orig_sr=sr_orig, target_sr=sr)
    sf.write(output_file, y_16k, sr)
    print("Resampled {} to {}".format(input_file, output_file))


if __name__ == "__main__":
    args = parser.parse_args()
    resample(args.input, args.output)
