import ipaddress

def is_valid_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

ip_address = input("Enter an IPv6 address: ")

if is_valid_ipv6(ip_address):
    print("✅ Valid IPv6 address.")
else:
    print("❌ Invalid IPv6 address.")


OUTPUT:
Enter an IPv6 address: 2001:db8:85a3::8a2e:370:7334
✅ Valid IPv6 address.
