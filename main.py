import subprocess
import string

if __name__ == '__main__':
 def func(comand, text, mode=0):
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        if mode == 0:
            print(out)
            if text in out:
                return True
            else:
                for i in out:
                    if i in string.punctuation:
                        out = out.replace(i, ' ')
                new_list = out.split()1
                if text in new_list:
                    return True
                else:
                    return False
    else:
        return False
print(func("cat /etc/os-release", 'VERSION', 1))
