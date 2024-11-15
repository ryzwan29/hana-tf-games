# Auto Deposit ETH Base for HANA Network / Auto Play Games

## Prerequisites
- Python3.10 or higher
- Python environment
- Pip or Pip3
- Screen

## Instalation
```
██████╗ ██╗   ██ ╔███████╗ ██╗    ██╗  █████╗  ███╗   ██╗
██╔══██╗ ██╗ ██║ ╚══ ███╔╝ ██║    ██║ ██╔══██╗ ████╗  ██║
██████╔╝  ████║     ███╔╝  ██║ █╗ ██║ ███████║ ██╔██╗ ██║
██╔══██╗   ██╔╝    ███╔╝   ██║███╗██║ ██╔══██║ ██║╚██╗██║
██║  ██║   ██║    ███████╗ ╚███╔███╔╝ ██║  ██║ ██║ ╚████║
╚═╝  ╚═╝   ╚═╝    ╚══════╝  ╚══╝╚══╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝
```
Run this script
```
source <(curl -s https://raw.githubusercontent.com/ryzwan29/hana-tf-games/main/install.sh)
```
Create screen
```
screen -R
```
**Edit pvkey.txt and input Private Key**
```
nano pvkey.txt
```
**Edit token.txt and input Refresh Token**
```
nano token.txt
```

run the script
```
python3 main.py
```
| **Selection**| **Function** |
|--------------|-------------------------|
| **Number 1** | Start auto TF           |
| **Number 2** | Start games (Grows & Graden)|
## Run grow and open garden boxes

**First You Need To Get Your Refresh Token**
- Open Hana Dashboard : https://hanafuda.hana.network/dashboard
- Click F12 to open console
- Find Application and choose session storage
- Select hana and copy your refreshToken
![image](image-2.png)
- Edit token.txt paste your refresh token
