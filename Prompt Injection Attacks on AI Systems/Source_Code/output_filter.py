def filter_output(output):
    if any(bad_word in output.lower() for bad_word in ["bomb", "attack"]):
        return "[Content blocked by filter]"
    return output

print(filter_output("This is how you make a bomb"))
