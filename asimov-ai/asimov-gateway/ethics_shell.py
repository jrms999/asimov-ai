
def run_ethics_shell(input_data):
    log = []
    if "kill" in input_data.lower():
        log.append("Block: Command violates Law 1 (harm)")
    elif "leak" in input_data.lower():
        log.append("Warn: Potential data leak - check Law 4")
    else:
        log.append("Allow: No ethical violation detected")
    return log
