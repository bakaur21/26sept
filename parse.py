def parse_string(stri):
    parts = stri.split('0')
    parts = [part for part in parts if part]
    if len(parts) >= 3:
        f_name = parts[0]
        l_name = parts[1]
        id_value = parts[2]
        result = {
            "first_name": f_name,
            "last_name": l_name,
            "id": id_value
        }
        return result
    else:
        return None

stri= "Baljeet000kaur0002112"
parsed_data = parse_string(stri)
print(parsed_data)
