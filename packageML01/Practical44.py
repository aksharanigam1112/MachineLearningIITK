# String Formatting

print("Price of %10s is %8.2f Rupees" % ("Apple", 123.435))  # by default it is right aligned
print("Price of %-10s is %-8.2f Rupees" % ("Apple", 123.435))  # This aligns it from the left
print("This is {0:>10s} line written by {1:<20s}".format("First", "Akshara"))  # Numbering with colon is done
                                                                                # > (Right align) < (Left Align)
x = 123
print("This value is {0:06d}".format(x)) #Right aligned.
                                            # 0 before 6 means padding fill
                                            # so the spaces vacant will be filled with 0