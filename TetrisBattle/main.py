import hid

if __name__ == "__main__":
    for device in hid.enumerate():
        print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x081f, 0xe401)
gamepad.set_nonblocking(True)

while True:
    report = gamepad.read(64)
    if report:
        left = report[0] == 0
        right = report[0] == 255
        up = report[1] == 0
        down = report[1] == 255

        print(left,right,up,down)
        print(report)