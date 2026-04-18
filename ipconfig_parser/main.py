from pathlib import Path
import json
def parseFiles(fileName):
    adapters = []

    with open(fileName, "r", encoding="utf-16") as file:
        content = file.readlines()

    for line in content:
        stripped = line.strip()
        
        if stripped.endswith(":") and "." not in stripped:
            current_adapter = {
                "adapter_name": stripped.rstrip(":"),
                "description": "",
                "physical_address": "",
                "dhcp_enabled": "",
                "ipv4_address": "",
                "subnet_mask": "",
                "default_gateway": "",
                "dns_servers": []
            }
            adapters.append(current_adapter)
            continue
        if " : " in stripped:
            parts = stripped.split(":", 1)
            key = parts[0].replace(".", "").strip().lower()
            value = parts[1].strip().split("(")[0].strip()

            if "description" in key:
                current_adapter["description"] = value
            elif "physical address" in key:
                current_adapter["physical_address"] = value
            elif "dhcp enabled" in key:
                current_adapter["dhcp_enabled"] = value
            elif "ipv4 address" in key:
                current_adapter["ipv4_address"] = value
            elif "subnet mask" in key:
                current_adapter["subnet_mask"] = value
            elif "default gateway" in key:
                current_adapter["default_gateway"] = value
            elif "dns servers" in key:
                if value:
                    current_adapter["dns_servers"].append(value)

    return adapters

def main():
    output = []
    for path in sorted(Path(".").glob("*.txt")):
        print(path.name)
        fileEntry = {
            "file_name": path.name,
            "adapters": parseFiles(path)
        }
        output.append(fileEntry)
        
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
        


if __name__ == "__main__":
    main()
