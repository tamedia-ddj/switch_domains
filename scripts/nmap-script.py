import pandas as pd
import numpy as np
import nmap

data_tp = pd.read_pickle('all_data.pkl')
url_ports = pd.DataFrame(columns=['url', "ip"])

nm = nmap.PortScanner()

for url in data_tp.columns:
    scanresult = nm.scan(url, arguments='-Pn')
    for ip in scanresult["scan"]:
        if "tcp" in scanresult["scan"][ip]:
            for ports, meta in scanresult["scan"][ip]["tcp"].items():
                if str(ports) + "-" + meta["name"] not in url_ports.columns.values:
                        url_ports[str(ports) + "-" + meta["name"]] = ""
        x = pd.DataFrame([[""] * len(url_ports.columns.values)], columns = url_ports.columns.values)
        x["url"] = url
        x["ip"] = ip
        if "tcp" in scanresult["scan"][ip]:
            for ports, meta in scanresult["scan"][ip]["tcp"].items():
                x[str(ports) + "-" + meta["name"]] = meta["state"]
        url_ports = url_ports.append(x, ignore_index=True)

## ermittelte Daten zwischenspeichern ##
url_ports.to_pickle('url_ports.pkl')