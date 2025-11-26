def hex_to_guid(hex_bytes):
    if len(hex_bytes) != 16:
        raise ValueError("Un GUID GPT doit contenir exactement 16 octets.")

    # Conversion en little-endian pour les 3 premiers champs
    data1 = hex_bytes[3:4] + hex_bytes[2:3] + hex_bytes[1:2] + hex_bytes[0:1]
    data2 = hex_bytes[5:6] + hex_bytes[4:5]
    data3 = hex_bytes[7:8] + hex_bytes[6:7]
    data4 = hex_bytes[8:16]  # big-endian

    # Formatage en chaîne hexadécimale
    guid_str = (
        ''.join(f'{b:02X}' for b in data1) + '-' +
        ''.join(f'{b:02X}' for b in data2) + '-' +
        ''.join(f'{b:02X}' for b in data3) + '-' +
        ''.join(f'{b:02X}' for b in data4[:2]) + '-' +
        ''.join(f'{b:02X}' for b in data4[2:])
    )
    return guid_str

def main():
    print("🔧 Entrez les 16 octets hexadécimaux du GUID GPT (ex: E3 C9 E3 16 5C 0B B8 4D 81 7D F9 2D F0 02 15 AE)")
    user_input = input("👉 Octets hexadécimaux : ")

    # Nettoyage et conversion
    hex_strs = user_input.replace(',', ' ').split()
    try:
        hex_bytes = [int(h, 16) for h in hex_strs]
        guid = hex_to_guid(hex_bytes)
        print(f"✅ GUID GPT : {guid}")
    except ValueError as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()
