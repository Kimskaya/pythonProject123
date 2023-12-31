import subprocess

tst = "/home/user/tst"
out = "/home/user/out"
folder1 = "/home/user/folder1"
folder2 = "/home/user/folder2"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def test_step1():
 
    result1 = checkout("cd {}; 7z a {}/arx2".format(tst, out), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(out), "arx2.7z")
    assert result1 and result2, "test1 fail"


def test_step2():
    
    result1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(out, folder1), "Everything is Ok")
    result2 = checkout("cd {}; ls".format(folder1), "qwer")
    result3 = checkout("cd {}; ls".format(folder1), "asdf")
    assert result1 and result2 and result3, "test2 fail"


def test_step3():
  
    assert checkout("cd {}; 7z t arx2.7z".format(out), "Everything is Ok"), "test3 fail"


def test_step4():

    assert checkout("cd {}; 7z u ../out/arx2.7z".format(tst), "Everything is Ok"), "test4 fail"


def test_step5():
  
    result1 = checkout("cd {}; 7z l arx2.7z".format(out), "qwer")
    result2 = checkout("cd {}; 7z l arx2.7z".format(out), "asdf")
    assert result1 and result2, "test5 fail"


def test_step6():

    result1 = checkout("cd {}; 7z x arx2.7z -o{} -y".format(out, folder2), "Everything is Ok")
    result2 = checkout("ls {}".format(folder2), "qwer")
    result3 = checkout("ls {}".format(folder2), "asdf")
    result4 = checkout("ls {}".format(folder2), "q")
    result5 = checkout("ls {}".format(folder2), "zxcv")
    assert result1 and result2 and result3 and result4 and result5, "test6 fail"


def test_step7():

    result = subprocess.run("cd {}; 7z h arx2.7z".format(out), shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    text = result.stdout.split()
    result2 = checkout("cd {}; crc32 arx2.7z".format(out), text[-4].lower())
    assert result2, "test7 fail"


def test_step8():

    assert checkout("cd {}; 7z d arx2.7z".format(out), "Everything is Ok"), "test8 fail"




