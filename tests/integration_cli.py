from subprocess import Popen, PIPE, check_output, STDOUT
import os

current_dir = os.path.dirname(os.path.realpath(__file__))


def spawn_process_with_routine(cmd: list[str], stdin_args: list[str]):
    (pipe_r, pipe_w) = os.pipe()
    (input_r, input_w) = os.pipe()

    p = Popen(cmd,
        shell = False,
        stdout = pipe_w,
        stdin=input_r,
        stderr = pipe_w)

    finished = False
    count = 0
    output_list = []
    last_output = None
    while p.poll() is None and finished is False:
        buf = os.read(pipe_r, 1024).decode().strip()
        output_list.append(buf)

        print("<-- ", buf)

        if (count < len(stdin_args)):
            print("--> ", stdin_args[count])
            os.write(input_w, (stdin_args[count]+"\n").encode())
            count = count + 1
        else:
            finished = True
            last_output = buf

    # cleanup
    os.close(pipe_r)
    os.close(pipe_w)
    return (last_output, output_list)

    

def test_correct_encoding_and_decoding():
    args = [
        "encode",
        "super secret encoded text",
        "n"
    ]
    (last_output,_) = spawn_process_with_routine(['python3', current_dir + '/../src/main.py', current_dir + '/test.png'],args)

    args = [
        "decode",
    ]
    (last_output,_) = spawn_process_with_routine(['python3', current_dir + '/../src/main.py', current_dir + '/../test.encoded.png'],args)
    assert last_output.find("super secret encoded text") != -1


def test_correct_encryption_and_decryption():
    args = [
        "encode",
        "super secret encoded text",
        "y",
        "my secret encryption key"
    ]
    (last_output,_) = spawn_process_with_routine(['python3', current_dir + '/../src/main.py', current_dir + '/test.png'],args)

    args = [
        "decode",
        "my secret encryption key",
    ]
    (last_output,_) = spawn_process_with_routine(['python3', current_dir + '/../src/main.py', current_dir + '/../test.encoded.png'],args)
    assert last_output.find("Decrypted message: super secret encoded text") != -1



