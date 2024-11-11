{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Servidor HTTP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Waiting for connections\n",
      "HTTP request received:\n",
      "b'GET / HTTP/1.1\\r\\nHost: 127.0.0.1:8080\\r\\nConnection: keep-alive\\r\\nsec-ch-ua: \"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"\\r\\nsec-ch-ua-mobile: ?0\\r\\nsec-ch-ua-platform: \"Windows\"\\r\\nUpgrade-Insecure-Requests: 1\\r\\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\\r\\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\\r\\nSec-Fetch-Site: none\\r\\nSec-Fetch-Mode: navigate\\r\\nSec-Fetch-User: ?1\\r\\nSec-Fetch-Dest: document\\r\\nAccept-Encoding: gzip, deflate, br, zstd\\r\\nAccept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-GB;q=0.6\\r\\n\\r\\n'\n",
      "Waiting for connections\n",
      "HTTP request received:\n",
      "b'GET /favicon.ico HTTP/1.1\\r\\nHost: 127.0.0.1:8080\\r\\nConnection: keep-alive\\r\\nsec-ch-ua-platform: \"Windows\"\\r\\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\\r\\nsec-ch-ua: \"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"\\r\\nsec-ch-ua-mobile: ?0\\r\\nAccept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8\\r\\nSec-Fetch-Site: same-origin\\r\\nSec-Fetch-Mode: no-cors\\r\\nSec-Fetch-Dest: image\\r\\nReferer: http://127.0.0.1:8080/\\r\\nAccept-Encoding: gzip, deflate, br, zstd\\r\\nAccept-Language: en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-GB;q=0.6\\r\\n\\r\\n'\n",
      "Waiting for connections\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 19\u001b[0m\n\u001b[1;32m     17\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[1;32m     18\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mWaiting for connections\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m---> 19\u001b[0m     (recvSocket, address) \u001b[38;5;241m=\u001b[39m \u001b[43mmySocket\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43maccept\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m     20\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHTTP request received:\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m     21\u001b[0m     \u001b[38;5;28mprint\u001b[39m(recvSocket\u001b[38;5;241m.\u001b[39mrecv(\u001b[38;5;241m1024\u001b[39m))\n",
      "File \u001b[0;32m/usr/local/lib/python3.12/socket.py:295\u001b[0m, in \u001b[0;36msocket.accept\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    288\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21maccept\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[1;32m    289\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"accept() -> (socket object, address info)\u001b[39;00m\n\u001b[1;32m    290\u001b[0m \n\u001b[1;32m    291\u001b[0m \u001b[38;5;124;03m    Wait for an incoming connection.  Return a new socket\u001b[39;00m\n\u001b[1;32m    292\u001b[0m \u001b[38;5;124;03m    representing the connection, and the address of the client.\u001b[39;00m\n\u001b[1;32m    293\u001b[0m \u001b[38;5;124;03m    For IP sockets, the address info is a pair (hostaddr, port).\u001b[39;00m\n\u001b[1;32m    294\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[0;32m--> 295\u001b[0m     fd, addr \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_accept\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[1;32m    296\u001b[0m     sock \u001b[38;5;241m=\u001b[39m socket(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mfamily, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtype, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mproto, fileno\u001b[38;5;241m=\u001b[39mfd)\n\u001b[1;32m    297\u001b[0m     \u001b[38;5;66;03m# Issue #7995: if no default timeout is set and the listening\u001b[39;00m\n\u001b[1;32m    298\u001b[0m     \u001b[38;5;66;03m# socket had a (non-zero) timeout, force the new socket in blocking\u001b[39;00m\n\u001b[1;32m    299\u001b[0m     \u001b[38;5;66;03m# mode to override platform-specific socket flags inheritance.\u001b[39;00m\n",
      "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
