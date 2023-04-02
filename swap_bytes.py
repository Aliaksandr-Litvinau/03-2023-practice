def swap_bytes(num: int) -> int:
    """
    The function takes a positive integer 2-byte number and swaps the bytes.

    :param num: Integer to replace bytes.
    :type num: int
    :return: The value of the number with swapped bytes.
    :rtype: int
    """
    # Get low byte
    byte1 = num & 0xff
    # Get high byte
    byte2 = (num >> 8) & 0xff
    # Gather a number with swapped bytes
    swapped_num = (byte1 << 8) | byte2
    return swapped_num


if __name__ == "__main__":
    num = 0x1234  # original number
    swapped_num = swap_bytes(num)
    print(hex(swapped_num))  # 0x3412
