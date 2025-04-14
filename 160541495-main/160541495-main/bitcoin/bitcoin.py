import json
import requests
import sys
try:
    if len(sys.argv)==1:
        sys.exit("faltan argumentos")
    float(sys.argv[1])
except ValueError:
    sys.exit("Mal")

x="https://api.coindesk.com/v1/bpi/currentprice.json"

a=float(sys.argv[1])
btc=requests.get(x)

#print(json.dumps(btc.json(),indent=2))
price=btc.json()
j=(price["bpi"]["USD"]["rate_float"])*a
#btc=btc[USD]
print(f"${j:,.4f}")
